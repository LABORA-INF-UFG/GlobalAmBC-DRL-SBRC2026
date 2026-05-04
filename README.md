# GlobalAmBC-DRL: SBRC 2026 Artifact

## Overview

This repository provides the experimental artifact for the paper:

**"A New Centralized DRL-Based Control Module for Dense Batteryless IoT Networks with Ambient Backscatter"**

The goal of this artifact is to enable reproducibility of the main results presented in the paper, particularly the temporal behavior of the network success rate under different control strategies.

---

## Artifact Goals

This artifact reproduces the behavior presented in **Figure 3**, demonstrating:

- Instability in networks without control (baseline)
- Stabilization using the GlobalAmBC-DRL module

---

## Repository Structure

```
GlobalAmBC-DRL-SBRC2026/
│
├── data/        # Input datasets
├── scripts/     # Execution pipeline
├── drl_agent/   # DRL components (DDPG-like structure)
├── results/     # Generated outputs
├── figures/     # Final figures
├── docs/        # Documentation
```

---

## Artifact Evaluation Badges

This artifact targets the following badges:

- Artifacts Available (SeloD)
- Artifacts Functional (SeloF)
- Artifacts Reproduced (SeloR)
- Artifacts Sustainable (SeloS)

---

## Basic Information

The artifact can be executed on standard environments:

- Operating System: Windows, Linux, or macOS
- Python: version 3.8 or higher
- RAM: at least 2 GB
- Disk: minimal (<100 MB)

---

## Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Dependencies include:

- pandas==2.0.3
- numpy==1.24.4
- matplotlib==3.7.2

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/LABORA-INF-UFG/GlobalAmBC-DRL-SBRC2026
cd GlobalAmBC-DRL-SBRC2026
pip install -r requirements.txt
```

---

## Minimal Test

To verify that the artifact is working correctly, run:

```bash
python scripts/plot_figure3.py
```

Expected result:

- File `figures/figure3.png` is generated
- A plot comparing baseline vs GlobalAmBC-DRL is displayed

---

## Experiments

### Claim 1 – Reproduction of Figure 3

To reproduce the main result of the paper:

```bash
bash run_experiment.sh
```

Or manually:

```bash
python scripts/extract_metrics.py
python scripts/run_drl.py
python scripts/plot_figure3.py
```

---

## Reproduction Modes

This artifact supports two modes of reproduction:

### 1. Canonical Reproduction (Default)

Uses the pre-processed dataset:

```
data/figure3_data.csv
```

This mode ensures **deterministic reproduction** of Figure 3 exactly as presented in the paper.

---

### 2. Pipeline-Based Reproduction

Runs the full processing pipeline:

```bash
python scripts/extract_metrics.py
python scripts/run_drl.py
```

This generates:

```
results/baseline/results.csv
results/drl/results.csv
```

These results can also be used for plotting, demonstrating the workflow of the system.

---

### Mode Selection

The script:

```bash
python scripts/plot_figure3.py
```

automatically selects:

- Pipeline data (if available)
- Otherwise, the canonical dataset

This design ensures both reproducibility and demonstration of the processing pipeline.

---

## Expected Output

After execution, the following files should be generated:

```
data/processed/processed_results.csv
results/baseline/results.csv
results/drl/results.csv
figures/figure3.png
```

---

## Expected Results

The generated figure should present:

### Baseline (no control)

- High variability
- Frequent oscillations
- Lower average performance

### GlobalAmBC-DRL

- Reduced variability
- More stable behavior
- Higher average success rate

---

## Security Considerations

This artifact does not pose any security risks:

- No external network access
- No privileged system operations
- No destructive actions

---

## Documentation

Detailed reproduction steps are available in:

```
docs/reproduction_steps.md
```

---

## Notes

- The dataset `data/figure3_data.csv` is provided as the **canonical dataset** to ensure deterministic and reproducible generation of Figure 3.

- The pipeline scripts (`extract_metrics.py` and `run_drl.py`) demonstrate the workflow of the system and generate intermediate results.

- The plotting script (`plot_figure3.py`) supports both:
  - Direct reproduction from the canonical dataset
  - Visualization using pipeline-generated results

- The DRL module included in this artifact is a **simplified DRL-inspired policy**, designed for demonstration purposes only, and does not represent a full DDPG implementation.

- This artifact reproduces the **qualitative behavior** of the original experiments without requiring OMNeT++ execution or full DRL training.

---

## Limitations

- The DRL agent is a simplified implementation designed for demonstration and reproducibility purposes.

- The artifact does not include a full OMNeT++ simulation environment.

- The canonical dataset is used to ensure deterministic reproduction of results.

- The pipeline demonstrates system behavior but is not intended to replicate the full experimental complexity of the original study.

---

## Final Remarks

This artifact was designed to ensure clarity, simplicity, and reproducibility, enabling reviewers to validate the main claims of the paper with minimal effort.

---

## Citation

If you use this artifact, please cite the associated paper:

```bibtex
@inproceedings{galhardo2026globalambc,
  title={Um Novo Módulo Arquitetural de Controle Centralizado com DRL para Redes IoT Densas sem Bateria Baseadas em Retroespalhamento Ambiente},
  author={Galhardo, Edwardes Amaro and Oliveira Junior, Antonio Carlos and Westphall, Carlos Becker},
  booktitle={Simpósio Brasileiro de Redes de Computadores e Sistemas Distribuídos (SBRC)},
  year={2026}
}
```

You may also cite this artifact as:

```bibtex
@misc{galhardo2026artifact,
  title={GlobalAmBC-DRL: Reproducible Artifact for Dense Batteryless IoT Networks with Ambient Backscatter},
  author={Galhardo, Edwardes Amaro},
  year={2026},
  howpublished={\url{https://github.com/LABORA-INF-UFG/GlobalAmBC-DRL-SBRC2026}},
  note={Public research artifact}
}
```

---

## License

This project is licensed under the MIT License.