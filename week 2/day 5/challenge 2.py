#the implementation
import requests
import time

class WebMonitor:
    def __init__(self):
        self.results = {}

    def measure_load_time(self, url):
        """Measures how long it takes to get a full response from a URL."""
        # Ensure the URL starts with http to avoid errors
        if not url.startswith('http'):
            url = f"https://{url}"
            
        try:
            # Start the timer
            start_time = time.time()
            
            # Perform the GET request
            response = requests.get(url, timeout=10)
            
            # End the timer
            end_time = time.time()
            
            # Calculate duration
            duration = end_time - start_time
            
            # Store and return result
            self.results[url] = round(duration, 4)
            return self.results[url]
            
        except requests.exceptions.RequestException as e:
            return f"Error connecting to {url}: {e}"

# --- Testing the code ---
monitor = WebMonitor()
sites = ["google.com", "ynet.co.il", "imdb.com", "github.com"]

print(f"{'Website':<20} | {'Load Time (s)':<15}")
print("-" * 40)

for site in sites:
    load_time = monitor.measure_load_time(site)
    print(f"{site:<20} | {load_time:<15}")