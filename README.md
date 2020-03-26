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


Create variable 'train' and 'test' using the df we created in cell 2 and slice data into train set and test set using the 

variable 'test_ind'


Cell 7


Visualize df slice 'train'


Cell 8


Visualize df slice 'test'


Cell 9


Create variable 'scaler' using MinMaxScaler which is imported from sklearn.preprocessing

Since recurrent neural networks feed information back into themselves, our data in the train set should be scaled. However, our data in the test set will not be scaled since we wont have data on future prices to scale.


Cell 10


scale train data


Cell 11


transform our train and test.

The Purpose is to standardize features by removing mean and scaling to unit variance


Cell 12


Create variable 'length' and set to 12 since we are using monthly data and a period is 12 months.

Create variable generator using TimeSeriesGenerator from tensorflow.keras.preprocessing.sequence

TSG generates batches for sequence data.

Our parameters for our TSG will be our scaled_train set which has both our x and y values since we have time stamped sequence information which we visualized in cell 7.

The way the generator works is based on the past (length - 1) data points, predict the next data point which in this case is the 12th.

Our batch_size is the number of timeseries samples in each batch which is going to be 1.


Cell 13 & 14


Visualize our generator on the 0th index of our TSG data


Cell 15


Number of features = 1 since we are only using hystorical data


Cell





