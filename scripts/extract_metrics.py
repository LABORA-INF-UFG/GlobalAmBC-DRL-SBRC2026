import os
import pandas as pd

print("=== Extracting metrics from raw data ===")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

raw_path = os.path.join(BASE_DIR, "data", "raw", "omnetpp_output.csv")
processed_path = os.path.join(BASE_DIR, "data", "processed", "processed_results.csv")

# Criar pasta se não existir
os.makedirs(os.path.dirname(processed_path), exist_ok=True)

# Ler dados brutos
df = pd.read_csv(raw_path)

# Calcular taxa de sucesso
df["success_rate"] = df["received"] / df["sent"]

# Salvar processado
df.to_csv(processed_path, index=False)

print(f"Processed data saved at: {processed_path}")