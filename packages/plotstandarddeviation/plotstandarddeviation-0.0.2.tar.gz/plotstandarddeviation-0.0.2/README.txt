Plot Standard Deviation is a library with currently one function:
To return all standard deviations from the mean within the range of the dataset.

This library contains one function:

getStandardDeviations(data)
This function takes a column of a pandas DataFrame and returns a list of all standard deviations from the mean within the dataset's range.

Note: If you want to plot lines using the given standard deviations, use a for loop to iterate over all the items in the function's returned list and use matplotlib.pyplot's axvline() for vertical or axline() for horizontal to plot the lines.