# cli-tts

Command Line Text-To-Speech using Google TTS

This is an interactive command line text-to-speech tool. Just enter text and the voice will be played.

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

// TODO

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
