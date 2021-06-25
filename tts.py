from gtts import gTTS as gtts
import simpleaudio as sa
import subprocess
import os
import sys

temp = './temp/'


while (True):
    s = input('> ')

    print('Generating...', end='')
    sys.stdout.flush()
    try:
        os.remove(temp + 'speech.mp3')
    except:
        pass
    tts = gtts(s)
    tts.save(temp + 'speech.mp3')

    print(' Decoding...', end='')
    sys.stdout.flush()
    try:
        os.remove(temp + 'speech.wav')
    except:
        pass
    subprocess.run(['ffmpeg', '-i', temp + 'speech.mp3', temp + 'speech.wav'],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(' Playing...', end='')
    sys.stdout.flush()
    wave = sa.WaveObject.from_wave_file(temp + 'speech.wav')
    wave.play()

    print('\n')
