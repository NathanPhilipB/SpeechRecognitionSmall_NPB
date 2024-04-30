import speech_recognition as sr
import requests 
import pyttsx3

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("Please wait...")
    with m as source: 
        r.adjust_for_ambient_noise(source)
    #print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: 
            audio = r.listen(source)
        print("Trying to recognize it...")

    #using PocketSphinx, not very great recognition
        #try:
        #    spoken_text = r.recognize_sphinx(audio)
        #    print("Tadbot thinks you said: " + spoken_text)
        #except sr.UnknownValueError:
        #    print("Tadbot could not understand audio")
        #except sr.RequestError as e:
        #    print(f"Could not request results from Sphinx; {e}")

        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            question = r.recognize_google(audio)
            print("Tadbot thinks you said: " + question)
        except sr.UnknownValueError:
            print("Tadbot could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        try:
            url = 'http://laptop_ip_adress:5000/xxxxxx'
            response = requests.post(url, json={'question': question})

            if response.status_code == 200:
            # Extract the JSON response
            # Extract the 'answer' string from the JSON response
                answer = response.json().get('answer', '')
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


except KeyboardInterrupt:
    pass


 