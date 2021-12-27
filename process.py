import speech_recognition as s_r
import subprocess
import os

# Main script to take the MIC input convert it to text and send it to Dectalk to say it. Missing ability to create a Virtual Mic to be played.


dectalks_path = "./HawkingSays/dectalk"

r = s_r.Recognizer()
my_mic = s_r.Microphone() #my device index is 1, you have to put your device index
with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source) #reduce noise
    audio = r.listen(source) #take voice input from the microphone

google_text = r.recognize_google(audio)

print(google_text) #to print voice into text
os.chdir(dectalks_path) # need to be in same dir for it to work
subprocess.run(['wine64', 'say.exe', google_text])