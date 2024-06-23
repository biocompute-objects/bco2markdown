


  
Object ID: https://biocomputeobject.org/BCO_000001/1.5  
Spec Version: https://w3id.org/ieee/ieee-2791-schema/2791object.json  
etag: 06c56ccdeeea2e805dd909302d5ab05d3e31c8e16fed17a27510cb00f53cc59e
# Provenance
  
Name: HCV1a ledipasvir resistance SNP detection  
Version: 1.5  
License: https://spdx.org/licenses/CC-BY-4.0.html  
Created: 2020-04-28T18:21:31.465Z  
Modified: 2021-09-08T13:42:22.111771  

### Contributors
  

|Name|Contribution|Affiliation|Email|ORCID|
| :---: | :---: | :---: | :---: | :---: |
|Charles Hadley King|createdBy, curatedBy|George Washington University|hadley_king@gwu.edu|https://orcid.org/0000-0003-1409-4549|
|Eric Donaldson|authoredBy|FDA|Eric.Donaldson@fda.hhs.gov|N/A|
  

### Review
  

|Name|Contribution|Affiliation|Email|ORCID|Status|Comments|Date|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Hadley Kinga|createdBy|George Washington University|hadley_king@gwmail.gwu.edu|N/A|approved|Approved by GW staff. Waiting for approval from FDA Reviewer|2020-04-21T14:17:21-0400|

# Usability
  
Identify baseline single nucleotide polymorphisms (SNPs)[SO:0000694], (insertions)[SO:0000667], and (deletions)[SO:0000045] that correlate with reduced (ledipasvir)[pubchem.compound:67505836] antiviral drug efficacy in (Hepatitis C virus subtype 1)[taxonomy:31646]
# Description

## Keywords
  
HCV1a, Ledipasvir, antiviral resistance, SNP, amino acid substitutions
## External References
  

|Name|Namespace|Access Time|IDs|
| :---: | :---: | :---: | :---: |
|PubChem-compound|pubchem.compound|2020-01-31T06:00:00.000Z|67505836|
|PubMed|pubmed|2020-01-01T07:00:00.000Z|26508693|
|Sequence Ontology|so|2020-01-01T06:00:00.000Z|SO:000002, SO:0000694, SO:0000667, SO:0000045|
|Taxonomy|taxonomy|2020-01-01T07:00:00.000Z|31646|

## Platform
  
HIVE
## Pipeline Steps
  
***Step 1: HIVE-hexagon***  
Version: 1.3  
Description: Alignment of reads to a set of references  
**Prerequisites**  

|Name|uri|Access time|
| :---: | :---: | :---: |
|Hepatitis C virus genotype 1|http://www.ncbi.nlm.nih.gov/nuccore/22129792|2017-01-24T09:40:17-0500|
|Hepatitis C virus type 1b complete genome|http://www.ncbi.nlm.nih.gov/nuccore/5420376|2017-01-24T09:40:17-0500|
|Hepatitis C virus (isolate JFH-1) genomic RNA|http://www.ncbi.nlm.nih.gov/nuccore/13122261|2017-01-24T09:40:17-0500|
|Hepatitis C virus clone J8CF, complete genome|http://www.ncbi.nlm.nih.gov/nuccore/386646758|2017-01-24T09:40:17-0500|
|Hepatitis C virus S52 polyprotein gene|http://www.ncbi.nlm.nih.gov/nuccore/295311559|2017-01-24T09:40:17-0500|
  
**Input List**  

|Name|uri|Access Time|
| :---: | :---: | :---: |
|N/A|http://example.com/dna.cgi?cmd=objFile&ids=514683|2017-01-24T09:40:17-0500|
|N/A|http://example.com/dna.cgi?cmd=objFile&ids=514682|2017-01-24T09:40:17-0500|
  
**Output List**  

|Name|uri|Access Time|
| :---: | :---: | :---: |
|N/A|http://example.com/data/514769/allCount-aligned.csv|2017-01-24T09:40:17-0500|
  
