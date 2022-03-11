import os
import snakemake
import cli.config

# get right directory, see https://stackoverflow.com/questions/4934806/how-can-i-find-scripts-directory-with-python
script_dir = os.path.dirname(os.path.realpath(__file__))
snakefile_location = os.path.join(script_dir,'..','snakemake_wrapper', 'Snakefile')
conda_prefix = os.path.abspath(os.path.join(script_dir, '..', 'snakemake_wrapper', 'conda'))

def config(dry_run, config_yaml, cluster_command, nodes, delete_all_output=False):

    print("[INFO] Invoking Snakemake with config {} and {} cores.".format(config_yaml, cores))

    finished_successfully = snakemake.snakemake(
        snakefile=snakefile_location,
        configfiles=[config_yaml],
        dryrun=dry_run,
        nodes=nodes,
        printshellcmds=True,
        delete_all_output=delete_all_output,
        use_conda=True,
        conda_prefix=conda_prefix,
        cluster=cluster_command
    )

    if not finished_successfully:
        os.sys.exit(os.EX_SOFTWARE)


def run_snakemake(dry_run, cores, cluster_command, nodes, output_dir):

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    yaml_config_file = os.path.join(output_dir, 'config.yaml')

    cli.config.create_config(cores, output_dir, yaml_config_file)

    config(dry_run, yaml_config_file, cores, cluster_command, nodes)


def delete_all_output(dry_run, config_yaml):

    run_snakemake_from_config(dry_run, config_yaml, 1, None, 1, True)
