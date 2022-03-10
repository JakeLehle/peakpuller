import os
import requests
from ruamel.yaml import YAML

script_dir = os.path.dirname(os.path.realpath(__file__))

DEFAULT_OPTIONALS_FILE = os.path.join(script_dir, 'optionals.yaml')

yaml = YAML(typ='safe')
yaml.default_flow_style = False

def get_default_optional_parameters():

    with open(DEFAULT_OPTIONALS_FILE) as f:

        default_optionals = yaml.load(f)

        return default_optionals

def get_default_config(experiment_title, experiment_description, transcription_factor_or_histone_chip, aligner, duplication_marker, genome_tsv, experimental_reads_are_paired_end, control_reads_are_paired_end, always_use_pooled_ctl, experimental_rep_R1, experimental_rep_R2, control_rep_R1, control_rep_R2):

    mandatory_parameters = {
        'rawdir': os.path.abspath(fastq_dir),
        'output_dir': os.path.abspath(output_dir),
        'group1': group1,
        'group2': group2,
        'samples': group1 + group2,
        'ref': os.path.abspath(fasta_ref),
        'computing_threads': cores_per_job,
        'io_threads': cores_per_job
    }

    optional_parameters = get_default_optional_parameters()

    reference_annotation_files = get_reference_annotation_files(genome_build)

    methylseekr_calibration_chr = get_methylseekr_calibration_chromosome(genome_build)

    return {
        **mandatory_parameters
    }


def dump_config(config_dict, target_file):

    with (open(target_file, 'w')) as f:

        yaml.dump(config_dict, f)


def create_config(use_sample_files, genome_build, cores_per_job, fastq_dir, reference_fasta, group1, group2, output_dir, target_yaml):

    samples_in_group1 = group1.split(',')
    samples_in_group2 = group2.split(',')

    config_yaml = get_default_config(experiment_title, experiment_description, transcription_factor_or_histone_chip, aligner, duplication_marker, genome_tsv, experimental_reads_are_paired_end, control_reads_are_paired_end, always_use_pooled_ctl, experimental_rep_R1, experimental_rep_R2, control_rep_R1, control_rep_R2)

    dump_config(config_yaml, target_yaml)
