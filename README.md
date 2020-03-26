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


Cell 16


create variable 'model' using Sequential() from tensorflow.keras.models

Add a Long short term memory layer (LSTM) into our model and add 100 neurons into the model.

We will use the ReLU activation function for the model as well.

To form a single output from the 100 neurons, we will use model.add(Dense(1)) to get our final output.

To minimize our loss function, we will use the adam optimization technique

Since our model is a continous variable, we will use the mean squared error (mse) as our loss function.


Cell 17


Summary of our model


Cell 18


Create an early stop mechanism so the model does not take hours to generate if the model is not making any improvements on the loss function


Cell 19


since our train set is a generator object, we need to make our test set a generator object so we will make a generator object for our validation set


Cell 20


Fit our model into the TSG

Add more epochs than necessary to ensure that the model works until the early stop is activated when no imporvements are being made in the function.


Cell 21


create a dataframe for the model history to maintain a record of how our model formed


Cell 22


Visualize our loss function on our validation set (val_loss)

Visualize our loss function on our training set (loss)


Cell 23


For loop for evaluating our test data

first_eval_batch uses the last 12 points in the set to predict the 13th point to build a forecast model

reshape first batch to our length and number of features

repeat steps for each interation of length using a for loop and append value to our current prediction (current_pred) variable.

This for loop will give us the scaled version of our predictions.


Cell 24


Inverse scaler transformation of our predictions


Cell 25


Add column [Predictions] to our test dataframe


Cell 26


Visualize our test dataframe with our predicted model along with test model


Cell 27


Visualize our Predcited model vs the test data in a graph


Cell 28-35


Repeat Cell 9-19 with our test data. In cell 9-19 we built the model using training data. Now that we see our model working well based on our predictions for our test data, we can repeat the same model for our test data to predict into the future prices of our adjusted close values.


Cell 36


Visualize entire dataframe of chosed ticker historical data from 1-31-00 to 02-29-20


Cell 37


Create new dataframe range 'forecast_index' and chose the starting point of the data


Cell 38


Create new dataframe for our forecasted data


Cell 39


Visualize our forecast dataframe


Cell 40


Visualize historical data


Cell 41


Visualize forecasted model


Cell 42


Visualize forecasted model overlayed with historical data


Cell 43


Visualize forecasted model overlayed with historical data with an x limit

















