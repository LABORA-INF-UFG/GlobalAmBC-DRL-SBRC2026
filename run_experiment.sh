echo "=============================="
echo "GlobalAmBC-DRL SBRC 2026 Pipeline"
echo "=============================="

echo "[1] Extracting metrics..."
python scripts/extract_metrics.py

echo "[2] Running DRL..."
python scripts/run_drl.py

echo "[3] Generating Figure 3..."
python scripts/plot_figure3.py

echo "=============================="
echo "Done."
echo "Figure available at: figures/figure3.png"
echo "=============================="