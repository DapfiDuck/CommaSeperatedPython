# Comma Seperated Python

[GitHub Pages](http://davidkowalk.github.io/CommaSeperatedPython).

CommaSeperatedPython is a lightweight python library to help with handling data from csv files.
This project aims at being an easy to use api for a very limited set of applications. It functions as a wrapper for the python-native csv function that handles the file for you.

## Functions
The csv-handler can perform different functions regarding loading data from files. [Documentation](https://davidkowalk.github.io/CommaSeperatedPython/docs/functions)

## Similar Resources
1. [Pandas](https://github.com/pandas-dev/pandas) is a powerful python library for data analysis. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis / manipulation tool available in any language. It is already well on its way towards this goal.

2. [Numpy](https://github.com/numpy/numpy) is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. It's mainly used for complicated matrix calculations.

## Example
In the folder ``src/exampledata/`` you can find data about the search relevance of python since 2004. Let's say you'd like to plot these with matplotlib.

You can install matplotlib via pypip:
```
pip install matplotlib
```

First we import our libraries:
```python
from matplotlib import pyplot as plt
import csvloader as csv
```

Next we need to load the data from the file
```python
sheet = csv.load_sheet("path/python_googletrends.csv")
dates = csv.get_collumn_of_sheet(sheet, 0)[1:-1]
data = csv.get_collumn_of_sheet(sheet, 1)[1:-1]
```

Since the data is loaded as strings while matplotlib expects floats or integers, we need to convert the data into a float-list.

```python
data = csv.float_list(data)
```

Now we can call matplotlib to plot the data:
```python
plt.plot(dates, data)
plt.xlabel("Dates")
plt.ylabel("Search Relevance")

plt.show()
```

This will plot the data over time.
