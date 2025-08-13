import requests
import json
from datetime import datetime

class ISSTracker:
    def __init__(self):
        self.api_url = "http://api.open-notify.org/iss-now.json"
        
    def get_current_position(self):
        """Get current ISS position"""
        try:
            response = requests.get(self.api_url)
            data = response.json()
            
            position = {
                'latitude': float(data['iss_position']['latitude']),
                'longitude': float(data['iss_position']['longitude']),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            return position
        except Exception as e:
            return f"Error: {e}"
    
    def get_human_readable_location(self, lat, lon):
        """Convert coordinates to human-readable location"""
        # Using a simple approach - you can enhance this
        if lat > 0:
            lat_dir = "N"
        else:
            lat_dir = "S"
            
        if lon > 0:
            lon_dir = "E"  
        else:
            lon_dir = "W"
            
        return f"{abs(lat):.2f}°{lat_dir}, {abs(lon):.2f}°{lon_dir}"
    
    def track_and_display(self):
        """Main tracking function"""
        position = self.get_current_position()
        if isinstance(position, dict):
            location = self.get_human_readable_location(
                position['latitude'], 
                position['longitude']
            )
            
            print(f"🛰️ ISS Current Location: {location}")
            print(f"📅 Time: {position['timestamp']}")
            print(f"🌍 Exact Coordinates: {position['latitude']}, {position['longitude']}")
            
            return position
        else:
            print(position)
            return None

if __name__ == "__main__":
    tracker = ISSTracker()
    tracker.track_and_display()
