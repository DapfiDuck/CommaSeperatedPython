# csvhandler

csvhandler is a lightweight library to help with handling data from csv files.

## Functions
The csv handler can perform different functions regarding loading data from files. [Documentation](./docs/functions)

## Example
In the folder ``src/exampledata/`` you can find data about the search relevance of python since 2004. Let's say you'd like to plot these with matplotlib.

You can install matplotlib via pypip:
```
pip install matplotlib
```

First we import our libraries:
```
from matplotlib import pyplot as plt
import csvloader as csv
```

Next we need to load the data from the file
```
sheet = csv.load_sheet("path/python_googletrends.csv")
dates = csv.get_collumn_of_sheet(sheet, 0)[1:-1]
data = csv.get_collumn_of_sheet(sheet, 1)[1:-1]
```

Since the data is loaded as strings while matplotlib expects floats or integers, we need to convert the data into a float-list.

```
data = csv.float_list(data)
```

Now we can call matplotlib to plot the data:
```
plt.plot(dates, data)
plt.xlabel("Dates")
plt.ylabel("Search Relevance")

plt.show()
```

This will plot the data over time.
