from gtts import gTTS as gtts
import simpleaudio as sa
import subprocess
import os
import sys

temp = './temp/'

print('Google TTS version 1.0 by ReekyStive')
print('Type ":quit" to quit, type ":proxy" to set proxy.')
print('Type anything to start.')

while (True):
    s = input('> ')
    if s.strip() == ':quit':
        break
    elif s.strip() == ':proxy':
        server = input('HTTP Proxy server: ')
        os.environ['http_proxy'] = server
        os.environ['https_proxy'] = server
        print('Proxy is set.\n')
        continue

    print('Generating...', end='')
    sys.stdout.flush()
    try:
        os.remove(temp + 'speech.mp3')
    except:
        pass
    try:
        tts = gtts(s)
        tts.save(temp + 'speech.mp3')
    except AssertionError:
        print(' Nothing to generate.\n')
        continue
    except:
        print(' Failed.')
        print('Please check your connection with Google.')
        print('Enter ":proxy" to set proxy.\n')
        continue

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
