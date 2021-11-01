#!/bin/env python
r"""
Allows to extract Feynman diagrams from LaTeX files that were created with the
`tikz-feynman` package. Extracted LaTeX commands and environments are stored in
a JSON file. The JSON file can be read in a second step to create
standalone .tex files that each contain one of the graphs.

The JSON file comprises key / value pairs. While a key represents a label, the
value is the extracted LaTeX code of a Feynman graph. If the original Feynman
graph source was part of figure environment, i.e. \begin{figure} ... \end
{figure}, with a LaTeX label, e.g. \label{feynman}, the label in the JSON file
will be based on this original label. The label is used as file base name of
the standalone tex file in the create step, i.e. a file with name <label>.tex
is written. With the example workflow below, this results in corresponding
output files <label>.pdf and <label>.png. Manually adjusting the labels in the
JSON file between the extract and create steps may therefore be useful to set
meaningful names. Detailed description of the label extraction

Supported actions:
    extract: Read .tex files from input folder and write JSON file containing
             extracted Feynman diagram sources.
    create:  Read JSON file and create standalone .tex files.
    print:   Print markdown snippets for each entry in JSON file.


Example workflow:
    # Extract and create
    python export_feynman.py -j feynman_tikz.json -s ../document extract
    python export_feynman.py -j feynman_tikz.json -t standalone_tex create

    # Compile and clean (lualatex required for tikz-feynman)
    latexmk -pdflatex=lualatex -pdf -output-directory=images standalone_tex/*
    latexmk -pdflatex=lualatex -pdf -output-directory=images standalone_tex/* -c

    # Optionally, convert pdf files to png (using ImageMagick convert)
    for f in images/*.pdf; do echo "Converting '$f' to png..."; convert -density 300 -colorspace GRAY "$f" "${f%.pdf}.png"; done
"""
import argparse
import collections
import itertools
import json
import glob
import os
import re
import sys


STANDALONE_TEX_TEMPLATE = r"""
\documentclass{standalone}

%%\documentclass[convert]{standalone}
%% convert: in addition to pdf output files, png files are created
%% convert options does not work properly with -output-directory option of latexmk

\usepackage{tikz-feynman}
\tikzfeynmanset{compat=1.1.0}


\begin{document}
%s
\end{document}
"""

def read_files(file_names):
    """ Generator yielding content from files.

    Args:
        param1 (list): List of files to be parsed.
    """
    for fn in file_names:
        with open(fn, "r") as f:
            file_content =  f.read()
            yield file_content

def latex_environments(file_contents, env):
    """ Generator yielding certain LaTeX environments from tex files' content.

    Args:
        param1 (list): Content from .tex files.
        param2 (str): Name of LaTeX environment to be extracted.
    """

    regex = r'(\\begin\{%s\}.*?\\end\{%s\})' % (env, env)

    for file_content in file_contents:
        matches = re.finditer(regex, file_content, re.MULTILINE | re.DOTALL)
        #yield from matches
        yield from (m.group(0) for m in matches)

def latex_commands(file_contents, command_name):
    """ Generator yielding all calls to a certain command including body.

    Because a balanced number of opening and closing curly braces needs to be
    matched, this cannot be solved by a default regular expression. The
    regex module provides a mechanism for recursive matching that can solve
    the balanced braces problem.

    Helpful links for balancing:

    Comprehensive answer with links for multiple languages:
    https://stackoverflow.com/questions/546433/regular-expression-to-match-balanced-parentheses

    Expression below is based on answer in this stackoverflow:
    https://stackoverflow.com/questions/5454322/python-how-to-match-nested-parentheses-with-regex

    Args:
        param1 (list): Content from .tex files.
        param2 (str): Name of command to be extracted.
    """
    import regex

    expr = r"""
        (                # actual capture group - start
          \\%s           # command name
          [^{]*?         # optional parameters of command in brackets
          (?<rec>        # capturing group rec
            {            # open braces for command body
              (?:        # non-capturing group
                [^{}]++  # anything but parenthesis one or more times without backtracking
                |        # or
                (?&rec)  # recursive substitute of group rec
              )*
            }            # close braces of command body
          )              # end capture group rec
        )                # actual capture group - start
    """ % (command_name)

    for file_content in file_contents:
        # VERBOSE mode allows better readable format of expression
        matches = regex.finditer(expr, file_content, flags=regex.VERBOSE)
        yield from (m.group(0) for m in matches)

def remove_prefix(s, prefix):
    return s[len(prefix):] if s.startswith(prefix) else s

def extract_labels(environment):
    regex = r'\\label\{(.*?)\}'
    labels = re.findall(regex, environment, re.MULTILINE | re.DOTALL)
    #print("labels", labels)
    return labels

