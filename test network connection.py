#This script is used to test the network connection
import requests


# try to check whether we have any connection to the internet
try:
    response = requests.get("https://www.google.com", timeout=10)
    print(f"Google Status Code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Connection Error: {e}")

# try to check whether we have any connection to the skype server
url = "https://client-s.gateway.messenger.live.com/v1/users/ME/endpoints"
try:
    response = requests.get(url, timeout=10)
    print(f"Status Code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Connection Error: {e}")