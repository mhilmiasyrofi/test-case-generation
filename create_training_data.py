
def get_bug_location(fpath) :
    file = open(fpath)
    lines = file.readlines()
    bugs = []
    for line in lines :
        bugs.append(int(line.split(",")[-1]))
    file.close()
    return bugs

def write_label(bugs, writer) :
    if (i in bugs):
        writer.write(", 1\n")
    else :
        writer.write(", 0\n")


if __name__ == '__main__':

    alexa_bugs = get_bug_location("bug/sr/alexa_bug.txt")
    deepspeech_bugs = get_bug_location("bug/sr/deepspeech_bug.txt")
    gcloud_bugs = get_bug_location("bug/sr/gcloud_bug.txt")
    gspeech_bugs = get_bug_location("bug/sr/gspeech_bug.txt")
    wav2letter_bugs = get_bug_location("bug/sr/wav2letter_bug.txt")
    wit_bugs = get_bug_location("bug/sr/wit_bug.txt")


    file = open("corpus-sentence.txt")
    corpus = file.readlines()
    file.close() 

    alexa_training_data = open("training_data/alexa.txt", "w+")
    deepspeech_training_data = open("training_data/deepspeech.txt", "w+")
    gcloud_training_data = open("training_data/gcloud.txt", "w+")
    gspeech_training_data = open("training_data/gspeech.txt", "w+")
    wav2letter_training_data = open("training_data/wav2letter.txt", "w+")
    wit_training_data = open("training_data/wit.txt", "w+")


    i = 0
    for sentence in corpus :
        i += 1

        alexa_training_data.write(sentence[:-1])
        deepspeech_training_data.write(sentence[:-1])
        gcloud_training_data.write(sentence[:-1])
        gspeech_training_data.write(sentence[:-1])
        wav2letter_training_data.write(sentence[:-1])
        wit_training_data.write(sentence[:-1])

        write_label(alexa_bugs, alexa_training_data)
        write_label(deepspeech_bugs, deepspeech_training_data)
        write_label(gcloud_bugs, gcloud_training_data)
        write_label(gspeech_bugs, gspeech_training_data)
        write_label(wav2letter_bugs, wav2letter_training_data)
        write_label(wit_bugs, wit_training_data)

    alexa_training_data.close()
    deepspeech_training_data.close()
    gcloud_training_data.close()
    gspeech_training_data.close()
    wav2letter_training_data.close()
    wit_training_data.close()
    
