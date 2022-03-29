# This is a walkthrough file for how to setup and run ChIP-seq from the ENCODE project pipelines created by Jake Lehle.
# Start off by setting up everything inside of an anaconda env.
# If you have never used anaconda, I highly reccomend it for the ease and reproducibility of pipeline setup on various different system arachtecures. 
# Here are the steps to install and setup anaconda for the first time. Skip ahead if you have already done this.

# Lets set up an new enviornment called encode

conda create --name encode
conda activate encode

# The pipeline is run using the cromwell software package which is called natively caper.
# To install caper just use pip. (make sure the version is >= 2.1

pip install caper
caper --version

# Now you have to iniate the cromewell so it can configure itself. I'm going to do this with a loacl configuration.
# The cromwell config file lives in the ~/.caper/deafult.conf consider making a backup of this file for safekeeping.

caper init local
cp ~/.caper/default.conf ~/.caper/default.conf.bak
 
# Okay now lets set up the pipeline. Cromwell uses the caper command which takes a .wdl config file and runs the samples trhough contanierized processing steps. If you are runnning this in a HPC you have to use singularity when running this pipeline so that's what I'll be covering here but personally I like running docker on my own system where I have full environment control. 

# Knowing this look for the .wdl file and take a peak at the different items it contains.
# The .wdl file we are given as an example is the chip.wdl and it lays out everything we will need to run the piepline and even gives urls to get the singularity containers which is important so you don't even have to have it set up locally. (This saves us some serious time).

# Next we need the input sample json file which conatins information about what aligner and peak caller we will be using. The example we will be using is found in /example_input_json/ENCSR936XTK_subsampled_chr19_only.json which uses bowtie2 as the aligner (blah) and mac2 as the peakcaller (ehh). I wanna replace those both with GEM in the future thst has shown to be much better. But whatever, you are learning so you don't need to worry about this. I'm just thinking out loud.

#If you look in the template.json it has a /path_to_genome/hg38 we need to download the hg38 genome and index genome before we can run the pipeline. Modify this line to say genome/hg38/hg38.tsv
# Then make the dir so we can download the files there.

mkdir -p genome/hg38

# Now go to the scripts dir and use the download_genome_data.sh to get those files you will need

./download_genome_data.sh hg38 ../genome/hg38/

# Lets run the pipeline with all this information.

caper run chip.wdl -i example_input_json/ENCSR936XTK_subsampled_chr19_only.json --singularity  

#/////////////////////////////////////////////////////////////////////////////////
# Peakpuller ChiP-seq Installation and Walkthrough
# This is the setup giud for the peakpuller pipeline.
# Fist let's start off my setting up a new Anaconda environment to set up the peakpuller software in.

conda create -n peakpuller

# Next let's pull the peakpuller repository from GitHub 

git clone https://github.com/JakeLehle/peakpuller.git
cd peakpuller

# Finally let's set up the command line interface and test the installation of the peakpuller software

python3 setup.py. install
peakpuller --help

# If the command outputs the usage and documnetation for peakpuller, congrats the software is installed and ready to go. Let's start testing everything out by running some sample data.
# The pipeline is set up to always be run from a YAML config file. So the first step in the pipeline is to generate a config file, then test the pipeline, and then modify the config file to inset your samples following the same format.
# So to generate the config file we will be using the create-config function in the peakpuller package.

peakpuller create-config --help

# Read over the documentation and decide on how many cores you would like to use as well as the name of the config file and the directory that you want all your results output into.

peakpuller create-config --cores-per-job 8 output new-config.yaml

# You will see that running this command generates the YAML config file in the current directory that has all of the information that you indicated as well as default settings for sample data to be run.   
