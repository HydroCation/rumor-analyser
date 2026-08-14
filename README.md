# Dynamic Rumour Spread Network Analyser

A discrete-event network simulation engine and analysis framework modeling information diffusion, misinformation propagation, and rumor contagion across complex social network topologies.

---

## 📌 Overview

This project simulates how rumors and information cascade through social networks using stochastic epidemic-diffusion models (SIR / ISR frameworks) mapped onto synthetic scale-free and complex graph structures. It evaluates the impact of network topology, influential seed spreaders, and stifling thresholds on total information reach and velocity.

---

## 🔬 Key Features

* **Network Topology Generation (`graph_utils.py`):**
  * **Scale-Free Networks:** Barabási-Albert preferential attachment graph generation modeling real-world power-law degree distributions.
  * **Node Centrality & Hub Identification:** Degree, Betweenness, and Closeness centrality metrics for seed selection.
* **Contagion & Rumor Dynamics (`simulator.py`):**
  * **Susceptible-Infected-Recovered (SIR) / Spreader-Stifler Dynamics:** Probabilistic transmission state machines modeling belief adoption and skepticism.
  * **Configurable Transmission Rates:** Dynamic control over spreading probability ($\beta$) and stifling/skepticism decay rate ($\gamma$).
* **Exploratory Analysis & Visualization (`rumor_model_dev.ipynb`):**
  * Step-by-step contagion cascade tracking.
  * Time-series curves for adoption rates, peak infection, and total reach.

---

## 📐 Mathematical Model & State Dynamics

The propagation dynamics follow a discrete-time stochastic Markovian state transition:

$$\begin{aligned}
S + I &\xrightarrow{\ \beta\ } 2I \quad\text{(Susceptible node adopts rumor from an Infected neighbor)} \\
I + R &\xrightarrow{\ \gamma\ } 2R \quad\text{(Spreader becomes Stifler upon encountering informed/skeptical node)} \\
I + I &\xrightarrow{\ \gamma\ } I + R \quad\text{(Spreader ceases diffusion upon contact with another spreader)}
\end{aligned}$$

* **$\beta$ (Transmission Rate):** Probability of rumor adoption per contact edge.
* **$\gamma$ (Stifling / Recovery Rate):** Probability of transitioning to a passive/stifler state.

---

## 📂 Repository Structure
```
├── src/
│   ├── init.py           # Package initialization
│   ├── config.py             # Global simulation parameters & hyperparameters
│   ├── graph_utils.py        # Graph generators & centrality calculation utilities
│   ├── simulator.py          # Discrete-event propagation engine
│   └── rumor_model_dev.ipynb # Interactive simulation runs & visualization
├── .gitignore                # Git ignore configuration
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.x
* **Network & Graph Modeling:** NetworkX
* **Data Processing & Scientific Computing:** NumPy, SciPy, Pandas
* **Visualization:** Matplotlib, Seaborn

---

## 🚀 Setup & Execution

### 1. Installation
```bash
git clone [https://github.com/HydroCation/rumor-analyser.git](https://github.com/HydroCation/rumor-analyser.git)
cd rumor-analyser
pip install -r requirements.txt
```
### 2. Run Interactive Simulation
Launch the development notebook to execute graph generation and observe propagation cascades:
```bash
jupyter notebook src/rumor_model_dev.ipynb
```
