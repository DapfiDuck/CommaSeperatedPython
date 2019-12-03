import csv

def load_sheet(url, delimiter=","):
    with open(url) as file:
        sheet = csv.reader(file, delimiter=delimiter)
        array = []

        for row in sheet:
            array.append(row)

    return array;

def load_collumn(url, collumn_nr, delimiter=","):
    array = get_array(url, delimiter=delimiter)
    collumn = []

    for row in array:
        collumn.append(row[collumn_nr])

    return collumn

def get_collumn_of_sheet(sheet, collumn_nr):

    collumn = []

    for row in sheet:
        collumn.append(row[collumn_nr])

    return collumn

def float_list(list):
    outlist = []

    for entry in list:
        outlist.append(float(entry))

    return outlist
