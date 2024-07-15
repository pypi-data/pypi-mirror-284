from Parse import parse_file
from matchingProgram import matching_process, build_hash_table, csv_writer
'''
script to execute matchingProgram used to paper querying
'''

results = []

#number of top candidates from k-mer matching to move on to levenhstein
#default = 5
levenshtein_candidates = 1


#parameter structure
#pip_command(file1, file2, k_value, written_file_name)

#----------------------------------------------------

'''
Have a levenshteinThreshold and ratioThreshold option.

Fro this to work take parameter name and set it equal in arguements.
'''
def fuzzy_match(k_value, file1,file1_key, file2, file2_key, levenshteinThreshold=.4, ratioThreshold=.85):
    mer_hash, paper_details = build_hash_table(k_value,file1, file1_key)

    callback = [lambda obj: results.append(matching_process(k_value, mer_hash,levenshtein_candidates, paper_details, obj,file2_key, levenshteinThreshold, ratioThreshold))]
    parse_file(file2,file2_key, callback)
    csv_writer(results)


fuzzy_match(3, 'C:/pipTheAdvisor/LargeScaleEntityMatchingForTheAdvisor/allPurposeTwoPhaseMatch/data.csv', 'name', 
            'C:/pipTheAdvisor/LargeScaleEntityMatchingForTheAdvisor/allPurposeTwoPhaseMatch/data2.csv', 'name')