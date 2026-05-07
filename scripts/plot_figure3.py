import pandas as pd
import matplotlib.pyplot as plt
import os
import argparse

print("=== Generating Figure 3 ===")

# ============================================================
# Command-line arguments
# ============================================================
parser = argparse.ArgumentParser(
    description="Generate Figure 3 for the GlobalAmBC-DRL artifact."
)

parser.add_argument(
    "--ylim_min",
    type=float,
    default=0.25,
    help="Minimum value for Y-axis limit"
)

parser.add_argument(
    "--ylim_max",
    type=float,
    default=0.9,
    help="Maximum value for Y-axis limit"
)

args = parser.parse_args()

# ============================================================
# Base project directory
# ============================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ============================================================
# Possible data sources
# ============================================================
canonical_data_path = os.path.join(BASE_DIR, "data", "figure3_data.csv")
baseline_path = os.path.join(BASE_DIR, "results", "baseline", "results.csv")
drl_path = os.path.join(BASE_DIR, "results", "drl", "results.csv")

# ============================================================
# Output directory
# ============================================================
figures_path = os.path.join(BASE_DIR, "figures")
os.makedirs(figures_path, exist_ok=True)

# ============================================================
# Reproduction mode selection
# ============================================================
if os.path.exists(baseline_path) and os.path.exists(drl_path):
    print("✔ Using pipeline-generated data (results/)")

    df_baseline = pd.read_csv(baseline_path)
    df_drl = pd.read_csv(drl_path)

    # Ensure column consistency
    df = pd.DataFrame({
        "time": df_baseline["time"],
        "success_rate_baseline": df_baseline["success_rate"],
        "success_rate_drl": df_drl["success_rate"]
    })

else:
    print("✔ Using canonical dataset (data/figure3_data.csv)")
    df = pd.read_csv(canonical_data_path)

# ============================================================
# Smoothing
# ============================================================
df["success_rate_drl"] = (
    df["success_rate_drl"]
    .rolling(window=3, min_periods=1)
    .mean()
)

# ============================================================
# Plot
# ============================================================
plt.figure(figsize=(8, 5))

plt.plot(
    df["time"],
    df["success_rate_baseline"],
    label="Sem Controle DRL"
)

plt.plot(
    df["time"],
    df["success_rate_drl"],
    label="Com GlobalAmBC-DRL"
)

plt.xlabel("Tempo de simulação")
plt.ylabel("Taxa de Sucesso")

plt.legend(loc='lower left')
plt.grid()

# ============================================================
# Configurable Y-axis limits
# ============================================================
plt.ylim(args.ylim_min, args.ylim_max)

# ============================================================
# Save figure
# ============================================================
output_path = os.path.join(figures_path, "figure3.png")
plt.savefig(output_path)

print(f"✔ Figura gerada em: {output_path}")

plt.show()