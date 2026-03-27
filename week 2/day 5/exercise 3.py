#chart implementation
import matplotlib.pyplot as plt
from pyowm import OWM
from datetime import datetime
import pytz

# --- Configuration ---
API_KEY = 'your_openweathermap_api_key_here' # Replace with your API Key
owm = OWM(API_KEY)
mgr = owm.weather_manager()
city_name = "Paris,FR"

def init_plot():
    """Sets the labels and title for the chart."""
    plt.ylabel('Humidity (%)')
    plt.title(f'3-Day Humidity Forecast for {city_name}')
    plt.xlabel('Date & Time (UTC)')

def plot_temperatures(times, humidities):
    """Creates the bar chart using time and humidity data."""
    # Note: Using bar chart for humidity as requested
    bars = plt.bar(times, humidities, color='skyblue', edgecolor='navy', width=0.08)
    plt.xticks(rotation=45, ha='right')
    return bars

def write_humidity_on_bar_chart(bars):
    """Annotates each bar with its specific humidity percentage."""
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 1,
                 f'{int(height)}%', ha='center', va='bottom', fontsize=8)

def main():
    # 1. Retrieve 5-day forecast (3h intervals)
    forecast = mgr.forecast_at_place(city_name, '3h').forecast
    
    # 2. Extract data for the first 24 slots (approx 3 days)
    times = []
    humidities = []
    
    for weather in forecast.get_weathers()[:24]:
        # Convert GMT timestamp to readable string using pytz
        dt = datetime.fromtimestamp(weather.ref_time, tz=pytz.UTC)
        times.append(dt.strftime('%m/%d %H:%M'))
        humidities.append(weather.humidity)

    # 3. Build the GUI
    plt.figure(figsize=(12, 6))
    init_plot()
    bars = plot_temperatures(times, humidities)
    write_humidity_on_bar_chart(bars)
    
    # Styling & Display
    plt.tight_layout()
    plt.ylim(0, 110) # Humidity is 0-100%
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    main()
    
#working with city IDS
reg = owm.city_id_registry()
list_of_locations = reg.ids_for('Paris', country='FR')
paris_id = list_of_locations[0][0] # Returns the integer ID