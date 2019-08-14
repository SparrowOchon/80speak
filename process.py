#!/usr/bin/env python3

import os
import json
import traceback
from pydub import AudioSegment

try:
    with open("requests.json", "r") as f:
        reqs = json.loads(f.read())

    print("PROCESSING REQUESTS...")

    for item in reqs:
        phrase = item["phrase"]
        phrase = '"This is a test of the 80speak python processor! It can run multiple jobs at once, and even output mp3!"'
        session = item["session"]
        print("----------------------------------------")
        print(f"SESSION: {session}")
        print(f"PHRASE: {phrase}")
        print("Converting to speech...")
        try:
            os.remove(f"/var/www/html/wav/{session}.wav")
        except:
            pass
        command = f"wine say.exe -w /var/www/html/wav/{session}.wav {phrase} &"
        print(command)
        os.system(command)
        print("----------------------------------------")
        # continue
        # print("Converting to mp3...")
        # sound = AudioSegment.from_file(f"/var/www/html/wav/{session}.wav", format="wav")
        # sound.export(f"/var/www/html/mp3/{session}.mp3", bitrate="32k", format="mp3")
        # print(f"Deleting original wav...")
        # os.remove(f"/var/www/html/wav/{session}.wav")
        # print("DONE!")
except:
    traceback.print_exc()
