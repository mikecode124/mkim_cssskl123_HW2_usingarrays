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
    As outlined in task #1, takes a 1-d list or array as an argument,
    transforms each of its values to a % of the mean of all values in
    the argument object.
    :param one_d: A one dimensional array or list
    :return: An array whose values correspond to the argument obj expressed in % of the mean
    '''
    as_array = np.asarray(one_d)  # cast the parameter arg as a numpy array
    error_fill = np.zeros(np.shape(one_d)) - 1  # sentinel value: -1
    mean_array = np.zeros(np.shape(one_d))  # create arrays that match the shape of input arg

    total = sum(one_d)
    count = len(one_d)
    mean = total / count  # calculate mean of all arg object elements

    # replace all entries (> 0) with their values expressed in % of the mean
    mean_array = np.where(as_array > 0, (as_array / mean) * 100, error_fill)
    #print(mean_array)

    # mean_array = np.around(mean_array, decimals=2) #reassign new array to mean_array
    # print(mean_array)
    return mean_array


def num_days_big_percent_chg(one_d, percent):
    as_array = np.asarray(one_d)
    change_arr = np.abs(as_array[:-1] - as_array[1:])
    perc_arr = (change_arr / as_array[:-1]) * 100
    bool_arr = perc_arr > percent
    ret_val = sum(bool_arr)

    return ret_val


def moving_average(one_d):
    as_array = np.asarray(one_d)
    #print(as_array)
    counter = 2

    ret_arr = np.zeros(as_array.shape[0] - 2)
    #print(len(ret_arr))

    while counter < len(as_array):
        #print("sum of as_array[0:3]" + str(sum(as_array[0:3])))
        temp_sum = sum(as_array[counter - 2:counter + 1])
        moving_3day = temp_sum / 3
        #print(moving_3day)
        ret_arr[counter - 2] = moving_3day
        counter += 1
        #print(counter)

    #print(ret_arr)
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

plt.figure(1)
plt.plot(np.arange(len(nasdaq_pom)), nasdaq_pom, label="NASDAQ")
plt.plot(np.arange(len(sp500_pom)), sp500_pom, label="S&P500")
plt.plot(np.arange(len(djia_pom)), djia_pom, label="DJIA")
plt.ylabel("Percent of Mean")
plt.xlabel("Trading Days Since Jun 1, 2016")
plt.title("Indices as Percent of Their Means")
plt.legend(loc="upper left")
#plt.show()

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

# num_days_big_percent_chg(): completed in --> Methods: section (line 50)
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

nasdaq_change = [num_days_big_percent_chg(stocks.nasdaq, 0.2),
                 num_days_big_percent_chg(stocks.nasdaq, 0.4),
                 num_days_big_percent_chg(stocks.nasdaq, 0.6),
                 num_days_big_percent_chg(stocks.nasdaq, 0.8),
                 num_days_big_percent_chg(stocks.nasdaq, 1)]

sp500_change = [num_days_big_percent_chg(stocks.sp500, 0.2),
                 num_days_big_percent_chg(stocks.sp500, 0.4),
                 num_days_big_percent_chg(stocks.sp500, 0.6),
                 num_days_big_percent_chg(stocks.sp500, 0.8),
                 num_days_big_percent_chg(stocks.sp500, 1)]

djia_change = [num_days_big_percent_chg(stocks.djia, 0.2),
                 num_days_big_percent_chg(stocks.djia, 0.4),
                 num_days_big_percent_chg(stocks.djia, 0.6),
                 num_days_big_percent_chg(stocks.djia, 0.8),
                 num_days_big_percent_chg(stocks.djia, 1)]

change_x = [0.2, 0.4, 0.6, 0.8, 1]

plt.figure(3)
plt.plot(change_x, nasdaq_change, label="NASDAQ")
plt.plot(change_x, sp500_change, label="S&P500")
plt.plot(change_x, djia_change, label="DJIA")
plt.ylabel("Number of Days")
plt.xlabel("Percentage Change Threshold Magnitude")
plt.title("Number of Days the Daily Percentage Change Exceeds a Threshold Magnitude")
plt.legend(loc="upper right")
#plt.show()

# -----------------------------------------------------------------------------
# Task #5:
# - Restricted to one (1) loop
# - Write 'moving_average()'
#   - Input is a 1-D array of numeric values
#   - Returns simple 3 day moving average
#       - Average each day with the 2 before it
#       - Return array will thus be 2 index less/shorter than input
# -----------------------------------------------------------------------------

# moving_average(): completed in --> Methods: section (line 50)
print(moving_average(stocks.nasdaq))

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
print(len(moving_average(stocks.nasdaq)))
plt.figure(4)
plt.plot(np.arange(len(moving_average(stocks.nasdaq))), moving_average(stocks.nasdaq), label="MA")
plt.plot(np.arange(len(stocks.nasdaq) - 2), stocks.nasdaq[2:], label="Non-MA")
plt.ylabel("Moving Average of Index")
plt.xlabel("Trading Days Since Jun 1, 2016")
plt.title("Three Day Moving Average of Nasdaq")
plt.legend(loc="upper left")

plt.figure(5)
plt.plot(np.arange(len(moving_average(stocks.sp500))), moving_average(stocks.sp500), label="MA")
plt.plot(np.arange(len(stocks.sp500) - 2), stocks.sp500[2:], label="Non-MA")
plt.ylabel("Moving Average of Index")
plt.xlabel("Trading Days Since Jun 1, 2016")
plt.title("Three Day Moving Average of S&P500")
plt.legend(loc="upper left")

plt.figure(6)
plt.plot(np.arange(len(moving_average(stocks.djia))), moving_average(stocks.djia), label="MA")
plt.plot(np.arange(len(stocks.djia) - 2), stocks.djia[2:], label="Non-MA")
plt.ylabel("Moving Average of Index")
plt.xlabel("Trading Days Since Jun 1, 2016")
plt.title("Three Day Moving Average of DJIA")
plt.legend(loc="upper left")

plt.show()

# ---End of File----
