import requests
import matplotlib.pyplot as plt

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

        if step == 'days':
            for day in data_js['days']:

                result['datetime'].append(day['datetime'])
            
                for element in elements:
                    if element in day:
                       result[element].append(day[element])
                    else:
                        result[element].append(None)

        elif step == 'hours':
            for hour in data_js['days'][0]['hours']:
                result['datetime'].append(hour['datetime'])
                
                for element in elements:
                    if element in hour:
                        result[element].append(hour[element])
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
start_date = '2025-05-03'
end_date = '2025-05-03'

weather_data = api_client.get_values(location, start_date, end_date, step='hours')

plov = WeatherPlot()
plov.plot(weather_data, title=f'Weather in Kyiv at {start_date}', ylabel='Values')
