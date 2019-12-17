import csv


def load_sheet(url, delimiter=","):
    with open(url) as file:
        sheet = csv.reader(file, delimiter=delimiter)
        array = []

        for row in sheet:
            array.append(row)

    return array


def load_column(url, column_nr, delimiter=","):
    array = load_sheet(url, delimiter=delimiter)
    column = get_column_of_sheet(array, column_nr)

    return column


def get_column_of_sheet(sheet, column_nr):
    column = []

    for row in sheet:
        column.append(row[column])

    return column


def float_list(to_float):
    outlist = []

    for entry in to_float:
        outlist.append(float(entry))

    return outlist
