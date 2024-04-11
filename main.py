# =============================================================================
# Project:      HW2 - USING ARRAYS
# Student:      Michael Kim
# Class:        CSSSKL 123
# Section:      A, Spring 2024
#
#
# In this assignment, we are tasked with reading from a .py file and
# utilizing/manipulating the data within 3 separate lists to perform certain
# operations while use of f/w loop syntax is mostly restricted. Ultimately,
# the data will be displayed and compared via visualizations.
#
# **Comments that specify each numbered task are in, "--> Main:", which begins
# after the Import and Methods sections below**
# =============================================================================

# --> Import module:

import numpy as np
import stocks #allows use of the .py file and its data
import matplotlib.pyplot as plt

# --> Methods:

def percent_of_mean(one_d):
    '''
    From task #1, takes a 1-d list or array as an argument,
    transforms each of its values to a % of the mean of all values in
    the argument object.
    :param one_d: A one dimensional array or list
    :return: An array whose values correspond to the argument obj expressed in %
    of the mean
    '''
    as_array = np.asarray(one_d)  # cast the parameter arg as a numpy array
    error_fill = np.zeros(np.shape(one_d)) - 1  # sentinel value: -1
    mean_array = np.zeros(np.shape(one_d))  # match the shape of input arg

    total = sum(one_d)
    count = len(one_d)
    mean = total / count  # calculate mean of all arg object elements

    # replace all entries (> 0) with their values expressed in % of the mean
    mean_array = np.where(as_array > 0, (as_array / mean) * 100, error_fill)

    return mean_array


def num_days_big_percent_chg(one_d, percent):
    '''
    From task #3, takes a 1-d list or array and a % value
    as an arguments. Finds the change from each day to day represented
    in %. Returns the total # of days that the change % exceeded the
    input percent value.
    :param one_d: A one dimensional array or list
    :param percent: Comparison % value
    :return: Number of days change exceeded % comparison value
    '''
    as_array = np.asarray(one_d)  # convert input to array
    # find the absolute difference between each day
    change_arr = np.abs(as_array[:-1] - as_array[1:])
    # represent difference value as %
    perc_arr = (change_arr / as_array[:-1]) * 100
    # create copy array filled with boolean T if > than input %
    bool_arr = perc_arr > percent
    # store sum of days that change % exceeds input %
    ret_val = sum(bool_arr)

    return ret_val


def moving_average(one_d):
    '''
    From task #5, takes a 1-d list or array as an argument. Calculates
    the average of each day with the 2 before it for a moving 3 day average.
    Returns an array with the 3 day moving averages. 2 index shorter than input.
    :param one_d: A one dimensional array or list
    :return: An array whose values represents the average of each day with the
    2 before it
    '''
    as_array = np.asarray(one_d)
    counter = 2  # counter starts @ 2 to allow 2 prev index (days) for 3 day avg
    # return array also 2 index less
    ret_arr = np.zeros(as_array.shape[0] - 2)

    # increment counter, break when counter == to length of input one_d
    while counter < len(as_array):
        # store each 3 day interval
        temp_sum = sum(as_array[counter - 2:counter + 1])
        # store average of each 3 day interval
        moving_3day = temp_sum / 3
        # assign average to corresponding return array position
        ret_arr[counter - 2] = moving_3day
        # increment counter with each loop
        counter += 1

    return ret_arr

# --> Main:

# -----------------------------------------------------------------------------
# Task #1:
# - Loops restricted / List comprehension structures restricted
# - Write 'percent_of_mean()'
#   - Input is a 1-D array of numeric values
#       - values represent the stock index for each day as a % of the
#         mean value over the period covered by the list
#   - Find mean of all values
#   - Store representation of each value as a % of the mean
# -----------------------------------------------------------------------------

# percent_of_mean(): completed in --> Methods: section (line 25)
print("\npercent_of_mean(nasdaq[3]): " +
      str(percent_of_mean(stocks.nasdaq)[3]) + "\n")  # should print 98.67...

# store method returns into separate variables
nasdaq_pom = percent_of_mean(stocks.nasdaq)
sp500_pom = percent_of_mean(stocks.sp500)
djia_pom = percent_of_mean(stocks.djia)

# -----------------------------------------------------------------------------
# Task #2:
# - Plot all 3 converted lists
#   - on the same graph
# - y-axis is: "Percent of Mean"
# - x-axis is: "Trading Days Since Jun 1, 2016"
# - Add legend item for each converted list
# - Title is: "Indices as Percent of Their Means"
# -----------------------------------------------------------------------------

# plot all 3 stock index representions on 1 graph, figure(1)
plt.figure(1)
# used stored method return from task 1
plt.plot(np.arange(len(nasdaq_pom)), nasdaq_pom, label="NASDAQ")
plt.plot(np.arange(len(sp500_pom)), sp500_pom, label="S&P500")
plt.plot(np.arange(len(djia_pom)), djia_pom, label="DJIA")
plt.ylabel("Percent of Mean")
plt.xlabel("Trading Days Since Jun 1, 2016")
plt.title("Indices as Percent of Their Means")
plt.legend(loc="upper left")

