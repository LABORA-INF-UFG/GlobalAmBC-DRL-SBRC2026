import pandas as pd
import matplotlib.pyplot as plt
import os

print("=== Generating Figure 3 ===")

# Caminho base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminhos possíveis
canonical_data_path = os.path.join(BASE_DIR, "data", "figure3_data.csv")
baseline_path = os.path.join(BASE_DIR, "results", "baseline", "results.csv")
drl_path = os.path.join(BASE_DIR, "results", "drl", "results.csv")

# Pasta de saída
figures_path = os.path.join(BASE_DIR, "figures")
os.makedirs(figures_path, exist_ok=True)

# ===============================
# Escolha do modo de reprodução
# ===============================
if os.path.exists(baseline_path) and os.path.exists(drl_path):
    print("✔ Using pipeline-generated data (results/)")

    df_baseline = pd.read_csv(baseline_path)
    df_drl = pd.read_csv(drl_path)

    # Garantir consistência de colunas
    df = pd.DataFrame({
        "time": df_baseline["time"],
        "success_rate_baseline": df_baseline["success_rate"],
        "success_rate_drl": df_drl["success_rate"]
    })

else:
    print("✔ Using canonical dataset (data/figure3_data.csv)")
    df = pd.read_csv(canonical_data_path)

# ===============================
# Suavização (mantido)
# ===============================
df["success_rate_drl"] = df["success_rate_drl"].rolling(window=3, min_periods=1).mean()

# ===============================
# Plot
# ===============================
plt.figure(figsize=(8, 5))

plt.plot(df["time"], df["success_rate_baseline"], label="Sem Controle DRL")
plt.plot(df["time"], df["success_rate_drl"], label="Com GlobalAmBC-DRL")

plt.xlabel("Tempo de simulação")
plt.ylabel("Taxa de Sucesso")

plt.legend(loc='lower left')
plt.grid()

# ===============================
# Limites do eixo Y (ajustável)
# ===============================
Y_MIN = 0.25
Y_MAX = 0.9
plt.ylim(Y_MIN, Y_MAX)

# ===============================
# Salvar figura
# ===============================
output_path = os.path.join(figures_path, "figure3.png")
plt.savefig(output_path)

print(f"✔ Figura gerada em: {output_path}")

plt.show()