import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

def generate_forecast(data, p, d, q):
    model = sm.tsa.ARIMA(data['Close'], order=(p, d, q))
    results = model.fit()

    # Forecast future prices
    forecast_steps = 30  # Number of steps to forecast into the future
    forecast = results.forecast(steps=forecast_steps)

    # Create a DataFrame to hold forecasted values
    forecast_dates = pd.date_range(start=data.index[-1], periods=forecast_steps + 1, closed='right')
    forecast_data = pd.DataFrame(forecast, index=forecast_dates, columns=['Forecast'])

    return forecast_data

def plot_forecast(data, forecast_data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Price', color='gray')
    plt.plot(forecast_data['Forecast'], label='Forecast', color='blue')

    plt.title('Price Forecast using ARIMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    # Load historical stock price data into a Pandas DataFrame
    # For this example, assume you have a CSV file named 'stock_data.csv' with columns ['Date', 'Close']
    data = pd.read_csv('stock_data.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    # Define the ARIMA model parameters (p, d, q)
    # p: order of the autoregressive part
    # d: degree of differencing
    # q: order of the moving average part
    p, d, q = 2, 1, 2

    # Generate the price forecast using ARIMA
    forecast_data = generate_forecast(data, p, d, q)

    # Plot the forecast
    plot_forecast(data, forecast_data)
