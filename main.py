# =============================================================================
# Project:      HW2 - USING ARRAYS
# Student:      Michael Kim
# Class:        CSSSKL 123
# Section:      A, Spring 2024
#
#
# In this assignment, we are tasked with reading from a .py file and
# utilizing/manipulating the data within 4 separate lists to perform certain
# operations while use of f/w loop syntax is or is not restricted. Ultimately,
# the data values read in will be displayed and compared via visualizations.
#
# **Comments that specify each numbered task are in, "Main:", which begins
# after the import and methods sections below.**
# =============================================================================
import numpy
# --> Import module:

import numpy as np
import stocks #allows use of the .py file and its data


# --> Methods:

def percent_of_mean(one_d):
    '''
    As outlined in task #1, takes a 1-d list or array as an argument,
    transforms each of its values to a % of the mean of all values in
    the argument object.
    :param one_d: A one dimensional array or list
    :return: An array whose values correspond to the argument obj expressed in % of the mean
    '''
    as_array = numpy.asarray(one_d)  # cast the parameter arg as a numpy array
    error_fill = np.zeros(np.shape(one_d)) - 1  # sentinel value: -1
    mean_array = np.zeros(np.shape(one_d))  # create arrays that match the shape of input arg

    total = sum(one_d)
    count = len(one_d)
    mean = total / count  # calculate mean of all arg object elements

    # replace all entries (> 0) with their values expressed in % of the mean
    mean_array = np.where(as_array > 0, (as_array / mean) * 100, error_fill)
    print(mean_array)

    # mean_array = np.around(mean_array, decimals=2) #reassign new array to mean_array.
    # print(mean_array)
    return mean_array


# --> Main:

# -----------------------------------------------------------------------------
# Task #1:
# - Loops restricted / List comprehension structures restricted
# - Write 'percent_of_mean()'.
#   - Input is a 1-D array of numeric values.
#       - values represent the stock index for each day as a % of the
#           mean value over the period covered by the list
#   - Find mean of all values
#   - Store representation of each value as a % of the mean
# -----------------------------------------------------------------------------

# percent_of_mean(): completed in methods-> section (line 25)
nasdaq_pom = percent_of_mean(stocks.nasdaq)
sp500_pom = percent_of_mean(stocks.sp500)
djia_pom = percent_of_mean(stocks.djia)

# -----------------------------------------------------------------------------
# Task #2:
# - Plot all 3 converted lists
# - Write 'percent_of_mean()'.
#   - Input is a 1-D array of numeric values.
#       - values represent the stock index for each day as a % of the
#           mean value over the period covered by the list
#   - Find mean of all values
#   - Store representation of each value as a % of the mean
# -----------------------------------------------------------------------------

