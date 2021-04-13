from sklearn.preprocessing import MinMaxScaler
from tensorflow.python.keras.layers import Dense, LSTM
from tensorflow.python.keras import Sequential
import math
import numpy as np


class LSTMModel:
    def trainData(self, df, epochs):
        # Create a new data frame
        data = df.filter(['Close'])
        # convert data frame to numpy array
        dataset = data.values
        # get number of rows to train the model on
        training_data_len = math.ceil(len(dataset) * .8)
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(dataset)
        # Create the training dataset
        # Create teh scaled training data set
        train_data = scaled_data[0:training_data_len, :]
        # split the data into x_train and y_train data sets
        x_train = []
        y_train = []
        for i in range(60, len(train_data)):
            x_train.append(train_data[i - 60:i, 0])
            y_train.append(train_data[i, 0])
        # Convert the x_train and y_train to numpy arrays
        x_train, y_train = np.array(x_train), np.array(y_train)
        # Reshape the data
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        # Build the LSTM Model
        model = Sequential()
        model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
        model.add(LSTM(50, return_sequences=False))
        model.add(Dense(25))
        model.add(Dense(1))
        # Compile the model
        model.compile(optimizer='adam', loss='mean_squared_error')
        # Train the model
        model.fit(x_train, y_train, epochs=epochs)
        test_data = scaled_data[training_data_len - 60:, :]
        # Create teh data sets x_test and y_test
        x_test = []
        # actual test values
        y_test = dataset[training_data_len:, :]
        for i in range(60, len(test_data)):
            x_test.append(test_data[i - 60:i, 0])
            # convert the data to a numpy array
        x_test = np.array(x_test)
        # Reshape the Data
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        # get the models predicted price values
        predictions = model.predict(x_test)
        predictions = scaler.inverse_transform(predictions)
        valid = data[training_data_len:]
        valid['Predictions'] = predictions
        return valid

