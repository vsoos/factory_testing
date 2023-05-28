import os
import subprocess

def convert_m4a_to_wav(folder_name):
    input_folder = os.path.join(os.getcwd(), folder_name)
    output_folder = os.path.join(os.getcwd(), 'converted_wav')

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of .m4a files in the input folder
    m4a_files = [file for file in os.listdir(input_folder) if file.endswith('.m4a')]

    # Convert each .m4a file to .wav
    for m4a_file in m4a_files:
        input_path = os.path.join(input_folder, m4a_file)
        wav_file = os.path.splitext(m4a_file)[0] + '.wav'
        output_path = os.path.join(output_folder, wav_file)

        # Use FFmpeg to perform the conversion
        subprocess.call(['ffmpeg', '-i', input_path, output_path])

    print('Conversion complete!')

# Usage example
convert_m4a_to_wav('original_m4a')

