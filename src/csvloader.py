#MIT License
#
#Copyright (c) 2019 David J. Kowalk
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import csv
from typing import List


def load_sheet(url: str, delimiter: str = ","):
    with open(url) as file:
        sheet = csv.reader(file, delimiter=delimiter)
        array = []

        for row in sheet:
            array.append(row)

    return array


def load_column(url, column_nr: int, delimiter: str=","):
    array = load_sheet(url, delimiter=delimiter)
    column = get_column_of_sheet(array, column_nr)

    return column


def get_column_of_sheet(sheet, column_nr: int):
    column: List = []

    for row in sheet:
        column.append(row[column])

    return column


def float_list(to_float: List) -> List[float]:
    outlist: List[float] = []

    for entry in to_float:
        outlist.append(float(entry))

    return outlist
