import os
import json
import random
import torch
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
intents_path = os.path.join(BASE_DIR, "intents.json")
if not os.path.exists(intents_path):
    intents_path = os.path.join(BASE_DIR, "static", "intents.json")
with open(intents_path, 'r', encoding='utf-8') as json_data:
    intents = json.load(json_data)
FILE = os.path.join(BASE_DIR, "data.pth")
data = torch.load(FILE, map_location=device)
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()
bot_name = "Sam"
def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)
    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    return "I do not understand..."
