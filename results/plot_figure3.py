import pandas as pd
import matplotlib.pyplot as plt
import os

# Garantir caminhos absolutos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "data", "figure3_data.csv")
figures_path = os.path.join(BASE_DIR, "figures")

# Criar pasta figures se não existir
os.makedirs(figures_path, exist_ok=True)

# Carregar dados
df = pd.read_csv(data_path)

# Plot
plt.figure()
plt.plot(df["time"], df["success_no_control"], label="Sem Controle")
plt.plot(df["time"], df["success_drl"], label="GlobalAmBC-DRL")

plt.xlabel("Tempo")
plt.ylabel("Taxa de Sucesso")
plt.title("Comportamento Temporal da Taxa de Sucesso")
plt.legend()
plt.grid()

# Salvar figura
output_path = os.path.join(figures_path, "figure3.png")
plt.savefig(output_path)

print(f"Figura gerada em: {output_path}")

plt.show()