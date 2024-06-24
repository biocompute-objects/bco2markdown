



# HCV1a ledipasvir resistance SNP detection
  
Object ID: https://biocomputeobject.org/BCO_000001/1.5  
Spec Version: https://w3id.org/ieee/ieee-2791-schema/2791object.json  
etag: 06c56ccdeeea2e805dd909302d5ab05d3e31c8e16fed17a27510cb00f53cc59e
# Usability
  
Identify baseline single nucleotide polymorphisms (SNPs)[SO:0000694], (insertions)[SO:0000667], and (deletions)[SO:0000045] that correlate with reduced (ledipasvir)[pubchem.compound:67505836] antiviral drug efficacy in (Hepatitis C virus subtype 1)[taxonomy:31646]
# Description

## Keywords
  
HCV1a, Ledipasvir, antiviral resistance, SNP, amino acid substitutions
## External References
  

|Name|Namespace|Access Time|IDs|
| :---: | :---: | :---: | :---: |
|PubChem-compound|pubchem.compound|Friday 31, January 2020|67505836|
|PubMed|pubmed|Wednesday 01, January 2020|26508693|
|Sequence Ontology|so|Wednesday 01, January 2020|SO:000002, SO:0000694, SO:0000667, SO:0000045|
|Taxonomy|taxonomy|Wednesday 01, January 2020|31646|

## Platform
  
HIVE
## Pipeline Steps
  
***Step 1: HIVE-hexagon***  
Version: 1.3  
Description: Alignment of reads to a set of references  
**Prerequisites**  

|Name|uri|Access time|
| :---: | :---: | :---: |
|Hepatitis C virus genotype 1|http://www.ncbi.nlm.nih.gov/nuccore/22129792|Tuesday 24, January 2017|
|Hepatitis C virus type 1b complete genome|http://www.ncbi.nlm.nih.gov/nuccore/5420376|Tuesday 24, January 2017|
|Hepatitis C virus (isolate JFH-1) genomic RNA|http://www.ncbi.nlm.nih.gov/nuccore/13122261|Tuesday 24, January 2017|
|Hepatitis C virus clone J8CF, complete genome|http://www.ncbi.nlm.nih.gov/nuccore/386646758|Tuesday 24, January 2017|
|Hepatitis C virus S52 polyprotein gene|http://www.ncbi.nlm.nih.gov/nuccore/295311559|Tuesday 24, January 2017|
  
**Input List**  

|Name|uri|Access Time|
| :---: | :---: | :---: |
|N/A|http://example.com/dna.cgi?cmd=objFile&ids=514683|Tuesday 24, January 2017|
|N/A|http://example.com/dna.cgi?cmd=objFile&ids=514682|Tuesday 24, January 2017|
  
**Output List**  

|Name|uri|Access Time|
| :---: | :---: | :---: |
|N/A|http://example.com/data/514769/allCount-aligned.csv|Tuesday 24, January 2017|
  
***Step 2: HIVE-heptagon***  
Version: 1.3  
Description: variant calling  
**Input List**  

|Name|uri|Access Time|
| :---: | :---: | :---: |
|N/A|http://example.com/data/514769/dnaAccessionBased.csv|Tuesday 24, January 2017|
  
**Output List**  

|Name|uri|Access Time|
| :---: | :---: | :---: |
|N/A|http://example.com/data/514801/SNPProfile.csv|Tuesday 24, January 2017|
|N/A|http://example.com/data/14769/allCount-aligned.csv|Tuesday 24, January 2017|

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
|Hepatitis C virus genotype 1|http://www.ncbi.nlm.nih.gov/nuccore/22129792|Tuesday 24, January 2017|N/A|
|Hepatitis C virus type 1b complete genome|http://www.ncbi.nlm.nih.gov/nuccore/5420376|Tuesday 24, January 2017|N/A|
|Hepatitis C virus (isolate JFH-1) genomic RNA|http://www.ncbi.nlm.nih.gov/nuccore/13122261|Tuesday 24, January 2017|N/A|
|N/A|http://www.ncbi.nlm.nih.gov/nuccore/386646758|Tuesday 24, January 2017|N/A|
|Hepatitis C virus S52 polyprotein gene|http://www.ncbi.nlm.nih.gov/nuccore/295311559|Tuesday 24, January 2017|N/A|
|HCV1a_drug_resistant_sample0001-01|http://example.com/nuc-read/514682|Tuesday 24, January 2017|N/A|
|HCV1a_drug_resistant_sample0001-02|http://example.com/nuc-read/514683|Tuesday 24, January 2017|N/A|

## Output Subdomain
  

|Media type|Filename|URI|Access Time|SHA Checksum|
| :---: | :---: | :---: | :---: | :---: |
|text/csv|N/A|http://example.com/data/514769/dnaAccessionBased.csv|Tuesday 24, January 2017|N/A|
|text/csv|N/A|http://example.com/data/514801/SNPProfile*.csv|Tuesday 24, January 2017|N/A|

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
|HIVE-hexagon|babajanian.1|http://example.com/dna.cgi?cmd=dna-hexagon&cmdMode=-|Tuesday 24, January 2017|d60f506cddac09e9e816531e7905ca1ca6641e3c|
|HIVE-heptagon|albinoni.2|http://example.com/dna.cgi?cmd=dna-heptagon&cmdMode=-|Tuesday 24, January 2017|N/A|

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
# Provenance
  
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
|Hadley Kinga|['createdBy']|George Washington University|hadley_king@gwmail.gwu.edu|N/A|approved|Approved by GW staff. Waiting for approval from FDA Reviewer|Tuesday 21, April 2020|
