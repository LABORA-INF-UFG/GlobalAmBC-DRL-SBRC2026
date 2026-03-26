import pandas as pd
import matplotlib.pyplot as plt
import os

print("=== Generating Figure 3 (from article data) ===")

# Caminho base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminho do dataset da figura (dados do artigo)
data_path = os.path.join(BASE_DIR, "data", "figure3_data.csv")

# Pasta de saída da figura
figures_path = os.path.join(BASE_DIR, "figures")
os.makedirs(figures_path, exist_ok=True)

# Carregar dados
df = pd.read_csv(data_path)

df["success_rate_drl"] = df["success_rate_drl"].rolling(window=3, min_periods=1).mean()

# Plot
plt.figure(figsize=(8, 5))

plt.plot(df["time"], df["success_rate_baseline"], label="Sem Controle DRL")
plt.plot(df["time"], df["success_rate_drl"], label="Com GlobalAmBC-DRL")

plt.xlabel("Tempo de simulação")
plt.ylabel("Taxa de Sucesso")
#plt.title("Comportamento Temporal da Taxa de Sucesso")

plt.legend(loc='lower left')
plt.grid()

plt.ylim(0.25, 0.9)

# Salvar figura
output_path = os.path.join(figures_path, "figure3.png")
plt.savefig(output_path)

print(f"Figura gerada em: {output_path}")

plt.show()