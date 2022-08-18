################################################################################
#                                  LOCAL SYSTEM                                #
################################################################################

### Operating System Version
### MacBook Pro
# ROOT_loc = "/Users/swvanderlaan"
# STORAGE_loc = "/Users/swvanderlaan"
# CLOUD_loc = "/Users/swvanderlaan/Library/Mobile Documents/com~apple~CloudDocs/"
# ONEDRIVE_loc = "/Users/swvanderlaan/Library/CloudStorage/OneDrive-UMCUtrecht/Genomics"

### MacBook Air
ROOT_loc = "/Users/slaan3"
STORAGE_loc = "/Users/slaan3"
CLOUD_loc = "/Users/slaan3/Library/Mobile Documents/com~apple~CloudDocs/"
ONEDRIVE_loc = "/Users/slaan3/Library/CloudStorage/OneDrive-UMCUtrecht/Genomics"

# STORAGE_loc = "/Volumes/LaCie"

### Generic 
LAB_loc = paste0(CLOUD_loc, "/Genomics/LabBusiness")

AEDB_loc = paste0(ONEDRIVE_loc, "/Athero-Express/AE-AAA_GS_DBs")

### Genetic and genomic data
PLINK_loc=paste0(STORAGE_loc,"/PLINK")
GWAS_loc=paste0(PLINK_loc,"/_GWAS_Datasets/_CHARGE_CAC")

# genetic
AEGSQC_loc =  paste0(PLINK_loc, "/_AE_ORIGINALS/AEGS_COMBINED_QC2018")
MICHIMP_loc=paste0(PLINK_loc,"/_AE_ORIGINALS/AEGS_COMBINED_EAGLE2_1000Gp3v5HRCr11")

# sc rna
AESCRNA_loc = paste0(PLINK_loc, "/_AE_ORIGINALS/AESCRNA/prepped_data")

# bulk rna
AERNA_loc = paste0(PLINK_loc, "/_AE_ORIGINALS/AERNA")

### Project
# PROJECT_loc = paste0(PLINK_loc, "/analyses/grants/telomeregrant2022")
PROJECT_loc = paste0(STORAGE_loc, "/git/CirculatoryHealth/EntropyMasker")

# # use this if there is relevant information here.
# ifelse(!dir.exists(file.path(PROJECT_loc, "/targets")), 
#        dir.create(file.path(PROJECT_loc, "/targets")), 
#        FALSE)
# TARGET_loc = paste0(PROJECT_loc,"/targets")

### SOME VARIABLES WE NEED DOWN THE LINE
TRAIT_OF_INTEREST = "EntropyMasker" # Phenotype
PROJECTNAME = "EntropyMasker"

cat("\nCreate a new analysis directories.\n")

cat("\n- general directory\n")
ifelse(!dir.exists(file.path(PROJECT_loc)), 
       dir.create(file.path(PROJECT_loc)), 
       FALSE)
ANALYSIS_loc = paste0(PROJECT_loc)

cat("\n- for plots\n")
ifelse(!dir.exists(file.path(ANALYSIS_loc, "/ae_plots")), 
       dir.create(file.path(ANALYSIS_loc, "/ae_plots")), 
       FALSE)
PLOT_loc = paste0(ANALYSIS_loc,"/ae_plots")

ifelse(!dir.exists(file.path(PLOT_loc, "/qc")), 
       dir.create(file.path(PLOT_loc, "/qc")), 
       FALSE)
QC_loc = paste0(PLOT_loc,"/qc")

cat("\n- for output of summary results\n")
ifelse(!dir.exists(file.path(ANALYSIS_loc, "/ae_output")), 
       dir.create(file.path(ANALYSIS_loc, "/ae_output")), 
       FALSE)
OUT_loc = paste0(ANALYSIS_loc, "/ae_output")

cat("\n- for baseline tables\n")
ifelse(!dir.exists(file.path(ANALYSIS_loc, "/ae_baseline")), 
       dir.create(file.path(ANALYSIS_loc, "/ae_baseline")), 
       FALSE)
BASELINE_loc = paste0(ANALYSIS_loc, "/ae_baseline")

# cat("\n- for genetic analyses\n")
# ifelse(!dir.exists(file.path(ANALYSIS_loc, "/SNP")), 
#        dir.create(file.path(ANALYSIS_loc, "/SNP")), 
#        FALSE)
# SNP_loc = paste0(ANALYSIS_loc, "/SNP")

# cat("\n- for Cox regression results\n")
# ifelse(!dir.exists(file.path(PLOT_loc, "/COX")), 
#        dir.create(file.path(PLOT_loc, "/COX")), 
#        FALSE)
# COX_loc = paste0(PLOT_loc, "/COX")


setwd(paste0(PROJECT_loc))
getwd()
list.files()