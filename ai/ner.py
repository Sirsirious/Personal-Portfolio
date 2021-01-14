import tensorflow as tf
from tensorflow.keras.preprocessing import sequence
from nlptools.core.structures import tokenize
import json
import numpy as np


def load_ner(language="en", path="preloaded/models/", filename="ner.h5"):
    if language == "en":
        model = tf.keras.models.load_model(path+filename)
        return model
    else:
        raise NotImplemented("No other languages implemented so far.")


def load_vocabs(path="preloaded/data/", tags="tag2idx.json",
                words="word2idx.json"):
    with open(path + words, 'r') as jsonfile:
        word2idx = json.load(jsonfile)
        idx2word = {v: k for k, v in word2idx.items()}
    with open(path + tags, 'r') as jsonfile:
        tags2idx = json.load(jsonfile)
        idx2tags = {v: k for k, v in tags2idx.items()}
    return word2idx, idx2word, tags2idx, idx2tags


def predict(sentence, model, word2idx, idx2tag, max_len=104):
    # Do simple tokenization
    tokens = tokenize(sentence)
    seq = [[word2idx[token.repr] if token.repr in word2idx else word2idx['<unk>'] for token in tokens[1:-1]]]
    test_seq = sequence.pad_sequences(maxlen=max_len, sequences=seq, padding="post", value=len(word2idx) - 1)
    output = model(test_seq)
    outputs = np.argmax(output, axis=-1)
    pred = []
    for i in range(len(tokens[1:-1])):
        if outputs[0][i] == len(word2idx) - 1:
            break
        idx = outputs[0][i]
        pred_label = idx2tag[idx]
        pred.append(pred_label)
    token_ner_dict = {}
    for idx, token in enumerate(tokens[1:-1]):
        token_ner_dict[idx] = {}
        token_ner_dict[idx]['token'] = token.repr
        token_ner_dict[idx]['tag'] = pred[idx]
    return token_ner_dict
