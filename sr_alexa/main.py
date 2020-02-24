from alexa_client import AlexaClient
from alexa_client.alexa_client import constants
from alexa_client.alexa_client import helpers

import os, glob

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
refresh_token = os.getenv("REFRESH_TOKEN")

client = AlexaClient(
    client_id=client_id,
    secret=client_secret,
    refresh_token=refresh_token,
    base_url=constants.BASE_URL_NORTH_AMERICA
)

client.connect()  # authenticate and other handshaking steps

dialog_request_id = helpers.generate_unique_id()

# audio_one = open('alexa_open_this_test.wav', 'rb')
# initial_directives = client.send_audio_file(
#     audio_one, dialog_request_id=dialog_request_id)

# with open('../../tests/resources/alexa_what_time_is_it.wav', 'rb') as f:

# fpath = "record_this_please_turn_on_the_light.wav"
translation_writer = open("output/alexa_translation.txt", "w+")

data = "sr_alexa/alexa_data/"

files = [f for f in glob.glob(data + "*.wav", recursive=True)]
# files = os.listdir(data)
files.sort()

for fpath in files:
    file_id = fpath.split(".")[0].split("/")[-1]
    print("Processing: " + fpath)
    audio = open(fpath, 'rb')
    directives = client.send_audio_file(
        audio, dialog_request_id=dialog_request_id)

    success = False
    text = ""
    if directives:
        for j, directive in enumerate(directives):
            if directive.name == 'RenderTemplate':
                success = True
                text = directive.payload['textField']
    else:
        print("Audio " + str(i) + "- Can't get response")

    if (success):
        translation_writer.write("%s\n" % (file_id + ", "+ text))

translation_writer.close()

