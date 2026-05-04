# ============================================================
# NOTE:
# This is a simplified DRL-inspired policy used only for
# demonstration and reproducibility purposes.
# It does NOT implement a full DDPG algorithm.
# ============================================================

import numpy as np
from .model import SimplePolicy

class DDPGAgent:
    """
    Simplified DRL agent used to simulate adaptive control behavior.

    This implementation does not represent a full DDPG algorithm,
    but a lightweight approximation for demonstration purposes.
    """
    def __init__(self):
        self.policy = SimplePolicy()

    def run(self, data):
        results = []

        for value in data:
            action = self.policy.predict(value)
            results.append(action)

        return np.array(results)