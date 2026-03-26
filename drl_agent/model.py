import numpy as np

class SimplePolicy:
    def __init__(self):
        pass

    def predict(self, state):
        # política simples (simulação)
        return state * 0.95 + np.random.normal(0, 0.01)