import random

def get_path_info(file_path):
	if file_path.find('/') < 0:
		folder = './'
		file_name_ending = file_path
	else:
		folder = file_path[:-file_path[::-1].find('/')]
		file_name_ending = file_path[-file_path[::-1].find('/'):]
	file_name = file_name_ending[:file_name_ending.find('.')]
	return folder, file_name_ending, file_name

def filter_50_50(data, seed=None):
	rev_loc = list(data['status'] == 1)
	rev_iloc = list(filter(lambda x: rev_loc[x], range(len(rev_loc))))
	rel_loc = list(data['status'] == 0)
	rel_iloc = list(filter(lambda x: rel_loc[x], range(len(rel_loc))))
	balance = min(len(rev_iloc), len(rel_iloc))
	if seed != None:
		random.seed(seed)
	rows = random.sample(rel_iloc, balance) + random.sample(rev_iloc, balance)
	return data.iloc[rows]

def get_help_text():
	return '''
seqQscorer - A machine learning application for quality assessment of NGS data

USAGE

	python seqQscorer.py [options]

DESCRIPTION

	The tool loads a pre-trained classification model to evaluate given
	feature sets describing the quality of sequencing data. For each given sample
	the model is applied to receive a probability of the sample to be of low quality. 
	Depending on the path provided by the user, the tool can be used on a single 
	sample or multiple samples contained in the given directory path(s).
	
	An example is provided in the git repository with a description in README. 
	Visit "https://github.com/salbrec/seqQscorer" to get more details.

OPTIONS
	
	--help		Print this help file and exit
	
	These options describe the experimental background of the data that is provided 
	by the user. This information is used to load the appropriate classification 
	model. When no information is provided for one ore more options, a more generalized 
	model is loaded.
	
	--spec		defines the species of the given data
			"human" or "mouse" are available
	
	--assay		defines the assay of the given data
			"ChIP-seq", "DNase-seq", and "RNA-seq" are available
	
	--rt		defines the run-type used in the given data
			"single-ended" or "paired-ended"
	
	These options specify the directories containing the statistics 
	or report summaries describing the data:
	
	--raw		path to the file or directory for the FastQC report(s)
	
	--map		path to the file or directory for the Bowtie2 mapping statistic(s)
	
	--loc		path to the file or directory for the location features (ChIPseeker)
	
	--tss		path to the file or directory for the TSS features (ChIPpeakAnno)
	
	Additional options:
	
	--out		path, that specifies a file for the output of the predictions
'''
