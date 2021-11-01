# export-feynman

While working on my thesis, I created several Feynman diagrams using the [LaTeX](https://www.latex-project.org) package [tikz-feynman](https://ctan.org/pkg/tikz-feynman). They may serve other people  either directly or as basis for derived graphs. Therefore, I publish the source code and the resulting graphs (PDF and PNG) in this repository.

Besides the Feynman graphs, the `export_feynman.py` utility can be used to extract Feynman diagrams and other [tikz](https://github.com/pgf-tikz/pgf) graphics from LaTeX sources. Extracted LaTeX commands and environments are stored in a JSON file. The JSON file can be read in a second step to create standalone .tex files that each contain one of the graphs.


## export_feynman.py

Setup
```bash
python -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
```

Example workflow
1. Extract graphics code from LaTeX source files, store extracted code in JSON file
    ```bash
    python export_feynman.py -j feynman_tikz.json -s <path to LaTeX source folder> extract
    ```
2. Optionally, adjust labels in JSON output file ([feynman_tikz.json](feynman_tikz.json) in example). This will influence the name of the created .tex and images files in the next step. See help menu for more information on the JSON file format: `python export_feynman.py -h`.

3. Create standalone .tex files in target / output folder `standalone_tex`, one file per graph
    ```bash
    python export_feynman.py -j feynman_tikz.json -t standalone_tex create
    ```

4. Compile LaTeX files (lualatex required for tikz-feynman) and clean up auxiliary files
    ```bash
    latexmk -pdflatex=lualatex -pdf -output-directory=output standalone_tex/*
    latexmk -pdflatex=lualatex -pdf -output-directory=output standalone_tex/* -c
    ```

5. Optionally, convert pdf files to png (here using [ImageMagick](https://imagemagick.org) convert)
    ```bash
    for f in output/*.pdf; do echo "Converting '$f' to png..."; convert -density 300 -colorspace GRAY "$f" "${f%.pdf}.png"; done
    ```


## Feynman Graphs

### Top Physics

#### Pair production

![feynman_ttbar_gg_s-channel](images/feynman_ttbar_gg_s-channel.png?raw=true "feynman_ttbar_gg_s-channel")

feynman_ttbar_gg_s-channel: [PDF](images/feynman_ttbar_gg_s-channel.pdf) | [PNG](images/feynman_ttbar_gg_s-channel.png) | [Tex](standalone_tex/feynman_ttbar_gg_s-channel.tex)



![feynman_ttbar_gg_t-channel](images/feynman_ttbar_gg_t-channel.png?raw=true "feynman_ttbar_gg_t-channel")

feynman_ttbar_gg_t-channel: [PDF](images/feynman_ttbar_gg_t-channel.pdf) | [PNG](images/feynman_ttbar_gg_t-channel.png) | [Tex](standalone_tex/feynman_ttbar_gg_t-channel.tex)



![feynman_ttbar_qq](images/feynman_ttbar_qq.png?raw=true "feynman_ttbar_qq")

feynman_ttbar_qq: [PDF](images/feynman_ttbar_qq.pdf) | [PNG](images/feynman_ttbar_qq.png) | [Tex](standalone_tex/feynman_ttbar_qq.tex)

---

#### Single top


![feynman_single_top_s](images/feynman_single_top_s.png?raw=true "feynman_single_top_s")

feynman_single_top_s: [PDF](images/feynman_single_top_s.pdf) | [PNG](images/feynman_single_top_s.png) | [Tex](standalone_tex/feynman_single_top_s.tex)



![feynman_single_top_t_4flavor](images/feynman_single_top_t_4flavor.png?raw=true "feynman_single_top_t_4flavor")

feynman_single_top_t_4flavor: [PDF](images/feynman_single_top_t_4flavor.pdf) | [PNG](images/feynman_single_top_t_4flavor.png) | [Tex](standalone_tex/feynman_single_top_t_4flavor.tex)



![feynman_single_top_t_5flavor](images/feynman_single_top_t_5flavor.png?raw=true "feynman_single_top_t_5flavor")

feynman_single_top_t_5flavor: [PDF](images/feynman_single_top_t_5flavor.pdf) | [PNG](images/feynman_single_top_t_5flavor.png) | [Tex](standalone_tex/feynman_single_top_t_5flavor.tex)



![feynman_single_top_tW_s-channel](images/feynman_single_top_tW_s-channel.png?raw=true "feynman_single_top_tW_s-channel")

feynman_single_top_tW_s-channel: [PDF](images/feynman_single_top_tW_s-channel.pdf) | [PNG](images/feynman_single_top_tW_s-channel.png) | [Tex](standalone_tex/feynman_single_top_tW_s-channel.tex)



![feynman_single_top_tW_t-channel](images/feynman_single_top_tW_t-channel.png?raw=true "feynman_single_top_tW_t-channel")

feynman_single_top_tW_t-channel: [PDF](images/feynman_single_top_tW_t-channel.pdf) | [PNG](images/feynman_single_top_tW_t-channel.png) | [Tex](standalone_tex/feynman_single_top_tW_t-channel.tex)


---
#### Top decay


![feynman_top_decay_hadronic](images/feynman_top_decay_hadronic.png?raw=true "feynman_top_decay_hadronic")

feynman_top_decay_hadronic: [PDF](images/feynman_top_decay_hadronic.pdf) | [PNG](images/feynman_top_decay_hadronic.png) | [Tex](standalone_tex/feynman_top_decay_hadronic.tex)



![feynman_top_decay_leptonic](images/feynman_top_decay_leptonic.png?raw=true "feynman_top_decay_leptonic")

feynman_top_decay_leptonic: [PDF](images/feynman_top_decay_leptonic.pdf) | [PNG](images/feynman_top_decay_leptonic.png) | [Tex](standalone_tex/feynman_top_decay_leptonic.tex)


---
####    ttbb - Bottom quark associated production of top quark pairs



![feynman_ttbb_electroweak](images/feynman_ttbb_electroweak.png?raw=true "feynman_ttbb_electroweak")

feynman_ttbb_electroweak: [PDF](images/feynman_ttbb_electroweak.pdf) | [PNG](images/feynman_ttbb_electroweak.png) | [Tex](standalone_tex/feynman_ttbb_electroweak.tex)



![feynman_ttbb_electroweak_2](images/feynman_ttbb_electroweak_2.png?raw=true "feynman_ttbb_electroweak_2")

feynman_ttbb_electroweak_2: [PDF](images/feynman_ttbb_electroweak_2.pdf) | [PNG](images/feynman_ttbb_electroweak_2.png) | [Tex](standalone_tex/feynman_ttbb_electroweak_2.tex)



![feynman_ttbb_gg_FSR_s-channel](images/feynman_ttbb_gg_FSR_s-channel.png?raw=true "feynman_ttbb_gg_FSR_s-channel")

feynman_ttbb_gg_FSR_s-channel: [PDF](images/feynman_ttbb_gg_FSR_s-channel.pdf) | [PNG](images/feynman_ttbb_gg_FSR_s-channel.png) | [Tex](standalone_tex/feynman_ttbb_gg_FSR_s-channel.tex)



![feynman_ttbb_gg_FSR_t-channel](images/feynman_ttbb_gg_FSR_t-channel.png?raw=true "feynman_ttbb_gg_FSR_t-channel")

feynman_ttbb_gg_FSR_t-channel: [PDF](images/feynman_ttbb_gg_FSR_t-channel.pdf) | [PNG](images/feynman_ttbb_gg_FSR_t-channel.png) | [Tex](standalone_tex/feynman_ttbb_gg_FSR_t-channel.tex)



![feynman_ttbb_noISRFSR](images/feynman_ttbb_noISRFSR.png?raw=true "feynman_ttbb_noISRFSR")

feynman_ttbb_noISRFSR: [PDF](images/feynman_ttbb_noISRFSR.pdf) | [PNG](images/feynman_ttbb_noISRFSR.png) | [Tex](standalone_tex/feynman_ttbb_noISRFSR.tex)



![feynman_ttbb_noISRFSR_2](images/feynman_ttbb_noISRFSR_2.png?raw=true "feynman_ttbb_noISRFSR_2")

feynman_ttbb_noISRFSR_2: [PDF](images/feynman_ttbb_noISRFSR_2.pdf) | [PNG](images/feynman_ttbb_noISRFSR_2.png) | [Tex](standalone_tex/feynman_ttbb_noISRFSR_2.tex)



![feynman_ttbb_qq_FSR](images/feynman_ttbb_qq_FSR.png?raw=true "feynman_ttbb_qq_FSR")

feynman_ttbb_qq_FSR: [PDF](images/feynman_ttbb_qq_FSR.pdf) | [PNG](images/feynman_ttbb_qq_FSR.png) | [Tex](standalone_tex/feynman_ttbb_qq_FSR.tex)



![feynman_ttbb_signature_ljets](images/feynman_ttbb_signature_ljets.png?raw=true "feynman_ttbb_signature_ljets")

feynman_ttbb_signature_ljets: [PDF](images/feynman_ttbb_signature_ljets.pdf) | [PNG](images/feynman_ttbb_signature_ljets.png) | [Tex](standalone_tex/feynman_ttbb_signature_ljets.tex)

---

### Higgs Physics

#### Higgs interactions


![feynman_higgs_interaction_Hff](images/feynman_higgs_interaction_Hff.png?raw=true "feynman_higgs_interaction_Hff")

feynman_higgs_interaction_Hff: [PDF](images/feynman_higgs_interaction_Hff.pdf) | [PNG](images/feynman_higgs_interaction_Hff.png) | [Tex](standalone_tex/feynman_higgs_interaction_Hff.tex)



![feynman_higgs_interaction_HHH](images/feynman_higgs_interaction_HHH.png?raw=true "feynman_higgs_interaction_HHH")

feynman_higgs_interaction_HHH: [PDF](images/feynman_higgs_interaction_HHH.pdf) | [PNG](images/feynman_higgs_interaction_HHH.png) | [Tex](standalone_tex/feynman_higgs_interaction_HHH.tex)



![feynman_higgs_interaction_HHHH](images/feynman_higgs_interaction_HHHH.png?raw=true "feynman_higgs_interaction_HHHH")

feynman_higgs_interaction_HHHH: [PDF](images/feynman_higgs_interaction_HHHH.pdf) | [PNG](images/feynman_higgs_interaction_HHHH.png) | [Tex](standalone_tex/feynman_higgs_interaction_HHHH.tex)



![feynman_higgs_interaction_HVV](images/feynman_higgs_interaction_HVV.png?raw=true "feynman_higgs_interaction_HVV")

feynman_higgs_interaction_HVV: [PDF](images/feynman_higgs_interaction_HVV.pdf) | [PNG](images/feynman_higgs_interaction_HVV.png) | [Tex](standalone_tex/feynman_higgs_interaction_HVV.tex)



![feynman_higgs_interaction_HVVH](images/feynman_higgs_interaction_HVVH.png?raw=true "feynman_higgs_interaction_HVVH")

feynman_higgs_interaction_HVVH: [PDF](images/feynman_higgs_interaction_HVVH.pdf) | [PNG](images/feynman_higgs_interaction_HVVH.png) | [Tex](standalone_tex/feynman_higgs_interaction_HVVH.tex)


---
#### Higgs production


![feynman_higgs_prod_ggF](images/feynman_higgs_prod_ggF.png?raw=true "feynman_higgs_prod_ggF")

feynman_higgs_prod_ggF: [PDF](images/feynman_higgs_prod_ggF.pdf) | [PNG](images/feynman_higgs_prod_ggF.png) | [Tex](standalone_tex/feynman_higgs_prod_ggF.tex)



![feynman_higgs_prod_ttH_gg_s-channel](images/feynman_higgs_prod_ttH_gg_s-channel.png?raw=true "feynman_higgs_prod_ttH_gg_s-channel")

feynman_higgs_prod_ttH_gg_s-channel: [PDF](images/feynman_higgs_prod_ttH_gg_s-channel.pdf) | [PNG](images/feynman_higgs_prod_ttH_gg_s-channel.png) | [Tex](standalone_tex/feynman_higgs_prod_ttH_gg_s-channel.tex)



![feynman_higgs_prod_ttH_gg_t-channel](images/feynman_higgs_prod_ttH_gg_t-channel.png?raw=true "feynman_higgs_prod_ttH_gg_t-channel")

feynman_higgs_prod_ttH_gg_t-channel: [PDF](images/feynman_higgs_prod_ttH_gg_t-channel.pdf) | [PNG](images/feynman_higgs_prod_ttH_gg_t-channel.png) | [Tex](standalone_tex/feynman_higgs_prod_ttH_gg_t-channel.tex)



![feynman_higgs_prod_ttH_qq](images/feynman_higgs_prod_ttH_qq.png?raw=true "feynman_higgs_prod_ttH_qq")

feynman_higgs_prod_ttH_qq: [PDF](images/feynman_higgs_prod_ttH_qq.pdf) | [PNG](images/feynman_higgs_prod_ttH_qq.png) | [Tex](standalone_tex/feynman_higgs_prod_ttH_qq.tex)



![feynman_higgs_prod_VBF_t-channel](images/feynman_higgs_prod_VBF_t-channel.png?raw=true "feynman_higgs_prod_VBF_t-channel")

feynman_higgs_prod_VBF_t-channel: [PDF](images/feynman_higgs_prod_VBF_t-channel.pdf) | [PNG](images/feynman_higgs_prod_VBF_t-channel.png) | [Tex](standalone_tex/feynman_higgs_prod_VBF_t-channel.tex)



![feynman_higgs_prod_VBF_u-channel](images/feynman_higgs_prod_VBF_u-channel.png?raw=true "feynman_higgs_prod_VBF_u-channel")

feynman_higgs_prod_VBF_u-channel: [PDF](images/feynman_higgs_prod_VBF_u-channel.pdf) | [PNG](images/feynman_higgs_prod_VBF_u-channel.png) | [Tex](standalone_tex/feynman_higgs_prod_VBF_u-channel.tex)



![feynman_higgs_prod_VH_WH](images/feynman_higgs_prod_VH_WH.png?raw=true "feynman_higgs_prod_VH_WH")

feynman_higgs_prod_VH_WH: [PDF](images/feynman_higgs_prod_VH_WH.pdf) | [PNG](images/feynman_higgs_prod_VH_WH.png) | [Tex](standalone_tex/feynman_higgs_prod_VH_WH.tex)



![feynman_higgs_prod_VH_ZBOX](images/feynman_higgs_prod_VH_ZBOX.png?raw=true "feynman_higgs_prod_VH_ZBOX")

feynman_higgs_prod_VH_ZBOX: [PDF](images/feynman_higgs_prod_VH_ZBOX.pdf) | [PNG](images/feynman_higgs_prod_VH_ZBOX.png) | [Tex](standalone_tex/feynman_higgs_prod_VH_ZBOX.tex)



![feynman_higgs_prod_VH_ZH](images/feynman_higgs_prod_VH_ZH.png?raw=true "feynman_higgs_prod_VH_ZH")

feynman_higgs_prod_VH_ZH: [PDF](images/feynman_higgs_prod_VH_ZH.pdf) | [PNG](images/feynman_higgs_prod_VH_ZH.png) | [Tex](standalone_tex/feynman_higgs_prod_VH_ZH.tex)


---
#### Higgs decay


![feynman_higgs_decay_H2ff](images/feynman_higgs_decay_H2ff.png?raw=true "feynman_higgs_decay_H2ff")

feynman_higgs_decay_H2ff: [PDF](images/feynman_higgs_decay_H2ff.pdf) | [PNG](images/feynman_higgs_decay_H2ff.png) | [Tex](standalone_tex/feynman_higgs_decay_H2ff.tex)



![feynman_higgs_decay_H2gammagamma](images/feynman_higgs_decay_H2gammagamma.png?raw=true "feynman_higgs_decay_H2gammagamma")

feynman_higgs_decay_H2gammagamma: [PDF](images/feynman_higgs_decay_H2gammagamma.pdf) | [PNG](images/feynman_higgs_decay_H2gammagamma.png) | [Tex](standalone_tex/feynman_higgs_decay_H2gammagamma.tex)



![feynman_higgs_decay_H2gg](images/feynman_higgs_decay_H2gg.png?raw=true "feynman_higgs_decay_H2gg")

feynman_higgs_decay_H2gg: [PDF](images/feynman_higgs_decay_H2gg.pdf) | [PNG](images/feynman_higgs_decay_H2gg.png) | [Tex](standalone_tex/feynman_higgs_decay_H2gg.tex)



![feynman_higgs_decay_H2VV](images/feynman_higgs_decay_H2VV.png?raw=true "feynman_higgs_decay_H2VV")

feynman_higgs_decay_H2VV: [PDF](images/feynman_higgs_decay_H2VV.pdf) | [PNG](images/feynman_higgs_decay_H2VV.png) | [Tex](standalone_tex/feynman_higgs_decay_H2VV.tex)



![feynman_higgs_decay_H2Zgamma](images/feynman_higgs_decay_H2Zgamma.png?raw=true "feynman_higgs_decay_H2Zgamma")

feynman_higgs_decay_H2Zgamma: [PDF](images/feynman_higgs_decay_H2Zgamma.pdf) | [PNG](images/feynman_higgs_decay_H2Zgamma.png) | [Tex](standalone_tex/feynman_higgs_decay_H2Zgamma.tex)

---
#### ttH (H->bb)


![feynman_ttH_gg2ttHbb](images/feynman_ttH_gg2ttHbb.png?raw=true "feynman_ttH_gg2ttHbb")

feynman_ttH_gg2ttHbb: [PDF](images/feynman_ttH_gg2ttHbb.pdf) | [PNG](images/feynman_ttH_gg2ttHbb.png) | [Tex](standalone_tex/feynman_ttH_gg2ttHbb.tex)



---
### Other Processes



![feynman_vjets_wjets](images/feynman_vjets_wjets.png?raw=true "feynman_vjets_wjets")

feynman_vjets_wjets: [PDF](images/feynman_vjets_wjets.pdf) | [PNG](images/feynman_vjets_wjets.png) | [Tex](standalone_tex/feynman_vjets_wjets.tex)



![feynman_vjets_wjets_2](images/feynman_vjets_wjets_2.png?raw=true "feynman_vjets_wjets_2")

feynman_vjets_wjets_2: [PDF](images/feynman_vjets_wjets_2.pdf) | [PNG](images/feynman_vjets_wjets_2.png) | [Tex](standalone_tex/feynman_vjets_wjets_2.tex)



![feynman_vjets_wjets_3](images/feynman_vjets_wjets_3.png?raw=true "feynman_vjets_wjets_3")

feynman_vjets_wjets_3: [PDF](images/feynman_vjets_wjets_3.pdf) | [PNG](images/feynman_vjets_wjets_3.png) | [Tex](standalone_tex/feynman_vjets_wjets_3.tex)



![feynman_vjets_ww](images/feynman_vjets_ww.png?raw=true "feynman_vjets_ww")

feynman_vjets_ww: [PDF](images/feynman_vjets_ww.pdf) | [PNG](images/feynman_vjets_ww.png) | [Tex](standalone_tex/feynman_vjets_ww.tex)



![feynman_vjets_wz](images/feynman_vjets_wz.png?raw=true "feynman_vjets_wz")

feynman_vjets_wz: [PDF](images/feynman_vjets_wz.pdf) | [PNG](images/feynman_vjets_wz.png) | [Tex](standalone_tex/feynman_vjets_wz.tex)



![feynman_vjets_zjets](images/feynman_vjets_zjets.png?raw=true "feynman_vjets_zjets")

feynman_vjets_zjets: [PDF](images/feynman_vjets_zjets.pdf) | [PNG](images/feynman_vjets_zjets.png) | [Tex](standalone_tex/feynman_vjets_zjets.tex)



![feynman_vjets_zz](images/feynman_vjets_zz.png?raw=true "feynman_vjets_zz")

feynman_vjets_zz: [PDF](images/feynman_vjets_zz.pdf) | [PNG](images/feynman_vjets_zz.png) | [Tex](standalone_tex/feynman_vjets_zz.tex)