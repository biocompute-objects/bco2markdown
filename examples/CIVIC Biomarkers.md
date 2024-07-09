



# CIVIC Biomarkers
  
Object ID: https://biocomputeobject.org/BCO_000494/0.1  
Spec Version: https://w3id.org/ieee/ieee-2791-schema/2791object.json  
etag: 0bd768e2788ee7114c34005231b0e56ff8348c3e3161b761050e609564b3d865
# Usability
  
For this data set, we pulled biomarker data from CIVIC. From the raw TSV, the data was cleaned and extracted. Data that was pulled were the biomarkers, assessed biomarker entity, specimen, and condition for the biomarker. Condition ID, specimen ID, and assessed biomarker entity ID were mapped from relevant external resources to the table. The data was then reprocessed and cleaned to be mapped into the new biomarker data model that was set by the Biomarker Partnership. Temporary ID's were assigned based on the core fields (assessed_biomarker_entity_id, assessed_biomarker_entity, biomarker, and condition). The primary use case for this data set is to see information on human cancer biomarkers.
# Description

## Keywords
  
Cancer, CIVIC, Biomarker
## External References

# IO Domain

## Input Subdomain
  

|Filename|URI|Access Time|SHA Checksum|
| :---: | :---: | :---: | :---: |
|civic.tsv|https://github.com/biomarker-ontology/biomarker-partnership/blob/data_conversion/data/results/tables/civic.tsv|Thursday 09, May 2024|N/A|

## Output Subdomain
  

|Media type|Filename|URI|Access Time|SHA Checksum|
| :---: | :---: | :---: | :---: | :---: |
|text/tsv|transformed_civic.tsv|https://github.com/biomarker-ontology/biomarker-partnership/blob/data_conversion/data/results/tables/transformed_civic.tsv|Thursday 09, May 2024|N/A|

# Execution Domain
  
Script Driver: Python Script
## Scripts:
  

|Filename|URI|Access Time|
| :---: | :---: | :---: |
|civic.ipynb|https://github.com/biomarker-ontology/biomarker-partnership/blob/data_conversion/src/civic.ipynb|Thursday 09, May 2024|

## Environment Variables
  
EDITOR: JUPYTER NOTEBOOK
## Software Prerequisites
  

|Name|Version|URI|Access Time|SHA Checksum|
| :---: | :---: | :---: | :---: | :---: |
|Python|3.19|https://www.python.org/ftp/python/3.10.0/|Thursday 09, May 2024|N/A|

## External Data Endpoints
  

|Name|URL|
| :---: | :---: |
|GitHub.com/Biomarker-Partnership|https://github.com/clinical-biomarkers|

# Error Domain

## empirical_error
  
empirical_error: null
## algorithmic_error
  
algorithmic_error: null
# Provenance
  
Version: 0.1  
License: https://spdx.org/licenses/CC-BY-4.0.html  
Created: 2024-05-09T16:31:41  
Modified: 2024-05-30T18:51:28.821Z  

### Contributors
  

|Name|Contribution|Affiliation|Email|ORCID|
| :---: | :---: | :---: | :---: | :---: |
|Vania Ballesteros Prieto|authoredBy, contributedBy, createdBy, curatedBy|George Washington University|vania.ballesterosprieto@gwmail.gwu.edu|N/A|
|Daniall Masood|createdWith, contributedBy|George Washinton University|daniallmasood@gwu.edu|N/A|
|Kate Warner|createdBy|The George Washington University|k.warner1@gwu.edu|N/A|
  

### Review
