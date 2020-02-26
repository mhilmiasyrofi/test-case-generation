from jiwer import wer

if __name__ == '__main__':

    file = open("alexa-test-command.txt")

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
    for line in lines :
        line = line.split(", ")
        tts = line[0]
        audio_id = line[1]
        translation = line[2]
        if ("apple" in tts)  :
            apple_alexa.write(audio_id + ", " +
                              str(wer(translation, data[int(audio_id)])) + "\n")
        else :
            google_alexa.write(audio_id + ", " + str(wer(translation, data[int(audio_id)])) + "\n")
    
    file.close()
    apple_alexa.close()
    google_alexa.close()

    file = open("output/deepspeech_translation.txt")
    apple_deepspeech = open("error/apple_deepspeech.txt", "w+")
    google_deepspeech = open("error/google_deepspeech.txt", "w+")
    lines = file.readlines()
    for line in lines:
        line = line.split(",")
        tts = line[0]
        audio_id = line[1]
        translation = line[2]
        if ("apple" in tts):
            apple_deepspeech.write(audio_id + ", " +
                              str(wer(translation, data[int(audio_id)])) + "\n")
        else:
            google_deepspeech.write(audio_id + ", " +
                               str(wer(translation, data[int(audio_id)])) + "\n")

    file.close()
    apple_deepspeech.close()
    google_deepspeech.close()

    file = open("output/gcloud_translation.txt")
    apple_gcloud = open("error/apple_gcloud.txt", "w+")
    google_gcloud = open("error/google_gcloud.txt", "w+")
    lines = file.readlines()
    for line in lines:
        line = line.split(",")
        tts = line[0]
        audio_id = line[1]
        translation = line[2]
        if ("apple" in tts):
            apple_gcloud.write(audio_id + ", " +
                              str(wer(translation, data[int(audio_id)])) + "\n")
        else:
            google_gcloud.write(audio_id + ", " +
                               str(wer(translation, data[int(audio_id)])) + "\n")

    file.close()
    apple_gcloud.close()
    google_gcloud.close()

    file = open("output/gspeech_translation.txt")
    apple_gspeech = open("error/apple_gspeech.txt", "w+")
    google_gspeech = open("error/google_gspeech.txt", "w+")
    lines = file.readlines()
    for line in lines:
        line = line.split(",")
        tts = line[0]
        audio_id = line[1]
        translation = line[2]
        if ("apple" in tts):
            apple_gspeech.write(audio_id + ", " +
                              str(wer(translation, data[int(audio_id)])) + "\n")
        else:
            google_gspeech.write(audio_id + ", " +
                               str(wer(translation, data[int(audio_id)])) + "\n")

    file.close()
    apple_gspeech.close()
    google_gspeech.close()

    file = open("output/wit_translation.txt")
    apple_wit = open("error/apple_wit.txt", "w+")
    google_wit = open("error/google_wit.txt", "w+")
    lines = file.readlines()
    for line in lines:
        line = line.split(",")
        tts = line[0]
        audio_id = line[1]
        translation = line[2]
        if ("apple" in tts):
            apple_wit.write(audio_id + ", " +
                              str(wer(translation, data[int(audio_id)])) + "\n")
        else:
            google_wit.write(audio_id + ", " +
                               str(wer(translation, data[int(audio_id)])) + "\n")

    file.close()
    apple_wit.close()
    google_wit.close()
