from gtts import gTTS as gtts
import simpleaudio as sa
import subprocess
import os
import sys

temp = './temp/'
langs_help = """
| Local accent              | Language code | Top-level domain |
| ------------------------- | ------------- | ---------------- |
| English (Australia)       | en            | com.au           |
| English (United Kingdom)  | en            | co.uk            |
| English (United States)   | en            | com              |
| English (Canada)          | en            | ca               |
| English (India)           | en            | co.in            |
| English (Ireland)         | en            | ie               |
| English (South Africa)    | en            | co.za            |
| French (Canada)           | fr            | ca               |
| French (France)           | fr            | fr               |
| Mandarin (China Mainland) | zh-CN         | any              |
| Mandarin (Taiwan)         | zh-TW         | any              |
| Portuguese (Brazil)       | pt            | com.br           |
| Portuguese (Portugal)     | pt            | pt               |
| Spanish (Mexico)          | es            | com.mx           |
| Spanish (Spain)           | es            | es               |
| Spanish (United States)   | es            | com              |
"""

print('Google TTS version 1.1 by ReekyStive')
print('Type ":quit" to quit, type ":help" for help.')
print('Type anything to start.')

lang = 'en'
tld = 'com'

while (True):
    s = input('> ')
    if s.strip() == ':quit':
        break
    elif s.strip() == ':proxy':
        server = input('HTTP proxy server: ')
        os.environ['http_proxy'] = server
        os.environ['https_proxy'] = server
        print('Proxy is set.\n')
        continue
    elif s.strip() == ':help':
        print(':quit  - quit')
        print(':help  - show help')
        print(':proxy - set proxy')
        print(':lang  - set language and local accent')
        print(':langs - show all languages and local accents')
        print()
        continue
    elif s.strip() == ':lang':
        lang = input('Language code(default: en): ')
        if lang.strip() == '':
            lang = 'en'
        tld = input('Top-level domain(default: com): ')
        if tld.strip() == '':
            tld = 'com'
        print('Language and local accent is set.')
        print()
        continue
    elif s.strip() == ':langs':
        print(langs_help)
        continue

    print('Generating...', end='')
    sys.stdout.flush()
    try:
        os.remove(temp + 'speech.mp3')
    except:
        pass
    try:
        tts = gtts(s, lang=lang, tld=tld)
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
