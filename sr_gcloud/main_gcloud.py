#!/usr/bin/env python3
import os
import glob

# obtain path to "english.wav" in the same folder as this script
from os import path
import uuid
import time
import base64
import hmac
import hashlib
import ssl
import certifi
import json

import speech_recognition as sr

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


class WaitTimeoutError(Exception):
    pass

class RequestError(Exception):
    pass

class UnknownValueError(Exception):
    pass


if __name__ == '__main__':

    translation_gcloud_writer = open("output/gcloud_translation.txt", "w+")

    r = sr.Recognizer()

    data = "data/"

    for (dirpath, _, filenames) in os.walk(data):
        if (len(filenames) > 0):
            if not os.path.exists(dirpath):
                os.makedirs(dirpath)
            for i in range(1, len(filenames)+1):
                filename = "audio_" + str(i) + ".wav"
                if (filename in filenames):
                    fpath = os.path.join(dirpath, filename)
                    print("Processing: " + fpath)

                    # use the audio file as the audio source
                    with sr.AudioFile(fpath) as source:
                        audio = r.record(source)  # read the entire audio file

                    # recognize speech using Google Cloud Speech
                    # GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
                    try:
                        # print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
                        translation = r.recognize_google_cloud(audio)
                        translation_gcloud_writer.write(
                            "%s\n" % (dirpath + ", " + filename[6:-4] + ", " + translation))
                        print("Google Cloud Speech thinks you said " + translation)
                    except sr.UnknownValueError:
                        print("Google Cloud Speech could not understand audio")
                        translation_gcloud_writer.write(
                            "%s\n" % (dirpath + ", " + filename[6:-4] + ", "))
                    except sr.RequestError as e:
                        print(
                            "Could not request results from Google Cloud Speech service; {0}".format(e))

    translation_gcloud_writer.close()