from csv import reader

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """

    with open(csv_file_path, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        list_of_rows = []
    # Pass reader object to list() to get a list of lists
        for lsrows in csv_reader:
            for i in range(len(lsrows)):
                if lsrows[i][0] in '0123456789':
                    lsrows[i] = int(lsrows[i])
            list_of_rows.append(lsrows)

    return(list_of_rows)
