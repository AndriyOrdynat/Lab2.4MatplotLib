import requests
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

class Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    
    def get_Api(self, location, start_date, end_date, step='days'):
        
        url = f"{self.base_url}/{location}/{start_date}/{end_date}"
        
        params = {
            'key': self.api_key,
            'unitGroup': 'metric',
            'include': step,
            'contentType': 'json'
        }
        
        return requests.get(url, params=params).json()
    
    def get_values(self, location, start_date, end_date, step='days'):
        elements = ['temp', 'humidity', 'windspeed', 'cloudcover', 'tempmax', 'tempmin']
        data_js = self.get_Api(location, start_date, end_date, step)
        
        result = {element: [] for element in elements}
        result['datetime'] = []
        for day in data_js[step]:

            result['datetime'].append(day['datetime'])
            
            for element in elements:
                if element in day:
                    result[element].append(day[element])
                else:
                    result[element].append(None)
        
        return result

class WeatherPlot:
    def __init__(self, colors=['blue', 'green', 'red', 'orange', 'yellow', 'brown']):
        self.colors = colors
        self.current_color = 0
    
    def plot(self, data, title='Weather Data', xlabel='Date/Time', ylabel='Values'):
        for element in data:
            if element != 'datetime':
                plt.plot(data['datetime'], data[element], label=element, color=self.colors[self.current_color % len(self.colors)])
                self.current_color += 1
        
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

api_client = Client('XRWY5S7RPXQGZ7EA9HDPGWXHW')

location = "Kyiv,Ukraine"
start_date = '2025-05-01'
end_date = '2025-05-2'

weather_data = api_client.get_values(location, start_date, end_date, step='hours')

plov = WeatherPlot()
plov.plot(weather_data, title='Weather in Kyiv', ylabel='Values')

