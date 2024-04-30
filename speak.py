import requests
import pyttsx3

url = 'http://laptop_ip_address:5000/xxxxxxxx'

response = requests.get(url)

try:
    if response.status_code == 200:
        # Extract the JSON response
        response_json = response.json()
        # Extract the 'answer' string from the JSON response
        answer = response_json.get('answer', '')
        if answer:
            # Use TTS to read the 'answer' aloud
            engine = pyttsx3.init()
            engine.say(answer)
            engine.runAndWait()
        else:
            print("No 'answer' found in the JSON response.")
    else:
        print(f"Failed to get response from Flask server. Status code: {response.status_code}")

except requests.RequestException as e:
    print(f"Error: {e}")