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


def recognize_wit(audio_data, key, show_all=False):
    """
    Performs speech recognition on ``audio_data`` (an ``AudioData`` instance), using the Wit.ai API.

    The Wit.ai API key is specified by ``key``. Unfortunately, these are not available without `signing up for an account <https://wit.ai/>`__ and creating an app. You will need to add at least one intent to the app before you can see the API key, though the actual intent settings don't matter.

    To get the API key for a Wit.ai app, go to the app's overview page, go to the section titled "Make an API request", and look for something along the lines of ``Authorization: Bearer XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX``; ``XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`` is the API key. Wit.ai API keys are 32-character uppercase alphanumeric strings.

    The recognition language is configured in the Wit.ai app settings.

    Returns the most likely transcription if ``show_all`` is false (the default). Otherwise, returns the `raw API response <https://wit.ai/docs/http/20141022#get-intent-via-text-link>`__ as a JSON dictionary.

    Raises a ``speech_recognition.UnknownValueError`` exception if the speech is unintelligible. Raises a ``speech_recognition.RequestError`` exception if the speech recognition operation failed, if the key isn't valid, or if there is no internet connection.
    """

    wav_data = audio_data.get_wav_data(
        # audio samples must be at least 8 kHz
        convert_rate=None if audio_data.sample_rate >= 8000 else 8000,
        convert_width=2  # audio samples should be 16-bit
    )
    url = "https://api.wit.ai/speech?v=20170307"
    request = Request(url, data=wav_data, headers={
        "Authorization": "Bearer {}".format(key), "Content-Type": "audio/wav"})
    try:
        # response = urlopen(request, timeout=self.operation_timeout)
        response = urlopen(request, context=ssl.create_default_context(
            cafile=certifi.where()))
    except HTTPError as e:
        raise RequestError(
            "recognition request failed: {}".format(e.reason))
    except URLError as e:
        raise RequestError(
            "recognition connection failed: {}".format(e.reason))
    response_text = response.read().decode("utf-8")
    result = json.loads(response_text)

    # return results
    if show_all:
        return result
    if "_text" not in result or result["_text"] is None:
        raise UnknownValueError()
    return result["_text"]


if __name__ == '__main__':

    translation_wit_writer = open("output/wit_translation.txt", "w+")

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

                    # recognize speech using Wit.ai
                    # Wit.ai keys are 32-character uppercase alphanumeric strings
                    WIT_AI_KEY = "5PBOPP2VVZM3MJFQOKK57YRG4DFWXIBZ"
                    try:
                        translation = recognize_wit(audio, key=WIT_AI_KEY)
                        translation_wit_writer.write(
                            "%s\n" % (dirpath + ", " + filename[6:-4] + ", " + translation))
                        print("Wit.ai thinks you said " + translation)
                    except sr.UnknownValueError:
                        print("Wit.ai could not understand audio")
                        translation_wit_writer.write(
                            "%s\n" % (dirpath + ", " + filename[6:-4] + ", "))
                    except sr.RequestError as e:
                        print(
                            "Could not request results from Wit.ai service; {0}".format(e))

    translation_wit_writer.close()
