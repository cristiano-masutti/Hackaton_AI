# Run diarization.py with parameters:
import sys
import os
import moviepy.editor as mp
import pandas as pd

if len(sys.argv) < 2:
    print("Usage: python pipeline.py <audio1>")
    sys.exit(1)

audio_file = sys.argv[1]
audio_file = audio_file.split('.')[0]  # Remove wav

if not os.path.exists(f'{audio_file}.wav'):
    print(f"File {audio_file}.wav does not exist")
    sys.exit(1)

# Directly call diarization.py as a script
os.system(f"python diarization.py {audio_file}.wav")

# Above function blocks so when it's done, we can process the output file of the form <audio_file>.srt
# and run classifier.py on each segment
def split_audio(audio, output_name, from_time, to_time):
    clip = mp.AudioFileClip(audio).subclip(from_time, to_time)
    clip.write_audiofile(output_name)

# Read the srt file
segments = []
with open(f"{audio_file}.srt", "r") as f:
    lines = f.readlines()
    for i in range(0, len(lines), 4):
        start, end = lines[i+1].split(" --> ")
        segments.append((start, end))

# Split the audio into segments
for i, (start, end) in enumerate(segments):
    split_audio(f'{audio_file}.wav', f"segment{i}.wav", start, end)

# For each row in the tsv file, run classifier.py on the segment
os.system(f"python classifier.py {' '.join([f'segment{i}.wav' for i in range(len(segments))])}")

# Clean up
os.system(f"rm {' '.join([f'segment{i}.wav' for i in range(len(segments))])}")

# Read results.csv and print the results
df = pd.read_csv("results.csv")

for i, row in df.iterrows():
    print(f"Segment {i}, {segments[i][0]} -> {segments[i][1]}: {row['label']} with score {row['score']}")
