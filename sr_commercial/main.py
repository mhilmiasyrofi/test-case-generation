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


def recognize_houndify(audio_data, client_id, client_key, show_all=False):
    """
    Performs speech recognition on ``audio_data`` (an ``AudioData`` instance), using the Houndify API.

    The Houndify client ID and client key are specified by ``client_id`` and ``client_key``, respectively. Unfortunately, these are not available without `signing up for an account <https://www.houndify.com/signup>`__. Once logged into the `dashboard <https://www.houndify.com/dashboard>`__, you will want to select "Register a new client", and fill in the form as necessary. When at the "Enable Domains" page, enable the "Speech To Text Only" domain, and then select "Save & Continue".

    To get the client ID and client key for a Houndify client, go to the `dashboard <https://www.houndify.com/dashboard>`__ and select the client's "View Details" link. On the resulting page, the client ID and client key will be visible. Client IDs and client keys are both Base64-encoded strings.

    Currently, only English is supported as a recognition language.

    Returns the most likely transcription if ``show_all`` is false (the default). Otherwise, returns the raw API response as a JSON dictionary.

    Raises a ``speech_recognition.UnknownValueError`` exception if the speech is unintelligible. Raises a ``speech_recognition.RequestError`` exception if the speech recognition operation failed, if the key isn't valid, or if there is no internet connection.
    """

    wav_data = audio_data.get_wav_data(
        convert_rate=None if audio_data.sample_rate in [
            8000, 16000] else 16000,  # audio samples must be 8 kHz or 16 kHz
        convert_width=2  # audio samples should be 16-bit
    )
    url = "https://api.houndify.com/v1/audio"
    user_id, request_id = str(uuid.uuid4()), str(uuid.uuid4())
    request_time = str(int(time.time()))
    request_signature = base64.urlsafe_b64encode(
        hmac.new(
            base64.urlsafe_b64decode(client_key),
            user_id.encode(
                "utf-8") + b";" + request_id.encode("utf-8") + request_time.encode("utf-8"),
            hashlib.sha256
        ).digest()  # get the HMAC digest as bytes
    ).decode("utf-8")
    request = Request(url, data=wav_data, headers={
        "Content-Type": "application/json",
        "Hound-Request-Info": json.dumps({"ClientID": client_id, "UserID": user_id}),
        "Hound-Request-Authentication": "{};{}".format(user_id, request_id),
        "Hound-Client-Authentication": "{};{};{}".format(client_id, request_time, request_signature)
    })
    try:
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
    if "Disambiguation" not in result or result["Disambiguation"] is None:
        raise UnknownValueError()
    return result['Disambiguation']['ChoiceData'][0]['Transcription']


if __name__ == '__main__':
    data = "tts_apple/generated_speech/"
    files = [f for f in glob.glob(data + "*.wav", recursive=True)]
    # files = os.listdir(data)
    files.sort()

    translation_gspeech_writer = open("output/gspeech_translation.txt", "w+")
    translation_gcloud_writer = open("output/gcloud_translation.txt", "w+")
    translation_wit_writer = open("output/wit_translation.txt", "w+")
    translation_houndify_writer = open("output/houndify_translation.txt", "w+")

    r = sr.Recognizer()

    for fpath in files:
        AUDIO_FILE = fpath
        file_id = fpath.split(".")[0].split("/")[-1]
        print("Processing: " + AUDIO_FILE)
        # AUDIO_FILE = path.join(path.dirname(
        #     path.realpath(__file__)), fpath)
        # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
        # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

        # use the audio file as the audio source
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            translation = r.recognize_google(audio)
            translation_gspeech_writer.write(
                "%s\n" % (file_id + ", " + translation))
            print("Google Speech Recognition thinks you said " + translation)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))

        # recognize speech using Google Cloud Speech
        # GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
        try:
            # print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
            translation = r.recognize_google_cloud(audio)
            translation_gcloud_writer.write(
                "%s\n" % (file_id + ", " + translation))
            print("Google Cloud Speech thinks you said " + translation)
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Cloud Speech service; {0}".format(e))

        # recognize speech using Wit.ai
        # Wit.ai keys are 32-character uppercase alphanumeric strings
        WIT_AI_KEY = "5PBOPP2VVZM3MJFQOKK57YRG4DFWXIBZ"
        try:
            translation = recognize_wit(audio, key=WIT_AI_KEY)
            translation_wit_writer.write(
                "%s\n" % (file_id + ", " + translation))
            print("Wit.ai thinks you said " + translation)
        except sr.UnknownValueError:
            print("Wit.ai could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Wit.ai service; {0}".format(e))

        # # recognize speech using Houndify
        # HOUNDIFY_CLIENT_ID = "6nCv2NMoB4Yz310PwCbpjQ=="  # Houndify client IDs are Base64-encoded strings
        # HOUNDIFY_CLIENT_KEY = "wzahBtWGs-OEbys29m_yQJ9xUkVOkDU57w-MjZnUctuVcjMEEPyU2o9Q7oesSia1IgKI3-jOTQ4ujzMXnIChBA=="  # Houndify client keys are Base64-encoded strings
        # try:
        #     translation = recognize_houndify(
        #         audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY)
        #     translation_houndify_writer.write("%s\n" % (translation))
        #     print("Houndify thinks you said " + translation)
        # except sr.UnknownValueError:
        #     print("Houndify could not understand audio")
        # except sr.RequestError as e:
        #     print("Could not request results from Houndify service; {0}".format(e))

    translation_gspeech_writer.close()
    translation_gcloud_writer.close()
    translation_wit_writer.close()
    translation_houndify_writer.close()
