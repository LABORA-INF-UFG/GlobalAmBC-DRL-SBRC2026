# ============================================================
# SimplePolicy
# Simplified heuristic policy used only for
# demonstration and reproducibility purposes.
# ============================================================

import numpy as np


class SimplePolicy:
    """
    Simple heuristic policy used for artifact demonstration.

    This policy simulates adaptive control behavior without
    implementing a full DRL optimization strategy.
    """

    def __init__(self):
        """
        Initialize the simplified policy.
        """
        pass

    def predict(self, state):
        """
        Generate a simplified adaptive control action.

        Parameters:
            state (float or np.ndarray):
                Current network state or metric value.

        Returns:
            float or np.ndarray:
                Simulated adaptive control output.
        """
        # Simplified policy simulation
        return state * 0.95 + np.random.normal(0, 0.01)