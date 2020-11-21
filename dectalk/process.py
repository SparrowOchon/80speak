import pyaudio
import wave
import os
import subprocess
import speech_recognition as sr

# Setting parameters of the audio file
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

# p = pyaudio.PyAudio()

# # creating and opening the stream
# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)

# print("* recording")

# frames = []

# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)

# print("* done recording")

# # Stopping the stream
# stream.stop_stream()
# stream.close()
# p.terminate()

# print("Writing File...")

# # writing the file
# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()

print("Using recognizer...")

r = sr.Recognizer()

with sr.AudioFile(WAVE_OUTPUT_FILENAME) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)

print("Done")

subprocess.call("wine say.exe", shell=True)
subprocess.run([text, '\n'])
# print(text)
os.system(text)

#!/usr/bin/env python3

# import os
# import json
# import traceback
# from pydub import AudioSegment

# try:
#     with open("requests.json", "r") as f:
#         reqs = json.loads(f.read())

#     print("PROCESSING REQUESTS...")

#     for item in reqs:
#         phrase = item["phrase"]
#         phrase = '"This is a test of the 80speak python processor! It can run multiple jobs at once, and even output mp3!"'
#         session = item["session"]
#         print("----------------------------------------")
#         print(f"SESSION: {session}")
#         print(f"PHRASE: {phrase}")
#         print("Converting to speech...")
#         try:
#             os.remove(f"/var/www/html/wav/{session}.wav")
#         except:
#             pass
#         command = f"wine say.exe -w /var/www/html/wav/{session}.wav {phrase} &"
#         print(command)
#         os.system(command)
#         print("----------------------------------------")
#         # continue
#         # print("Converting to mp3...")
#         # sound = AudioSegment.from_file(f"/var/www/html/wav/{session}.wav", format="wav")
#         # sound.export(f"/var/www/html/mp3/{session}.mp3", bitrate="32k", format="mp3")
#         # print(f"Deleting original wav...")
#         # os.remove(f"/var/www/html/wav/{session}.wav")
#         # print("DONE!")
# except:
#     traceback.print_exc()
