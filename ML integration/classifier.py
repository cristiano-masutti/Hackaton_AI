# Requires transformers library
from joblib import Parallel, delayed
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import os
import sys
import pandas as pd
from transformers import pipeline

THRESHOLD = 0.635  # Ideal is 0.69 on dataset

fake_prediction_model = pipeline("audio-classification", model="alexandreacff/wav2vec2-base-ft-fake-detection")

def predict_fake(wav):
  model_result = fake_prediction_model(wav)
  prediction = model_result[0]['label']
  return model_result[0]['label'], model_result[0]['score']

if len(sys.argv) < 2:
  print("Usage: python classifier.py <audio1> <audio2> ...")
  sys.exit(1)

audio_files = sys.argv[1:]
scores = []
labels = []

for audio in audio_files:
  if not os.path.exists(audio):
    print(f"File {audio} does not exist")
  else:
    label, score = predict_fake(audio)
    labels.append('fake' if score > THRESHOLD else 'real')
    scores.append(score)

# Create file with results
df = pd.DataFrame({'audio': audio_files, 'label': labels, 'score': scores})

# Save to CSV
df.to_csv('results.csv', index=False)

