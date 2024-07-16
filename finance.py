
# Import the modules
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Download historical data for Microsoft for the past 6 years
mft = yf.Ticker('MSFT')
df = mft.history(period="8y")

# Print the historical data
print(type(df))

#plotting the close uVing the index
df.plot.line(y = 'Close', use_index = True)

# Remove columns not needed
#del df['Dividends']
#del df['Stock Splits']

# create a column which shifts all close prices forword by a day
df['Tomorrow'] = df['Close'].shift(-1)

# Create a new column called target for predicting direction of prices
df['Target'] = (df['Tomorrow'] > df['Close']).astype(int)

print(df)
# Creating the initial ML model
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(min_samples_split=100, n_estimators = 100, random_state=7)

#split the data
df = df.copy()
train = df.iloc[:-100]
test = df.iloc[-100:]

# Create redictors
predictors = ["Close", "Volume", "Open", "High", "Low"]

model.fit(train[predictors], train["Target"])

#import the precision to check model performance
from sklearn.metrics import precision_score

preds = model.predict(test[predictors])

preds = pd.Series(preds, index = test.index)
print(preds)

precision_score(test["Target"], preds)

def model_predict(train, test, predictors, model):
    model.fit(train[predictors], train["Target"])
    preds = model.predict(test[predictors])
    preds = pd.Series(preds, index = test.index, name = "Predictions")
    combined = pd.concat([test["Target"], preds], axis = 1)
    return combined


def backtest(data, model, predictors, start = 750, step = 75):
    all_predictions = []
    
    for i in range(start, data.shape[0], step):
        train = data.iloc[0:i].copy()
        test = data.iloc[i:(i+step)].copy()
        predictions = model_predict(train, test, predictors, model)
        all_predictions.append(predictions)
    return pd.concat(predictions)

predictions = backtest(df, model, predictors)

print(predictions)

precision_score(predictions["Target"], predictions["Predictions"])