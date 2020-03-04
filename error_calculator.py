from jiwer import wer

def preprocess_translation(translation) :
    translation = translation[:-1].lower()
    words = translation.split(" ")
    preprocessed = []
    for w in words :
        substitution = ""
        if w == "mister" :
            substitution = "mr"
        elif w == "missus":
            substitution = "mrs"
        elif w == "can not":
            substitution = "cannot"
        elif w == "mr." :
            substitution = "mr"
        elif w == "i'm" :
            substitution = "i am"
        elif w == "you're":
            substitution = "you are"
        elif w == "1" :
            substitution = "one"
        elif w == "2" :
            substitution = "two"
        elif w == "3" :
            substitution = "three"
        elif w == "4" :
            substitution = "four"
        elif w == "5" :
            substitution = "five"
        elif w == "6" :
            substitution = "six"
        elif w == "7" :
            substitution = "seven"
        elif w == "8" :
            substitution = "eight"
        elif w == "9" :
            substitution = "nine"
        else :
            substitution = w
        preprocessed.append(substitution)
    return " ".join(preprocessed)[1:] + "\n"


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
        parts = line.split(",")
        if (line != "\n" and len(parts) == 3) : 
            tts = parts[0]
            audio_id = parts[1]
            idx = int(audio_id)
            translation = parts[2]
            translation = preprocess_translation(translation)
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
        parts = line.split(",")
        if (line != "\n" and len(parts) == 3) : 
            tts = parts[0]
            audio_id = parts[1]
            idx = int(audio_id)
            translation = parts[2]
            translation = preprocess_translation(translation)
            # if (int(audio_id) == 336) :
            #     print("T: " + str(translation))
            #     print("A: " + str(data[int(audio_id)]))
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
        parts = line.split(",")
        if (line != "\n" and len(parts) == 3) : 
            tts = parts[0]
            audio_id = parts[1]
            idx = int(audio_id)
            translation = parts[2]
            translation = preprocess_translation(translation)
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
        parts = line.split(",")
        if (line != "\n" and len(parts) == 3) : 
            tts = parts[0]
            audio_id = parts[1]
            idx = int(audio_id)
            translation = parts[2]
            translation = preprocess_translation(translation)
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
        parts = line.split(",")
        if (line != "\n" and len(parts) == 3) : 
            tts = parts[0]
            audio_id = parts[1]
            idx = int(audio_id)
            translation = parts[2]
            translation = preprocess_translation(translation)
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


    file = open("output/wav2letter_translation.txt")
    apple_wav2letter = open("error/apple_wav2letter.txt", "w+")
    google_wav2letter = open("error/google_wav2letter.txt", "w+")
    lines = file.readlines()
    apple = {}
    google = {}
    for line in lines:
        parts = line.split(",")
        if (line != "\n" and len(parts) == 3) : 
            tts = parts[0]
            audio_id = parts[1]
            idx = int(audio_id)
            translation = parts[2]
            translation = preprocess_translation(translation)
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
        apple_wav2letter.write(str(k) + ", " + apple[k] + "\n")

    keys = sorted(google.keys())
    for k in keys:
        google_wav2letter.write(str(k) + ", " + google[k] + "\n")

    file.close()
    apple_wav2letter.close()
    google_wav2letter.close()
