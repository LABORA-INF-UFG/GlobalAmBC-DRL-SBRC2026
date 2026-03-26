import os
import subprocess

print("=== GlobalAmBC-DRL SBRC 2026 Artifact ===\n")

print("1) Gerando dados...")
subprocess.run(["python", "generate_data.py"], cwd=os.path.dirname(__file__))

print("\n2) Gerando gráfico...")
subprocess.run(["python", "plot_figure3.py"], cwd=os.path.dirname(__file__))

print("\n✔ Experimento concluído!")
print("Figura disponível em: figures/figure3.png")