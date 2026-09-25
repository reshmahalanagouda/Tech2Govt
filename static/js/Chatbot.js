import os
import json
import random
import torch
import nltk
nltk.download('punkt')

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

BASE_DIR = os.path.dirname(os.path.abspath(_file_))

with open(os.path.join(BASE_DIR, 'static', 'intents.json'), 'r') as json_data:
    intents = json.load(json_data)

FILE = os.path.join(BASE_DIR, "data.pth")
data = torch.load(FILE, map_location=device)
