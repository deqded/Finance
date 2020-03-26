# Finance

Explanation of the Predictive model

Cell 1

Imports

Cell 2

Create dataframe 'df' with data retrieved from 'Get 20 yrs of S&P 500 data and combine data into 1 csv file.py'.
Set df['Date'] as index

Cell 3

Identify what ticker we are going to be predicting for.
List of all tickers- https://en.wikipedia.org/wiki/List_of_S%26P_500_companies excluding BRK.B and BF.B
The ticker is the symbol in the wiki table
Resample df into monthly data.

Cell 4

Create variable test_size
For test size keep integer less than 24 months to make sure the training data is at least 70% of hystorical data

Cell 5

Create variable test_ind
test_ind seperates our training data and testing data

Cell 6

Create variable 'train' and 'test' using the df we created in cell 2 and slice data into train set and test set using the variable 'test_ind'

Cell 7

Visualize df slice 'train'

Cell 8

Visualize df slice 'test'

Cell 9

Cell 10

