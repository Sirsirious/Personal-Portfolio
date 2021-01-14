import pytest
from ai.ner import *


def test_load_ner():
    ner = load_ner()
    assert ner is not None
    assert "keras" in str(type(ner))


def test_load_vocabs():
    word2idx, idx2word, tags2idx, idx2tags = load_vocabs()
    assert type(word2idx) == dict
    assert len(word2idx) == len(idx2word)
    assert type(tags2idx) == dict
    assert len(tags2idx) == len(idx2tags)


def test_predict():
    ner = load_ner()
    word2idx, idx2word, tags2idx, idx2tags = load_vocabs()
    ner_dict = predict("This is a test sentence", ner, word2idx, idx2tags)
    assert type(ner_dict) == dict
    assert len(ner_dict) == 5
    assert 'token' in ner_dict[0]
    assert 'tag' in ner_dict[0]
    ner_dict = predict("My name is James", ner, word2idx, idx2tags)
    assert ner_dict[3]['tag'] == 'B-per'
    assert ner_dict[3]['token'] == "James"