***Step 2: HIVE-heptagon***  
Version: 1.3  
Description: variant calling  
**Input List**  

|Name|uri|Access Time|
| :---: | :---: | :---: |
|N/A|http://example.com/data/514769/dnaAccessionBased.csv|2017-01-24T09:40:17-0500|
  
**Output List**  

|Name|uri|Access Time|
| :---: | :---: | :---: |
|N/A|http://example.com/data/514801/SNPProfile.csv|2017-01-24T09:40:17-0500|
|N/A|http://example.com/data/14769/allCount-aligned.csv|2017-01-24T09:40:17-0500|

# Parametric Domain
  

|Parameter|Step|Value|
| :---: | :---: | :---: |
|seed|1|14|
|minimum_match_len|1|66|
|divergence_threshold_percent|1|0.30|
|minimum_coverage|2|15|
|freq_cutoff|2|0.10|

# IO Domain

## Input Subdomain
  

|Filename|URI|Access Time|SHA Checksum|
| :---: | :---: | :---: | :---: |
|Hepatitis C virus genotype 1|http://www.ncbi.nlm.nih.gov/nuccore/22129792|2017-01-24T09:40:17-0500|N/A|
|Hepatitis C virus type 1b complete genome|http://www.ncbi.nlm.nih.gov/nuccore/5420376|2017-01-24T09:40:17-0500|N/A|
|Hepatitis C virus (isolate JFH-1) genomic RNA|http://www.ncbi.nlm.nih.gov/nuccore/13122261|2017-01-24T09:40:17-0500|N/A|
|N/A|http://www.ncbi.nlm.nih.gov/nuccore/386646758|2017-01-24T09:40:17-0500|N/A|
|Hepatitis C virus S52 polyprotein gene|http://www.ncbi.nlm.nih.gov/nuccore/295311559|2017-01-24T09:40:17-0500|N/A|
|HCV1a_drug_resistant_sample0001-01|http://example.com/nuc-read/514682|2017-01-24T09:40:17-0500|N/A|
|HCV1a_drug_resistant_sample0001-02|http://example.com/nuc-read/514683|2017-01-24T09:40:17-0500|N/A|

## Output Subdomain
  

|Media type|Filename|URI|Access Time|SHA Checksum|
| :---: | :---: | :---: | :---: | :---: |
|text/csv|N/A|http://example.com/data/514769/dnaAccessionBased.csv|2017-01-24T09:40:17-0500|N/A|
|text/csv|N/A|http://example.com/data/514801/SNPProfile*.csv|2017-01-24T09:40:17-0500|N/A|

# Execution Domain
  
Script Driver: shell
## Scripts:
  

|Filename|URI|Access Time|
| :---: | :---: | :---: |
|N/A|https://example.com/workflows/antiviral_resistance_detection_hive.py|N/A|

## Environment Variables
  
HOSTTYPE: x86_64-linux  
EDITOR: vim
## Software Prerequisites
  

|Name|Version|URI|Access Time|SHA Checksum|
| :---: | :---: | :---: | :---: | :---: |
|HIVE-hexagon|babajanian.1|http://example.com/dna.cgi?cmd=dna-hexagon&cmdMode=-|2017-01-24T09:40:17-0500|d60f506cddac09e9e816531e7905ca1ca6641e3c|
|HIVE-heptagon|albinoni.2|http://example.com/dna.cgi?cmd=dna-heptagon&cmdMode=-|2017-01-24T09:40:17-0500|N/A|

## External Data Endpoints
  

|Name|URL|
| :---: | :---: |
|HIVE|http://example.com/dna.cgi?cmd=login|
|access to e-utils|http://eutils.ncbi.nlm.nih.gov/entrez/eutils/|

# Error Domain

## empirical_error
  
false_negative_alignment_hits: <0.0010  
false_discovery: <0.05
## algorithmic_error
  
false_positive_mutation_calls_discovery: <0.00005  
false_discovery: 0.005