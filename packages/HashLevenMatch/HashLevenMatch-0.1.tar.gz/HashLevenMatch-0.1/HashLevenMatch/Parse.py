import xml.etree.ElementTree as ET
import csv
from Kmer import mer_builder


class MyObject:
    def __init__(self, **kwargs):
        self.id = 0
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __repr__(self):
        return str(self.__dict__)


'''
@brief: Used to parse through CSV file.

@author: Davis Spradling
'''

'''
Used to parse through files.

@param: file_name - File that is being parsed.

@param: callback - Methods you want to be executed every time a paper is parsed.

@param: file_associated_attributes - Attributes that will be associated at the end of output when done for file being parsed.

'''

def parse_file(file_name, file_key, callback, file_associated_attributes=None):

    # Ensure file_associated_attributes is a list
    if file_associated_attributes is None:
        file_associated_attributes = []
        
    # Add file_key to file_associated_attributes
    file_associated_attributes.append(file_key)
    i = 0

    with open(file_name, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            obj_data = {attr: row[attr] for attr in file_associated_attributes if attr in row}
            obj = MyObject(**obj_data)
            i+=1
            obj.id = i 
            for fnction in callback:
                fnction(obj)


k = 3

file1_key = "name"
dblp_callbacks = [lambda obj: mer_builder(obj, file1_key, k, False, False)]
parse_file("C:/pipTheAdvisor/LargeScaleEntityMatchingForTheAdvisor/allPurposeTwoPhaseMatch/data.csv", file1_key, dblp_callbacks, ["phone"])
