import pygame._sdl2 as sdl2
from pygame import mixer

# The following is used to find an appropriate output device and try playing directly through it.


try:
    mixer.init()
    # a list of alternative >OUTPUT< devices
    print(list(sdl2.get_audio_device_names()))

    # then....
    mixer.quit()
    mixer.init(devicename='<OUTPUT NAME>')
    mixer.music.load("test.ogg")
    mixer.music.play(-1)
    mixer.quit()
except Exception as e:
    print(e)