import os
import wave
import struct
import glob


if __name__ == '__main__':

    files = [f for f in glob.glob("tts_apple/generated_speech/*.wav", recursive=True)]
    files.sort()

    output_folder = "sr_alexa/alexa_data/"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for fpath in files:

        file_id = fpath.split("/")[-1]
        output_file = output_folder + file_id

        data = []

        skill_executor = wave.open("sr_alexa/skill_executor.wav", 'rb')
        gap = wave.open("sr_alexa/gap.wav", 'rb')
        alexa_instruction = wave.open(fpath, 'rb')
        for j in range(0, skill_executor.getnframes()):
            current_frame = skill_executor.readframes(1)
            data.append([alexa_instruction.getparams(), current_frame])
        for j in range(0, gap.getnframes()):
            current_frame = gap.readframes(1)
            data.append([alexa_instruction.getparams(), current_frame])
            data.append([alexa_instruction.getparams(), current_frame])
        for j in range(0, alexa_instruction.getnframes()):
            current_frame = alexa_instruction.readframes(1)
            data.append([alexa_instruction.getparams(), current_frame])

        alexa_instruction.close()
        skill_executor.close()
        alexa_instruction.close()

        output = wave.open(output_file, 'wb')
        output.setparams(data[0][0])
        for params, frames in data:
            output.writeframes(frames)
        output.close()

        print("Save audio at %s" % output_file)
