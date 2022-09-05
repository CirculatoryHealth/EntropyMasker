## EntropyMasker

<!-- Please add a brief introduction to explain what the project is about    -->
Yipei Song<sup>1</sup>, Francesco Cisternino<sup>5</sup>, Joost Mekke<sup>2</sup>, Gert Jan de Borst<sup>2</sup>, Dominique P.V. de Kleijn<sup>2</sup>, Gerard Pasterkamp<sup>3</sup>, Aryan Vink<sup>4</sup>, Craig Glastonbury<sup>5</sup>, Sander W. van der Laan<sup>3\*</sup>, Clint L. Miller<sup>1\*</sup>. \* Authors contributed equally.

<sup>1) Center for Public Health Genomics, Department of Public Health Sciences, Department of Biochemistry and Molecular Genetics, University of Virginia, Charlottesville, VA 22908, USA. 2) Department of Vascular Surgery, Division Surgical Specialties, University Medical Center Utrecht, Utrecht University, Utrecht, the Netherlands. 3) Central Diagnostics Laboratory, Division Laboratories, Pharmacy, and Biomedical Genetics, University Medical Center Utrecht, Utrecht University, Utrecht, the Netherlands. 4) Department of Pathology, Division Laboratories, Pharmacy, and Biomedical Genetics, University Medical Center Utrecht, Utrecht University, Utrecht, the Netherlands. 5) Human Technopole, Viale Rita Levi-Montalcini, 1, 20157, Milano, Italy.</sup>


### Description

**`EntropyMasker`** is a fully automated approach for separating foreground (tissue) and background in bright-field microscopic whole-slide images of (immuno)histologically stained samples. This method is unaffected by changes in scanning or image processing conditions, by using a measure of local entropy and generating corresponding binary tissue masks.


### Scientific abstract

**Background:** Tissue segmentation of histology whole-slide images remains a critical challenge in digital pathology for both disease diagnosis and phenotyping for research purposes. When the tissue structure of a specimen is relatively porous and heterogeneous, such as for atherosclerotic plaques, precise tissue segmentation is essential for a correct interpretation. 

