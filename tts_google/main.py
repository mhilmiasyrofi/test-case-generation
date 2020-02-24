# English
# 'en-us': 'English (US)'
# 'en-ca': 'English (Canada)'
# 'en-uk': 'English (UK)'
# 'en-gb': 'English (UK)'
# 'en-au': 'English (Australia)'
# 'en-gh': 'English (Ghana)'
# 'en-in': 'English (India)'
# 'en-ie': 'English (Ireland)'
# 'en-nz': 'English (New Zealand)'
# 'en-ng': 'English (Nigeria)'
# 'en-ph': 'English (Philippines)'
# 'en-za': 'English (South Africa)'
# 'en-tz': 'English (Tanzania)'
import os
from gtts import gTTS

file = open("alexa-test-command.txt")
lines = file.readlines()

mp3_folder = "tts_google/mp3_generated_speech/"
wav_folder = "tts_google/generated_speech/"

if not os.path.exists(mp3_folder):
    os.makedirs(mp3_folder)

if not os.path.exists(wav_folder):
    os.makedirs(wav_folder)
    
i = 0
for line in lines:
    i = i + 1
    tts = gTTS(line, lang='en-ph')
    outfile = mp3_folder + "audio_%02d.mp3" % i
    wavfile = wav_folder + "audio_%02d.wav" % i
    tts.save(outfile)
    os.system('ffmpeg -i /Users/mhilmiasyrofi/Documents/test-case-generation/' + outfile +
              ' -acodec pcm_s16le -ac 1 -ar 16000 /Users/mhilmiasyrofi/Documents/test-case-generation/' + wavfile + ' -y')
    print("Generated audio_%02d.wav" % i)