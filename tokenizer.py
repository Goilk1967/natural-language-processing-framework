import re
from collections import Counter
class BytePairEncoder:
    def __init__(self, vocab_size):
        self.vocab_size = vocab_size
        self.merges = {}
    def train(self, text):
        # Simplified BPE training logic
        words = text.split()
        vocab = Counter(words)
        return vocab
    def encode(self, text):
        return text.split()
