import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import pandas as pd
import numpy as np

from drl_agent.ddpg import DDPGAgent

print("=== Running DRL ===")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminhos
input_path = os.path.join(BASE_DIR, "data", "processed", "processed_results.csv")

baseline_output = os.path.join(BASE_DIR, "results", "baseline", "results.csv")
drl_output = os.path.join(BASE_DIR, "results", "drl", "results.csv")

# Criar pastas se não existirem
os.makedirs(os.path.dirname(baseline_output), exist_ok=True)
os.makedirs(os.path.dirname(drl_output), exist_ok=True)

# Ler dados processados
df = pd.read_csv(input_path)

# BASELINE = dados originais
baseline_df = df.copy()
baseline_df.to_csv(baseline_output, index=False)

# DRL
agent = DDPGAgent()

success_values = df["success_rate"].values

# Simular ação do DRL
drl_values = agent.run(success_values)

# Garantir que valores fiquem entre 0 e 1
drl_values = np.clip(drl_values, 0, 1)

drl_df = df.copy()
drl_df["success_rate"] = drl_values

drl_df.to_csv(drl_output, index=False)

print(f"Baseline saved at: {baseline_output}")
print(f"DRL results saved at: {drl_output}")