**Method:** In this study, we developed a unique approach called **`EntropyMasker`** based on statistical analysis and binary morphology to tackle the issue of fore- and background segmentation (masking) in histopathological [whole-slide images (WSIs)](https://pubmed.ncbi.nlm.nih.gov/32452840/), which has yet to be solved. 

**Results and conclusion:** We tested our system on large extracts from 97 high-resolution WSIs of hematoxylin and eosin and 8 other staining types on atherosclerotic plaques from the [Athero-Express Biobank Study](https://doi.org/10.1007/s10564-004-2304-6) each with different staining quality and acquired under different imaging settings. We compared our method with four other widely used methods and found that our method had the highest sensitivity and [Jaccard similarity index](https://en.wikipedia.org/wiki/Jaccard_index). We envision a positive impact of **`EntropyMasker`** to WSI-preprocessing in image analyses for disease phenotyping beyond the field of atherosclerosis. 

### Where do I start?

**`EntropyMasker`** is dependent on `python3`. You can run it locally or through a high-performance compute cluster (HPC). <!-- We created
detailed instructions in the wiki to install the necessary
`python`-libraries.-->

To run `EntropyMasker` run the following code:

    python EntropyMaster/entropyMasker.py --input_img --output_img

| Flag              | Required/Optional | Description                                    |
|------------------|------------------|-------------------------------------|
| `-i/--input_img`  | required          | complete path to the whole-slide image to mask |
| `-o/--output_img` | required          | complete path to the masked output-image       |
| `-h/--help`       | optional          | to get a usage-description                     |

_Description of commands._


### Project structure

<!--  You can add rows to this table, using "|" to separate columns.         -->

| File                      | Description                                             | Usage                       |
|---------------------------|---------------------------------------------------------|----------------------|
| README.md                 | Description of project                                  | Human editable              |
| EntropyMasker.Rproj       | R project file to generate this README.md               | Loads R project; reads only |
| LICENSE                   | User permissions                                        | Read only                   |
| EntropyMaster             | The EntropyMasker program                               | Human editable              |
| AEDB.EM.baseline.Rmd      | R Markdown notebook to produce baseline table and plots | Human editable              |
| ae_baseline               | Baseline for the 97 samples used                        | Human editable              |
| ae_output                 | Output folder for the R Markdown notebook               | Human editable              |
| ae_plots                  | Plotss folder for the R Markdown notebook               | Human editable              |
| images                    | Images used in this README.md                           | Human editable              |
| notebook                  | Jupyter notebook for this project                       | Human editable              |
| scripts                   | QuPath scripts used for this project                    | Human editable              |


### Questions and issues

<!-- Do you have burning questions or do you want to discuss usage with other users? Please use the Discussions tab.-->

Do you have burning questions or do you want to discuss usage with other users? Do you want to report an issue? Or do you have an idea for improvement or adding new features to our method and tool? Please use the [Issues tab](https://github.com/CirculatoryHealth/EntropyMasker/issues).


### Citations

Using our **`EntropyMasker`** method? Please cite our work:

    An automatic entropy method to efficiently mask histology whole-slide images
    Yipei Song, Francesco Cisternino, Joost Mekke, Gert Jan de Borst, Dominique P.V. de Kleijn, Gerard Pasterkamp, Aryan Vink, Craig Glastonbury, Sander W. van der Laan, Clint L. Miller.
    medRxiv 2022.09.01.22279487; doi: https://doi.org/10.1101/2022.09.01.22279487


### Data availability

The whole-slide images used in this project are available through a [DataverseNL repository](https://doi.org/10.34894/QI135J "ExpressScan: Histological whole-slide image data from the Athero-Express (AE) and Aneurysm-Express (AAA) Biobank Studies"). There are restrictions on use by commercial parties, and on sharing openly based on (inter)national laws, regulations and the written informed consent. Therefore these data (and additional clinical data) are only available upon discussion and signing a Data Sharing Agreement (see Terms of Access) and within a specially designed UMC Utrecht provided environment.


### Acknowledgements, disclosures, and funding

We are thankful for the support of the Netherlands CardioVascular Research Initiative of the Netherlands Heart Foundation (CVON 2011/B019 and CVON 2017-20: Generating the best evidence-based pharmaceutical targets for atherosclerosis [GENIUS I&II]), the ERA-CVD program 'druggable-MI-targets' (grant number: 01KL1802), and the Leducq Fondation 'PlaqOmics'.

Funding for this research was provided by National Institutes of Health (NIH) grant nos. R00HL125912 and R01HL14823 (to Clint L. Miller), and a Leducq Foundation Transatlantic Network of Excellence ('PlaqOmics') grant no. 18CVD02 (to Dr. Clint L. Miller and Dr. Sander W. van der Laan), and EU H2020 TO_AITION grant no. 848146 (to Dr. Sander W. van der Laan).

Dr. Sander W. van der Laan has received Roche funding for unrelated work.

Dr Craig A. Glastonbury has stock options in BenevolentAI and is a paid consultant for BenevolentAI, unrelated to this work.

Plaque samples are derived from arterial endarterectomies as part of the [Athero-Express Biobank Study](https://doi.org/10.1007/s10564-004-2304-6) which is an ongoing study in the UMC Utrecht. We would like to thank all the (former) employees involved in the Athero-Express Biobank Study of the Departments of Surgery of the St. Antonius Hospital Nieuwegein and University Medical Center Utrecht for their continuing work. In particular we would like to thank (in no particular order) Marijke Linschoten, Arjan Samani, Petra H. Homoed-van der Kraak, Tim Bezemer, Tim van de Kerkhof, Joyce Vrijenhoek, Evelyn Velema, Ben van Middelaar, Sander Reukema, Robin Reijers, Joëlle van Bennekom, and Bas Nelissen. Lastly, we would like to thank all participants of the Athero-Express Biobank Study; without you these studies would not be possible.

<center><a href='https://www.era-cvd.eu'><img src="images/ERA_CVD_Logo_CMYK.png" align="center" height="75"/></a> <a href='https://www.to-aition.eu'><img src="images/to_aition.png" align="center" height="75"/></a> <a href='https://www.plaqomics.com'><img src="images/leducq-logo-large.png" align="center" height="75"/></a> <a href='https://www.fondationleducq.org'><img src="images/leducq-logo-small.png" align="center" height="75"/></a> <a href='https://osf.io/zcvbs/'><img src="images/worcs_icon.png" align="center" height="75"/></a> <a href='https://www.atheroexpress.nl'><img src="images/AE_Genomics_2010.png" align="center" height="100"/></a></center>

#### Changes log

    Version:      v1.0.1</br>
    Last update:  2022-09-05</br>
    Written by:   Yipei Song; Craig Glastonbury; Sander W. van der Laan; Clint L. Miller.
        
    * v1.0.1 Made public. Added citation to preprint. Fix in the readme.
    * v1.0.0 Initial version.  

------------------------------------------------------------------------

#### Creative Commons BY-NC-ND 4.0

##### Copyright (c) 2022. [Yipei Song](https://github.com/PetraSong) \| [Craig Glastonbury](https://github.com/GlastonburyC) \| [Sander W. van der Laan](https://github.com/swvanderlaan) \| [Clint L. Miller](https://github.com/clintmil).
<sup>This is a human-readable summary of (and not a substitute for) the [license](LICENSE). You are free to: Share, copy and redistribute the material in any medium or format. The licencor cannot revoke these freedoms as long as you follow the license terms.</sup>

<sup>Under the following terms:</br></sup>
<sup>-   Attribution --- You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.</br></sup>
<sup>-   NonCommercial --- You may not use the material for commercial purposes.</br></sup>
<sup>-   NoDerivatives --- If you remix, transform, or build upon the material, you may not distribute the modified material.</br></sup>
<sup>-   No additional restrictions --- You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.</sup>

<sup>Notices: You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation. No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.</sup>
