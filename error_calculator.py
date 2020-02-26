from jiwer import wer

if __name__ == '__main__':

    file = open("corpus-sentence.txt")

    lines = file.readlines()

    data = {}

    i = 0
    for line in lines:
        i = i + 1
        data[i] = line
    
    file.close()

    file = open("output/alexa_translation.txt")
    apple_alexa = open("error/apple_alexa.txt", "w+")
    google_alexa = open("error/google_alexa.txt", "w+")
    lines = file.readlines()
    apple = {}
    google = {}
    for line in lines:
        line = line.split(",")
        tts = line[0]
        audio_id = line[1]
        idx = int(audio_id)
        translation = line[2]
        error = "%.2f" % wer(translation, data[int(audio_id)])
        if ("apple" in tts):
            if (idx not in apple.keys()):
                apple[idx] = error
            else:
                if (apple[idx] > error):
                    apple[idx] = error
        else:
            if (idx not in google.keys()):
                google[idx] = error
            else:
                if (google[idx] > error):
                    google[idx] = error
    keys = sorted(apple.keys())
    for k in keys:
        apple_alexa.write(str(k) + ", " + apple[k] + "\n")

    keys = sorted(google.keys())
    for k in keys:
        google_alexa.write(str(k) + ", " + google[k] + "\n")

    file.close()
    apple_alexa.close()
    google_alexa.close()

    file = open("output/deepspeech_translation.txt")
    apple_deepspeech = open("error/apple_deepspeech.txt", "w+")
    google_deepspeech = open("error/google_deepspeech.txt", "w+")
    lines = file.readlines()
    apple = {}
    google = {}
    for line in lines:
        line = line.split(",")
        tts = line[0]
        audio_id = line[1]
        idx = int(audio_id)
        translation = line[2]
        error = "%.2f" % wer(translation, data[int(audio_id)])
        if ("apple" in tts):
            if (idx not in apple.keys()) :
                apple[idx] = error
            else :
                if (apple[idx] > error) :
                    apple[idx] = error
        else:
            if (idx not in google.keys()):
                google[idx] = error
            else:
                if (google[idx] > error):
                    google[idx] = error
    keys = sorted(apple.keys())
    for k in keys :
        apple_deepspeech.write(str(k) + ", " + apple[k] + "\n")

    keys = sorted(google.keys())
    for k in keys:
        google_deepspeech.write(str(k) + ", " + google[k] + "\n")

    file.close()
    apple_deepspeech.close()
    google_deepspeech.close()

    file = open("output/gcloud_translation.txt")
    apple_gcloud = open("error/apple_gcloud.txt", "w+")
    google_gcloud = open("error/google_gcloud.txt", "w+")
    lines = file.readlines()
    apple = {}
    google = {}
    for line in lines:
        line = line.split(",")
        tts = line[0]
        audio_id = line[1]
        idx = int(audio_id)
        translation = line[2]
        error = "%.2f" % wer(translation, data[int(audio_id)])
        if ("apple" in tts):
            if (idx not in apple.keys()):
                apple[idx] = error
            else:
                if (apple[idx] > error):
                    apple[idx] = error
        else:
            if (idx not in google.keys()):
                google[idx] = error
            else:
                if (google[idx] > error):
                    google[idx] = error
    keys = sorted(apple.keys())
    for k in keys:
        apple_gcloud.write(str(k) + ", " + apple[k] + "\n")

    keys = sorted(google.keys())
    for k in keys:
        google_gcloud.write(str(k) + ", " + google[k] + "\n")

    file.close()
    apple_gcloud.close()
    google_gcloud.close()

    file = open("output/gspeech_translation.txt")
    apple_gspeech = open("error/apple_gspeech.txt", "w+")
    google_gspeech = open("error/google_gspeech.txt", "w+")
    lines = file.readlines()
    apple = {}
    google = {}
    for line in lines:
        line = line.split(",")
        tts = line[0]
        audio_id = line[1]
        idx = int(audio_id)
        translation = line[2]
        error = "%.2f" % wer(translation, data[int(audio_id)])
        if ("apple" in tts):
            if (idx not in apple.keys()):
                apple[idx] = error
            else:
                if (apple[idx] > error):
                    apple[idx] = error
        else:
            if (idx not in google.keys()):
                google[idx] = error
            else:
                if (google[idx] > error):
                    google[idx] = error
    keys = sorted(apple.keys())
    for k in keys:
        apple_gspeech.write(str(k) + ", " + apple[k] + "\n")

    keys = sorted(google.keys())
    for k in keys:
        google_gspeech.write(str(k) + ", " + google[k] + "\n")


    file.close()
    apple_gspeech.close()
    google_gspeech.close()

    file = open("output/wit_translation.txt")
    apple_wit = open("error/apple_wit.txt", "w+")
    google_wit = open("error/google_wit.txt", "w+")
    lines = file.readlines()
    apple = {}
    google = {}
    for line in lines:
        line = line.split(",")
        tts = line[0]
        audio_id = line[1]
        idx = int(audio_id)
        translation = line[2]
        error = "%.2f" % wer(translation, data[int(audio_id)])
        if ("apple" in tts):
            if (idx not in apple.keys()):
                apple[idx] = error
            else:
                if (apple[idx] > error):
                    apple[idx] = error
        else:
            if (idx not in google.keys()):
                google[idx] = error
            else:
                if (google[idx] > error):
                    google[idx] = error
    keys = sorted(apple.keys())
    for k in keys:
        apple_wit.write(str(k) + ", " + apple[k] + "\n")

    keys = sorted(google.keys())
    for k in keys:
        google_wit.write(str(k) + ", " + google[k] + "\n")


    file.close()
    apple_wit.close()
    google_wit.close()
