import os
import glob
import subprocess

if __name__ == '__main__':

    translation_writer = open("output/deepspeech_translation.txt", "w+")
    
    data = "tts_apple/generated_speech/"
    files = [f for f in glob.glob(data + "*.wav", recursive=True)]
    # files = os.listdir(data)
    files.sort()

    for fpath in files:
        file_id = fpath.split(".")[0].split("/")[-1]
        cmd = 'deepspeech --model sr_deepspeech/deepspeech-0.6.1-models/output_graph.pbmm --lm sr_deepspeech/deepspeech-0.6.1-models/lm.binary --trie sr_deepspeech/deepspeech-0.6.1-models/trie --audio ' + fpath

        proc = subprocess.Popen([cmd],
                                stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()

        transcription = out.decode("utf-8")
        
        translation_writer.write("%s" % (file_id + ", " + transcription))
        # print("Out: " + transcription)

    translation_writer.close()





