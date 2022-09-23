import pandas as pd
from csv import reader

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """

    with open(csv_file_path, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        
    return(list_of_rows)
