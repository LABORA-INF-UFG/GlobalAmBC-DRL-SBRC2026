# Reproduction Guide – GlobalAmBC-DRL (SBRC 2026)

## 1. Objective

This document provides step-by-step instructions to reproduce **Figure 3** from the paper:

**"A New Centralized DRL-Based Control Module for Dense Batteryless IoT Networks with Ambient Backscatter"**

The figure compares the temporal behavior of the network success rate under two scenarios:

* Baseline (no control)
* With GlobalAmBC-DRL

---

## 2. Repository Structure

The repository is organized as follows:

```
GlobalAmBC-DRL-SBRC2026/
│
├── data/        # Input datasets
├── scripts/     # Execution pipeline
├── results/     # Generated outputs
├── figures/     # Final figure
├── docs/        # Documentation
```

---

## 3. Requirements

### 3.1 System Requirements

* Operating System: Windows, Linux, or macOS
* Python: version 3.8 or higher

### 3.2 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Reproduction Steps

### Step 1 – Extract metrics

```bash
python scripts/extract_metrics.py
```

This step processes the raw dataset:

```
data/raw/omnetpp_output.csv
```

and generates:

```
data/processed/processed_results.csv
```

---

### Step 2 – Run DRL module

```bash
python scripts/run_drl.py
```

This step generates:

```
results/baseline/results.csv
results/drl/results.csv
```

---

### Step 3 – Generate Figure 3

```bash
python scripts/plot_figure3.py
```

This step produces:

```
figures/figure3.png
```

---

## 5. One-Command Execution

Alternatively, the full pipeline can be executed with:

```bash
./run_experiment.sh
```

---

## 6. Expected Output

After execution, the following files must exist:

* `data/processed/processed_results.csv`
* `results/baseline/results.csv`
* `results/drl/results.csv`
* `figures/figure3.png`

---

## 7. Expected Results

The generated figure should present:

### Baseline (no control)

* Higher variability
* Frequent oscillations
* Lower average performance

### GlobalAmBC-DRL

* Reduced variability
* More stable behavior
* Higher average success rate

---

## 8. Notes on Reproducibility

* The dataset `figure3_data.csv` is provided to ensure deterministic reproduction of the published figure.
* The DRL module is included to demonstrate the pipeline structure and system behavior.
* The results preserve the relative performance trends observed in the original paper.

---

## 9. Execution Time

Expected runtime: less than 5 seconds.

---

## 10. Scope of Reproducibility

This artifact reproduces:

* The behavior of Figure 3
* The impact of centralized DRL control

This artifact does NOT require:

* OMNeT++ installation
* Full DRL training process

---

## 11. Troubleshooting

### Issue: ModuleNotFoundError (drl_agent)

Run scripts from the root directory:

```bash
python scripts/run_drl.py
```

---

### Issue: Missing results files

Ensure Step 2 was executed before plotting.

---

### Issue: Figure not generated

Verify all previous steps were executed successfully.

---

## 12. Contact

Edwardes A. Galhardo
[edwardesamarogalhardo@inf.ufg.br](mailto:edwardesamarogalhardo@inf.ufg.br)
