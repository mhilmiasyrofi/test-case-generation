import os
import glob
import subprocess

if __name__ == '__main__':

    translation_writer = open("output/deepspeech_translation.txt", "w+")
    
    data = "data/"

    for (dirpath, _, filenames) in os.walk(data):
        if (len(filenames) > 0):
            if not os.path.exists(dirpath):
                os.makedirs(dirpath)
            for filename in filenames:
                if (".wav" in filename):
                    fpath = os.path.join(dirpath, filename)
                    print("Processing: " + fpath)
                    cmd = 'deepspeech --model sr_deepspeech/deepspeech-0.6.1-models/output_graph.pbmm --lm sr_deepspeech/deepspeech-0.6.1-models/lm.binary --trie sr_deepspeech/deepspeech-0.6.1-models/trie --audio ' + fpath

                    proc = subprocess.Popen([cmd],
                                            stdout=subprocess.PIPE, shell=True)
                    (out, err) = proc.communicate()

                    transcription = out.decode("utf-8")
                    
                    translation_writer.write("%s" % (dirpath + ", " + filename + ", " + transcription))
                    # print("Out: " + transcription)

    translation_writer.close()





