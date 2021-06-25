# cli-tts

Thanks to [gTTS](https://github.com/pndurette/gTTS) by [@pndurette](https://github.com/pndurette)!

This is an interactive command line text-to-speech tool using Google TTS. Just type text and the voice will be played.

Multi-language is supported.

## Quick Start

### macOS

``` bash
$ git clone https://github.com/ReekyStive/cli-tts.git
$ cd cli-tts

$ brew install ffmpeg
# be sure ffmpeg is in PATH
$ pip install -r requirements.txt

$ python tts.py
```

### Windows

There's a package that already included everything:
[Win32 Release](https://github.com/ReekyStive/cli-tts/releases/download/v1.1/google-tts-win32.7z)

## Screenshots

<img width="682" alt="Screen Shot 2021-06-25 at 22 35 50" src="https://user-images.githubusercontent.com/26853900/123440780-baaccf00-d605-11eb-8522-634bc6075f30.png">

## Supported Languages

| Local accent              | Language code | Top-level domain |
| ------------------------- | ------------- | ---------------- |
| English (Australia)       | `en`          | `com.au`         |
| English (United Kingdom)  | `en`          | `co.uk`          |
| English (United States)   | `en`          | `com`            |
| English (Canada)          | `en`          | `ca`             |
| English (India)           | `en`          | `co.in`          |
| English (Ireland)         | `en`          | `ie`             |
| English (South Africa)    | `en`          | `co.za`          |
| French (Canada)           | `fr`          | `ca`             |
| French (France)           | `fr`          | `fr`             |
| Mandarin (China Mainland) | `zh-CN`       | `<any>`          |
| Mandarin (Taiwan)         | `zh-TW`       | `<any>`          |
| Portuguese (Brazil)       | `pt`          | `com.br`         |
| Portuguese (Portugal)     | `pt`          | `pt`             |
| Spanish (Mexico)          | `es`          | `com.mx`         |
| Spanish (Spain)           | `es`          | `es`             |
| Spanish (United States)   | `es`          | `com`            |

## Requirements

- Python 3.x
- Pip packages
  - gTTS
  - simpleaudio
- ffmpeg (in PATH)
