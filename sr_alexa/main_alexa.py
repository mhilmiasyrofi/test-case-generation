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

translation_writer = open("output/alexa_translation.txt", "w+")

data = "sr_alexa/alexa_data/"

for (dirpath, _, filenames) in os.walk(data):
    if (len(filenames) > 0):
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        for i in range(1,len(filenames)+1):
            filename = "audio_" + str(i) + ".wav"
            if (filename in filenames) :
                fpath = os.path.join(dirpath, filename)
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
                    print("Transcription: " + text)
                    translation_writer.write("%s\n" % (dirpath + ", " + filename[6:-4] + ", " + text))
                else :
                    print("Transcription: ")
                    translation_writer.write("%s\n" % (dirpath + ", " + filename[6:-4] + ", "))
                    

translation_writer.close()

