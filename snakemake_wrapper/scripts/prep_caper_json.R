if (exists("snakemake")) {
  logFile <- file(snakemake@log[[1]])

  sink(logFile, append = TRUE)
  sink(logFile, append = TRUE, type = 'message')
}

library(rjson)

### DATA
caper_dir <- snakemake@params$caper_dir
chip_title <- snakemake@params$chip_title
chip_description <- snakemake@params$chip_description
chip_genome_tsv <- snakemake@params$chip_genome_tsv
chip_pipeline_type <- snakemake@params$chip_pipeline_type
aligner <- snakemake@params$aligner
duplication_marker <- snakemake@params$duplication_marker
control_reads_are_paired <- snakemake@params$control_reads_are_paired
always_use_pooled_ctl <- snakemake@params$always_use_pooled_ctl
control_rep1_R1 <- snakemake@params$control_rep1_R1
control_rep2_R1 <- snakemake@params$control_rep2_R1
exp_reads_are_paired <- snakemake@params$exp_reads_are_paired
exp_rep1_R1 <- snakemake@params$exp_rep1_R1
exp_rep2_R1 <- snakemake@params$exp_rep2_R1

setwd(caper_dir)

json_list <- list(chip.pipeline_type = chip_pipeline_type, chip.genome_tsv = chip_genome_tsv, chip.fastqs_rep1_R1 = list(exp_rep1_R1), chip.fastqs_rep2_R1 = list(exp_rep2_R1), chip.ctl_fastqs_rep1_R1 = list(control_rep1_R1), chip.ctl_fastqs_rep2_R1 = list(control_rep2_R1), chip.paired_end = exp_reads_are_paired, chip.title = chip_title, chip.description = chip_description)

jsonData <- toJSON(json_list, indent = 2, method = "C")


write(jsonData, "peakpuller.json")
