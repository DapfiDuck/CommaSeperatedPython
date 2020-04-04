# Documentation

**Contents**
1. [Importing CSV Handler into your project.](#importing-csv-handler-into-your-project)
2. [Functions](#functions)
  - [load_sheet()](#load_sheet)
  - [load_collumn()](#load_collumn)
  - [get_collumn_of_sheet()](#get_collumn_of_sheet)
  - [float_list()](#float_list)

## Importing CSV-Handler into your project
To import CommaSeperatedPython into your project you can clone the project from [github](http://github.com/DapfiDuck/csvhandler) and put the ``csvloader.py`` into your project. Now import the library into your python project with:
```python
import csvloader as csv
```
Now you can use all functions of CSP inside your project. If the handler is imported like this functions must be called with ``csv.functionname()`` They can also be imported individually

## Functions
### load_sheet()
Returns contents of the csv as a 2-Dimensional array of strings.

|Parameters|Description|Required|
|----------|-----------|--------|
|url       |Path to the file|y|
|delimiter |Delimiter between values|n|

Usage:
```python
from csvloader import load_sheet
sheet = load_sheet("./example_data/example.csv")
print(sheet)
```

### load_collumn()
Loads and returns a collumn of the csv-file as a 1-Dimensional list of Strings.

|Parameters|Description|Required|
|----------|-----------|--------|
|url       |String Path to the file|y|
|collumn_nr|Index of the collumn to be loaded starting at 0|y|
|delimiter |Delimiter between values|n|

Usage:
```python
from csvloader import load_collumn
col = load_collumn("./example_data/example.csv", 1)
print(col)
```

### get_collumn_of_sheet()
Returns a specific collumn of a preloaded array as a 1 dimensional list.


|Parameters|Description|Required|
|----------|-----------|--------|
|sheet     |2D Array   |y|
|collumn_nr|Index of the collumn to be loaded starting at 0|y|

Usage:
```python
from csvloader import get_collumn_of_sheet as get_col
data = [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25]]

x = get_col(data, 0)
y = get_col(data, 1)

print(x)
print(y)
```

### float_list()
Converts every entry in a list to float.

|Parameters|Description|Required|
|----------|-----------|--------|
|list|List of datapoints as strings|y|

Usage:
```python
from csvloader import float_list
data = ["1", "4", "9", "16", "25"]
floatdata = float_list(data)
print(data)
print(floatdata)
```