# -----------------------------------------------------------------------------
# Task #3:
# - Loops restricted / List comprehension structures restricted
# - Write 'num_days_big_percent_chg()'
#   - two parameters:
#       - 1-D array values of a stock index
#       - a percentage value
#   - returns a number of days
#       - represents # of days the stock value change from the previous day
#         exceeded the input %
#       - both + and - change amount count as being larger than the %
# -----------------------------------------------------------------------------

# num_days_big_percent_chg(): completed in --> Methods: section (line 48)
print("num_days_big_percent_chg(nasdaq, 4%): " +
      str(num_days_big_percent_chg(stocks.nasdaq, 4)))  # should print: 1

# -----------------------------------------------------------------------------
# Task #4:
# - Calculate the % change from day to day for each stock index
#   - Use 'num_days_big_percent_chg()'
#   - Track the following:
#       - # of days change exceeds 0.2%
#       - # of days change exceeds 0.4%
#       - ... exceeds 0.6%
#       - ... exceeds 0.8%
#       - ... exceeds 1.0%
#   - Plot each stock's representation
#       - # of days vs % threshold values
#       - label axis, title, and make legend
# -----------------------------------------------------------------------------

# make lists for total # of days which correspond to thresholds
nasdaq_change = [num_days_big_percent_chg(stocks.nasdaq, 0.2),
                 num_days_big_percent_chg(stocks.nasdaq, 0.4),
                 num_days_big_percent_chg(stocks.nasdaq, 0.6),
                 num_days_big_percent_chg(stocks.nasdaq, 0.8),
                 num_days_big_percent_chg(stocks.nasdaq, 1)]

# "" line 168
sp500_change = [num_days_big_percent_chg(stocks.sp500, 0.2),
                 num_days_big_percent_chg(stocks.sp500, 0.4),
                 num_days_big_percent_chg(stocks.sp500, 0.6),
                 num_days_big_percent_chg(stocks.sp500, 0.8),
                 num_days_big_percent_chg(stocks.sp500, 1)]

# "" line 168
djia_change = [num_days_big_percent_chg(stocks.djia, 0.2),
                 num_days_big_percent_chg(stocks.djia, 0.4),
                 num_days_big_percent_chg(stocks.djia, 0.6),
                 num_days_big_percent_chg(stocks.djia, 0.8),
                 num_days_big_percent_chg(stocks.djia, 1)]

# create threshold values, correspond index total to above 3 lists
change_x = [0.2, 0.4, 0.6, 0.8, 1]

# plot all on one graph, figure(2)
plt.figure(2)
plt.plot(change_x, nasdaq_change, label="NASDAQ")
plt.plot(change_x, sp500_change, label="S&P500")
plt.plot(change_x, djia_change, label="DJIA")
plt.ylabel("Number of Days")
plt.xlabel("Percentage Change Threshold Magnitude")
plt.title("Number of Days the Daily Percentage Change Exceeds a Threshold Magnitude")
plt.legend(loc="upper right")

# -----------------------------------------------------------------------------
# Task #5:
# - Restricted to one (1) loop
# - Write 'moving_average()'
#   - Input is a 1-D array of numeric values
#   - Returns simple 3 day moving average
#       - Average each day with the 2 before it
#       - Return array will thus be 2 index less/shorter than input
# -----------------------------------------------------------------------------

# moving_average(): completed in --> Methods: section (line 71)
print("\nmoving_average(nasdaq[0]]): "
      + str(moving_average(stocks.nasdaq)[0]))  # should print 4955.37...

# -----------------------------------------------------------------------------
# Task #6:
#   - Plot each stock's representation separately (3 separate figures)
#       - Two plots per graph
#           - 3 day moving average (MA)
#           - Market value on the same day (Non-MA) (no average or anything)
#       - Y-axis: "Moving Average of Index"
#       - X-axis: "Trading Days Since Jun 1, 2016"
#       - Title: "Three Day Moving Average of {stock index name}"
#       - Legend: MA, Non-MA
# -----------------------------------------------------------------------------

# plot 3 seperate graphs, figure(3-5)
plt.figure(3)
plt.plot(np.arange(len(moving_average(stocks.nasdaq))), moving_average(stocks.nasdaq), label="MA")
plt.plot(np.arange(len(stocks.nasdaq) - 2), stocks.nasdaq[2:], label="Non-MA")
plt.ylabel("Moving Average of Index")
plt.xlabel("Trading Days Since Jun 1, 2016")
plt.title("Three Day Moving Average of Nasdaq")
plt.legend(loc="upper left")

plt.figure(4)
plt.plot(np.arange(len(moving_average(stocks.sp500))), moving_average(stocks.sp500), label="MA")
plt.plot(np.arange(len(stocks.sp500) - 2), stocks.sp500[2:], label="Non-MA")
plt.ylabel("Moving Average of Index")
plt.xlabel("Trading Days Since Jun 1, 2016")
plt.title("Three Day Moving Average of S&P500")
plt.legend(loc="upper left")

plt.figure(5)
plt.plot(np.arange(len(moving_average(stocks.djia))), moving_average(stocks.djia), label="MA")
plt.plot(np.arange(len(stocks.djia) - 2), stocks.djia[2:], label="Non-MA")
plt.ylabel("Moving Average of Index")
plt.xlabel("Trading Days Since Jun 1, 2016")
plt.title("Three Day Moving Average of DJIA")
plt.legend(loc="upper left")

# show all graphs from all relevant tasks simultaneously
plt.show()

# ---End of File----