def guess_labels(graphs, figures):
    """ Tries to find fitting labels to extracted graphs from surrounding figures.

    The method tries to find a figure environment that contains a graph. If a
    corresponding figure is found, the first \\label{...} after the graph
    definition is used as label for the graph. In case of label collisions or
    if multiple graphs share a common label, a counter is suffixed to the label.

    In case were a graph is defined outside of a figure environment or no label
    is assigned, the running index inside the graphs list will be used as
    pseudo-label.
    Args:
        param1 (list): List of extracted commands and environments containing
                       Feynman graph definitions.
        param2 (list): List of extracted figures.
    """

    label_counter = collections.Counter()
    for i, graph in enumerate(graphs):
        found = False
        for j, fig in enumerate(figures):
            idx = fig.find(graph)
            if idx >= 0:
                found = True
                labels = extract_labels(fig[idx:])
                try:
                    label = remove_prefix(labels[0], "fig:")
                except IndexError:
                    label = str(i)
                label = label.replace(":", "_")

                label_counter[label] += 1
                if label_counter[label] > 1:
                    label += "_" + str(label_counter[label])

                yield label

        if not found:
            yield str(i)

def extract_feynman_figures(source_directory, json_filename):
    """ Extracts Feynman graphs and stores them in JSON file.

    Feynman graphs using the `tikz-feynman` package are considered. In
    particular, they are either created with the \feynmandiagram{} command or
    they are created inside a tikzpicture environment.

    Args:
        param1 (str): Directory containing .tex files.
        param2 (str): Name of JSON output file.
    """
    tex_files = glob.glob(os.path.join(source_directory, "*.tex"))
    file_contents = read_files(tex_files)

    # create separate streams for \feynmandiagram{} commands, tikzpicture, and
    # figure environment
    file_contents_cmd, file_contents_env, file_contents_figs = \
        itertools.tee(file_contents, 3)

    #
    # feynmangraph
    #
    feynmangraph_cmds = latex_commands(
        file_contents_cmd, command_name="feynmandiagram"
        )
    # append obligatory ";" to \feynmandiagram{}; call
    feynmangraph_cmds = (f + ";" for f in feynmangraph_cmds)

    #
    # tikzpictures
    #
    tikzpictures = latex_environments(file_contents_env, env="tikzpicture")

    #
    # separate streams (command and environments) are merged again
    #
    graphs = itertools.chain(feynmangraph_cmds, tikzpictures)
    graphs = list(fig for fig in graphs)


    #
    # guess labels
    #
    figures = latex_environments(file_contents_figs, env="figure")
    figures = (f for f in figures if '\\feynmandiagram' in f or "tikz" in f)
    figures = list(figures)
    guessed_labels = guess_labels(graphs, figures)

    #
    # output
    #
    graphs = dict(zip(guessed_labels, graphs))
    with open(json_filename, "w") as f:
        json.dump(graphs, f, indent=4)

def create_standalone_tex_files(json_filename, target_directory):
    """ Reads JSON file from extract step and creates standalone .tex files.

    Args:
        param1 (str): JSON input file name.
        param2 (str): Path to directory where standalone .tex files will be
                      stored.
    """
    with open(json_filename, "r") as f:
        figs = json.load(f)

    for label, fig in figs.items():
        tex_basename = label + ".tex"
        tex_filename = os.path.join(target_directory, tex_basename)
        with open(tex_filename, "w") as f:
            print(f"Writing tex file '{tex_filename}'...")
            f.write(STANDALONE_TEX_TEMPLATE % fig)

def print_links(json_filename):
    """ Print markdown entry (img tag, links) for each item in JSON file.
    """
    markdown_template = """

![{label}](images/{label}.png?raw=true "{label}")

{label}: [PDF](images/{label}.pdf) | [PNG](images/{label}.png) | [Tex](standalone_tex/{label}.tex)
    """

    with open(json_filename, "r") as f:
        figs = json.load(f)

    for label in figs:
        print(markdown_template.format(label=label))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description=__doc__)
    parser.add_argument("-j", "--json", required=True, metavar="FILE",
        help="Path to JSON file for exporting / importing.",
        default="feynman_tikz.json")
    parser.add_argument("-s", "--source", required="extract" in sys.argv,
        metavar="FOLDER",
        help="Path to folder containing *.tex sources."
        )
    parser.add_argument("-t", "--target", required="create" in sys.argv,
        metavar="FOLDER",
        help="Path to folder where target / standalone .tex files will be "
             "written."
        )
    parser.add_argument("action", choices=["extract", "create", "print"], default=None)
    args = parser.parse_args()

    if args.action == "extract":
        print(f"Extracting Feynman graphs from tex files in folder "
            f"'{args.source}'...")
        extract_feynman_figures(
            source_directory=args.source,
            json_filename=args.json
            )

    if args.action == "create":
        print(f"Creating standalone tex files for graphs in JSON file"
        f" '{args.json}'. Output will be written to folder '{args.target}'...")
        create_standalone_tex_files(
            json_filename=args.json,
            target_directory=args.target
            )

    if args.action == "print":
        print(f"Printing markdown...")
        print_links(json_filename=args.json)
