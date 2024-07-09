



# DeepProg: an ensemble of deep-learning and machine-learning models for prognosis prediction using multi-omics data
  
Object ID: https://biocomputeobject.org/BCO_000453/2.0  
Spec Version: https://w3id.org/ieee/ieee-2791-schema/2791object.json  
etag: e64517ee967b5990d86e18b365b8db0371c7fb20
# Usability
  
Identifying disease subtypes (cancer) is clinically very significant in patient survival prediction  
It explicitly models patient survival as the objective and is predictive of new patient survival risks. DeepProg constructs a flexible ensemble of hybrid-models (a combination of deep-learning and machine learning models) and integrates their outputs following the ensemble learning paradigm.  
DeepProg was applied on RNA-Seq, Methylation and miRNA data from 32 cancers in The Cancer Genome Atlas (TCGA),from NCBI, with a total of around 10,000 samples.  
The results from the DeepProg method are compared to results from the Similarity Network Fusion (SNF) algorithm, used to identify cancer subtypes linked to survival by others.   
In all, DeepProg yields much better log-rank p values and C-indices than the SNF method. 
# Description

## Keywords
  
Survival, Prognosis, Multi-omics, Cancer, Ensemble learning, Deep learning, Machine learning
## External References
  

|Name|Namespace|Access Time|IDs|
| :---: | :---: | :---: | :---: |
|NCBI-GEO|NCBI.GEO|1:19PM|GSE4922, GSE1456, GSE3494, GSE7390|
|Synapse Repository|synapse-repo|1:19PM|syn1688369|

## Platform
  
Affymetrix HG-U133A microarray
## Pipeline Steps
  
***Step 1: TCGA-Assembler***  
Version: versions 2.0.5  
Description: The package TCGA-Assembler is used to write custom scripts to download RNA-Seq (UNC IlluminaHiSeq RNASeqV2), miRNA Sequencing (BCGSC IlluminaHiSeq, Level 3), and DNA methylation (JHU-USC HumanMethylation450) data from the TCGA website.  
**Input List**  

|Name|uri|Access Time|
| :---: | :---: | :---: |
|N/A|https://tcga-data.nci.nih.gov/tcga/|Tuesday 27, February 2024|
  
**Output List**  

|Name|uri|Access Time|
| :---: | :---: | :---: |
|N/A|https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8281595/bin/13073_2021_930_MOESM2_ESM.xlsx||
  
***Step 2: Gene Expression Omnibus (GEO)***  
Version:   
Description: Four public datasets (all on Affymetrix HG-U133A microarray platform) were downloaded (GSE4922, GSE1456, GSE3494, and GSE7390) , along with one Metabric RNA-Seq datasets as the validation datasets.   
**Input List**  

|Name|uri|Access Time|
| :---: | :---: | :---: |
|N/A|https://www.ncbi.nlm.nih.gov/geo/||
  
**Output List**  

|Name|uri|Access Time|
| :---: | :---: | :---: |
|N/A|https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8281595/bin/13073_2021_930_MOESM1_ESM.xlsx||
  
***Step 3: Synapse repository***  
Version:   
Description: Here the Metabric dataset was obtained with approval, and consists of 1981 breast cancer samples  
**Input List**  

|Name|uri|Access Time|
| :---: | :---: | :---: |
|N/A|https://www.synapse.org/#!Synapse:syn1688369|Tuesday 27, February 2024|
  
**Output List**  

|Name|uri|Access Time|
| :---: | :---: | :---: |
|N/A|https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8281595/bin/13073_2021_930_MOESM7_ESM.docx|Tuesday 27, February 2024|

# Parametric Domain
  

|Parameter|Step|Value|
| :---: | :---: | :---: |
|training set|1|100|
|n (normalization)|2|between 0 and 1|
|number of epochs|3|10|
|dropout rate|4|50%|
|log-rank p values (Wilcoxon test)|5|<0.01|

# IO Domain

## Input Subdomain
  

|Filename|URI|Access Time|SHA Checksum|
| :---: | :---: | :---: | :---: |
|Summary of 32 TCGA cancer types|https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8281595/bin/13073_2021_930_MOESM2_ESM.xlsx|N/A|N/A|

## Output Subdomain
  

|Media type|Filename|URI|Access Time|SHA Checksum|
| :---: | :---: | :---: | :---: | :---: |
|xlsx|DeepProg performances when using a number of models ranging from 1 to 30. The Cox-PH log-rank p value (pval) and the C-index (CI) are calculated for two datasets: HCC and BRCA. Two validation datasets are used for HCC: LIRI and GSE, and four datasets for BRCA, named Anna, Patiwan, Miller, and Metabric datasets respectively.|https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8281595/bin/13073_2021_930_MOESM1_ESM.xlsx|Tuesday 27, February 2024|N/A|
|xlsx|Cox-PH log-rank p value, Silhouette score, and clustering stability score obtained using DeepProg on the 32 cancers and with a number of input clusters from 2 to 5.|https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8281595/bin/13073_2021_930_MOESM3_ESM.xlsx|Tuesday 27, February 2024|N/A|

# Execution Domain
  
Script Driver: Python3
## Scripts:
  

|Filename|URI|Access Time|
| :---: | :---: | :---: |
|DeepProg|https://github.com/lanagarmire/DeepProg|N/A|

## Environment Variables

## Software Prerequisites
  

|Name|Version|URI|Access Time|SHA Checksum|
| :---: | :---: | :---: | :---: | :---: |
|scikit-optimize|0.8.1|https://scikit-optimize.github.io/stable/|Tuesday 27, February 2024||
|Ray tune|2.9.3|https://docs.ray.io/en/latest/tune.html|Tuesday 27, February 2024||
|python package lifelines|0.28.0|https://github.com/CamDavidsonPilon/lifelines|Tuesday 27, February 2024||

## External Data Endpoints
  

|Name|URL|
| :---: | :---: |

# Error Domain

# Provenance
  
Version: 2.0  
License: https://creativecommons.org/licenses/by/4.0/  
Created: 2024-02-23T19:22:52  
Modified: 2024-04-02T19:09:33  

### Contributors
  

|Name|Contribution|Affiliation|Email|ORCID|
| :---: | :---: | :---: | :---: | :---: |
|Chinweoke Okonkwo|curatedBy|George Washington University|s.okonkwo@email.gwu.edu||
|Olivier B. Poirien|authoredBy|1Current address: Computational Sciences, The Jackson Laboratory, 10 Discovery Drive Farmington, Farmington, Connecticut 06032 USA  2University of Hawaii Cancer Center, Honolulu, HI 96813 USA|||
|Zheng Jing|authoredBy|Department of Computational Medicine and Bioinformatics, University of Michigan|||
|Kumardeep Chaudhary|authoredBy|2University of Hawaii Cancer Center, Honolulu, HI 96813 USA  4Current address: Department of Genetics and Genomic Sciences, Icahn School of Medicine at Mount Sinai|||
|Sijia Huang|authoredBy|2University of Hawaii Cancer Center, Honolulu, HI 96813 USA  5Current address: Department of Biostatistics, Epidemiology and Informatics, University of Pennsylvania, Philadelphia|||
|Lana X. Garmire|authoredBy|2University of Hawaii Cancer Center, Honolulu, HI 96813 USA  3Current address: Department of Computational Medicine and Bioinformatics, University of Michigan|||
  

### Review
  

|Name|Contribution|Affiliation|Email|ORCID|Status|Comments|Date|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
