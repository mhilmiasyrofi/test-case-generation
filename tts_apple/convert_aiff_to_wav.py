# importing os module  
import os 
  
# Get the list of all files and directories 
# in the root directory 
input_dir = "tts_apple/aiff_generated_speech/"
output_dir = "tts_apple/generated_speech/"

dir_list = os.listdir(input_dir) 

for path in dir_list :
    file_id = path.split(".")[0]
    command = "ffmpeg -i " + input_dir + file_id + \
        ".aiff -acodec pcm_s16le -ac 1 -ar 16000 " + output_dir + file_id + ".wav -y"
    # print(command)
    os.system(command)
