



# WGS Simulation of DUF1220 Regions
  
Object ID: https://biocomputeobject.org/BCO_067092/1.0  
Spec Version: https://w3id.org/ieee/ieee-2791-schema/2791object.json  
etag: 089dbf204912cba6454a320a578825f4996e3d08d2e908944bb1f76077d36011
# Usability
  
Pipeline for identifying copy number of genetic sequences independent of the genes in which they occur, and with higher fidelity than existing methods. Approximately 25 individuals were randomly chosen from each of the CEU, YRI, CHB, JPT, MXL, CLM, PUR, ASW, LWK, CHS, TSI, IBS, FIN, and BGR populations for a total of 324 individuals. Where domains were more than 1 kb apart, the boundaries of the domains were extended up to 250 bp to allow the possibility of capturing unique sequence directly adjacent to the domain. This example pipeline was created based on the work of Astling et al. doi: 10.1186/s12864-017-3976-z
# Description

## Keywords
  
Genome, Genomics, Simulation, Alignment, Alignment-Strategies, copy-number-variation, cnv, DUF1220, Genome informatics, Next-generation sequencing, Bioinformatics
## External References

# Parametric Domain
  

|Parameter|Step|Value|
| :---: | :---: | :---: |
|command line args|1|cutadapt -a XXX -A XXX -q 10 -minimum-length 80 -trim-n|
|command line arg|7|--very-sensitive|
|max insert size|7|800|

# IO Domain

## Input Subdomain
  

|Filename|URI|Access Time|SHA Checksum|
| :---: | :---: | :---: | :---: |
|N/A|ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/|N/A|N/A|

## Output Subdomain
  

|Media type|Filename|URI|Access Time|SHA Checksum|
| :---: | :---: | :---: | :---: | :---: |
|TEXT/CSS|N/A|http://example.com/data/514769/analyzed.csv|N/A|N/A|

# Execution Domain
  
Script Driver: shell
## Scripts:
  

|Filename|URI|Access Time|
| :---: | :---: | :---: |
|Linux CentOS 7|http://isoredirect.centos.org/centos/8/isos/x86_64/|N/A|

## Environment Variables
  
HOSTTYPE: x86_64-linux  
EDITOR: vim
## Software Prerequisites
  

|Name|Version|URI|Access Time|SHA Checksum|
| :---: | :---: | :---: | :---: | :---: |
|Bowtie2|2.2.5|http://bowtie-bio.sourceforge.net/bowtie2/index.shtml|Monday 12, August 2019|N/A|
|Bedtools|2.17.0|https://bedtools.readthedocs.io/en/latest/|Monday 12, August 2019|N/A|
|Samtools|0.1.19-44428cd|http://samtools.sourceforge.net/|Monday 12, August 2019|N/A|
|mrsFAST-Ultra|3.3.11|http://sfu-compbio.github.io/mrsfast/|Monday 12, August 2019|N/A|
|Bowtie1|1.1.2|http://bowtie-bio.sourceforge.net/index.shtml|Monday 12, August 2019|N/A|
|Perl module: Math::Random|0.72|https://cpan.metacpan.org/authors/id/G/GR/GROMMEL/Math-Random-0.72.tar.gz|Monday 12, August 2019|N/A|
|Perl module: Math::Complex|1.59|http://ftp.altlinux.org/pub/distributions/ALTLinux/Sisyphus/noarch/RPMS.classic//perl-Math-Complex-1.59-alt1.noarch.rpm|Monday 12, August 2019|N/A|

## External Data Endpoints
  

|Name|URL|
| :---: | :---: |
|access to e-utils|http://eutils.ncbi.nlm.nih.gov/entrez/eutils/|

# Provenance
  
Version: 1.0  
License: https://opensource.org/licenses/MIT  
Created: 2020-08-30T11:00:52.937Z  
Modified: 2021-09-08T14:13:34.350947  

### Contributors
  

|Name|Contribution|Affiliation|Email|ORCID|
| :---: | :---: | :---: | :---: | :---: |
|Mike Taylor|createdBy|GWU|mtaylor@example.edu|https://orcid.org/0000-0002-1003-5675|
|Josiah S. Carberry|curatedBy|GWU|jcarberry@example.edu|https://orcid.org/0000-0002-1825-0097|
|Jonathon Keeney|createdBy|Creator|keeneyjg@gwu.edu||
  

### Review
  

|Name|Contribution|Affiliation|Email|ORCID|Status|Comments|Date|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
