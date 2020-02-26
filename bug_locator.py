
def getMapping(lines) :
    hash_map = {}
    for line in lines:
        line = line.split(",")
        idx = int(line[0])
        value = float(line[1])
        hash_map[idx] = value
    return hash_map

if __name__ == '__main__':

    apple_alexa = open("error/apple_alexa.txt")
    apple_alexa_lines = apple_alexa.readlines()
    apple_alexa_map = getMapping(apple_alexa_lines)

    google_alexa = open("error/google_alexa.txt")
    google_alexa_lines = google_alexa.readlines()
    google_alexa_map = getMapping(google_alexa_lines)


    apple_deepspeech = open("error/apple_deepspeech.txt")
    apple_deepspeech_lines = apple_deepspeech.readlines()
    apple_deepspeech_map = getMapping(apple_alexa_lines)

    google_deepspeech = open("error/google_deepspeech.txt")
    google_deepspeech_lines = google_deepspeech.readlines()
    google_deepspeech_map = getMapping(google_deepspeech_lines)


    apple_gcloud = open("error/apple_gcloud.txt")
    apple_gcloud_lines = apple_gcloud.readlines()
    apple_gcloud_map = getMapping(apple_gcloud_lines)

    google_gcloud = open("error/google_gcloud.txt")
    google_gcloud_lines = google_gcloud.readlines()
    google_gcloud_map = getMapping(google_gcloud_lines)


    apple_gspeech = open("error/apple_gspeech.txt")
    apple_gspeech_lines = apple_gspeech.readlines()
    apple_gspeech_map = getMapping(apple_gspeech_lines)

    google_gspeech = open("error/google_gspeech.txt")
    google_gspeech_lines = google_gspeech.readlines()
    google_gspeech_map = getMapping(google_gspeech_lines)


    apple_wit = open("error/apple_wit.txt")
    apple_wit_lines = apple_wit.readlines()
    apple_wit_map = getMapping(apple_wit_lines)

    google_wit = open("error/google_wit.txt")
    google_wit_lines = google_wit.readlines()
    google_wit_map = getMapping(google_wit_lines)

    
    alexa_bug = open("bug/sr/alexa_bug.txt", "w+")
    deepspeech_bug = open("bug/sr/deepspeech_bug.txt", "w+")
    gcloud_bug = open("bug/sr/gcloud_bug.txt", "w+")
    gspeech_bug = open("bug/sr/gspeech_bug.txt", "w+")
    wit_bug = open("bug/sr/wit_bug.txt", "w+")


    ### ALEXA BUG
    for idx, alexa_error in apple_alexa_map.items():
        if (alexa_error != 0) :
            isOtherSpeechRecognitionCanTranslate = False
            if (idx in apple_deepspeech_map.keys()) :
                if (apple_deepspeech_map[idx] == 0) :
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in apple_gcloud_map.keys()):
                if (apple_gcloud_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in apple_gspeech_map.keys()):
                if (apple_gspeech_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in apple_wit_map.keys()):
                if (apple_wit_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            
            if isOtherSpeechRecognitionCanTranslate :
                alexa_bug.write("apple, " + str(idx) + "\n")

    for idx, alexa_error in google_alexa_map.items():
        if (alexa_error != 0):
            isOtherSpeechRecognitionCanTranslate = False
            if (idx in google_deepspeech_map.keys()) :
                if (google_deepspeech_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in google_gcloud_map.keys()):
                if (google_gcloud_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in google_gspeech_map.keys()):
                if (google_gspeech_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in google_wit_map.keys()):
                if (google_wit_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True

            if isOtherSpeechRecognitionCanTranslate:
                alexa_bug.write("google, " + str(idx) + "\n")



    ### DEEPSPEECH BUG
    for idx, deepspeech_error in apple_deepspeech_map.items():
        if (deepspeech_error != 0):
            isOtherSpeechRecognitionCanTranslate = False
            if (idx in apple_alexa_map.keys()):
                if (apple_alexa_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in apple_gcloud_map.keys()):
                if (apple_gcloud_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in apple_gspeech_map.keys()):
                if (apple_gspeech_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in apple_wit_map.keys()):
                if (apple_wit_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True

            if isOtherSpeechRecognitionCanTranslate:
                deepspeech_bug.write("apple, " + str(idx) + "\n")

    for idx, deepspeech_error in google_deepspeech_map.items():
        if (deepspeech_error != 0):
            isOtherSpeechRecognitionCanTranslate = False
            if (idx in google_alexa_map.keys()):
                if (google_alexa_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in google_gcloud_map.keys()):
                if (google_gcloud_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in google_gspeech_map.keys()):
                if (google_gspeech_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in google_wit_map.keys()):
                if (google_wit_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True

            if isOtherSpeechRecognitionCanTranslate:
                deepspeech_bug.write("google, " + str(idx) + "\n")

    ### GCLOUD BUG
    for idx, gcloud_error in apple_gcloud_map.items():
        if (gcloud_error != 0):
            isOtherSpeechRecognitionCanTranslate = False
            if (idx in apple_alexa_map.keys()):
                if (apple_alexa_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in apple_deepspeech_map.keys()):
                if (apple_deepspeech_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in apple_gspeech_map.keys()):
                if (apple_gspeech_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in apple_wit_map.keys()):
                if (apple_wit_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True

            if isOtherSpeechRecognitionCanTranslate:
                gcloud_bug.write("apple, " + str(idx) + "\n")

    for idx, gcloud_error in google_gcloud_map.items():
        if (gcloud_error != 0):
            isOtherSpeechRecognitionCanTranslate = False
            if (idx in google_alexa_map.keys()):
                if (google_alexa_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in google_deepspeech_map.keys()):
                if (google_deepspeech_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in google_gspeech_map.keys()):
                if (google_gspeech_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in google_wit_map.keys()):
                if (google_wit_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True

            if isOtherSpeechRecognitionCanTranslate:
                gcloud_bug.write("google, " + str(idx) + "\n")



    ### GSPEECH BUG
    for idx, gspeech_error in apple_gspeech_map.items():
        if (gspeech_error != 0):
            isOtherSpeechRecognitionCanTranslate = False
            if (idx in apple_alexa_map.keys()):
                if (apple_alexa_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in apple_deepspeech_map.keys()):
                if (apple_deepspeech_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in apple_gcloud_map.keys()):
                if (apple_gcloud_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in apple_wit_map.keys()):
                if (apple_wit_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True

            if isOtherSpeechRecognitionCanTranslate:
                gspeech_bug.write("apple, " + str(idx) + "\n")

    for idx, gspeech_error in google_gspeech_map.items():
        if (gspeech_error != 0):
            isOtherSpeechRecognitionCanTranslate = False
            if (idx in google_alexa_map.keys()):
                if (google_alexa_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in google_deepspeech_map.keys()):
                if (google_deepspeech_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in google_gcloud_map.keys()):
                if (google_gcloud_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in google_wit_map.keys()):
                if (google_wit_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True

            if isOtherSpeechRecognitionCanTranslate:
                gspeech_bug.write("google, " + str(idx) + "\n")


    ### WIT BUG
    for idx, wit_error in apple_wit_map.items():
        if (wit_error != 0):
            isOtherSpeechRecognitionCanTranslate = False
            if (idx in apple_alexa_map.keys()):
                if (apple_alexa_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in apple_deepspeech_map.keys()):
                if (apple_deepspeech_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in apple_gcloud_map.keys()):
                if (apple_gcloud_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in apple_gspeech_map.keys()):
                if (apple_gspeech_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True

            if isOtherSpeechRecognitionCanTranslate:
                wit_bug.write("apple, " + str(idx) + "\n")

    for idx, wit_error in google_wit_map.items():
        if (wit_error != 0):
            isOtherSpeechRecognitionCanTranslate = False
            if (idx in google_alexa_map.keys()):
                if (google_alexa_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in google_deepspeech_map.keys()):
                if (google_deepspeech_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in google_gcloud_map.keys()):
                if (google_gcloud_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True
            if (idx in google_gspeech_map.keys()):
                if (google_gspeech_map[idx] == 0):
                    isOtherSpeechRecognitionCanTranslate = True

            if isOtherSpeechRecognitionCanTranslate:
                wit_bug.write("google, " + str(idx) + "\n")

    alexa_bug.close()
    deepspeech_bug.close()
    gcloud_bug.close()
    gspeech_bug.close()
    wit_bug.close()


    tts_apple_bug = open("bug/tts/apple_bug.txt", "w+")
    tts_google_bug = open("bug/tts/google_bug.txt", "w+")

    length = len(apple_deepspeech_lines)

    for i in range(length) :
        ## apple tts bug
        if (i in apple_alexa_map.keys() 
            and i in apple_deepspeech_map.keys() 
            and i in apple_gcloud_map.keys()
            and i in apple_gspeech_map.keys()
            and i in apple_wit_map.keys()) :
            if (apple_alexa_map[i] != 0 
                and apple_deepspeech_map[i] != 0
                and apple_gcloud_map[i] != 0
                and apple_gspeech_map[i] != 0
                and apple_wit_map[i] != 0
                ) :
                tts_apple_bug.write(str(i) + "\n")
        
        ## google tts bug
        if (i in google_alexa_map.keys() 
            and i in google_deepspeech_map.keys() 
            and i in google_gcloud_map.keys()
            and i in google_gspeech_map.keys()
            and i in google_wit_map.keys()) :
            if (google_alexa_map[i] != 0 
                and google_deepspeech_map[i] != 0
                and google_gcloud_map[i] != 0
                and google_gspeech_map[i] != 0
                and google_wit_map[i] != 0
                ) :
                tts_google_bug.write(str(i) + "\n")

    tts_apple_bug.close()
    tts_google_bug.close()


    apple_alexa.close()
    apple_deepspeech.close()
    apple_gcloud.close()
    apple_gspeech.close()
    apple_wit.close()

    google_alexa.close()
    google_deepspeech.close()
    google_gcloud.close()
    google_gspeech.close()
    google_wit.close()




    

    




    
