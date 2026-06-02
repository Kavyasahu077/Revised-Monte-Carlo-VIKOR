# Monte Carlo + Bayesian Network + VIKOR Risk Assessment Framework

## Overview

This project implements an integrated risk assessment and decision-support framework using:

* Monte Carlo Simulation
* Bayesian Network Inference
* VIKOR Multi-Criteria Decision Making (MCDM)

The framework evaluates the risk of different system components under uncertain operating conditions, with a particular focus on the impact of abnormal vibration on equipment reliability.

---

## Objectives

* Model uncertainty using Monte Carlo simulation.
* Estimate component failure risks using Bayesian reasoning.
* Rank components based on multiple risk criteria using VIKOR.
* Identify the most critical components requiring attention or maintenance.

---

## Project Structure

```text
project/
│
├── main.py
├── config.py
│
├── ahp/
│   ├── ahp_weights.py
│   └── __init__.py
│
├── bayesian/
│   ├── bn_model.py
│   └── __init__.py
│
├── data/
│   ├── generator.py
│   └── __init__.py
│
├── simulation/
│   ├── monte_carlo.py
│   └── __init__.py
│
├── vikor/
│   ├── vikor_engine.py
│   └── __init__.py
│
├── results_visualisation/
│   ├── plots.py
│   └── __init__.py
│
└── output/
```

---

## Methodology

### 1. Data Generation

Synthetic operational data is generated for:

* Pump
* Turbine
* Sensor
* Valve

Each component is assigned:

* Failure Probability
* Severity
* Detectability
* Vibration Level

### 2. Bayesian Risk Estimation

The Bayesian module adjusts component failure probabilities based on vibration influence, reflecting practical engineering behavior.

### 3. Monte Carlo Simulation

Thousands of simulations are executed to account for uncertainty and variability in risk parameters.

### 4. VIKOR Ranking

Components are ranked using:

* Failure Probability
* Severity
* Non-Detectability

Higher scores indicate greater overall risk.

---

## Output

The framework produces:

* Component risk rankings
* Risk score distributions
* Probability of being the highest-risk component
* Visualization plots

Example ranking:

```text
1. Turbine
2. Pump
3. Valve
4. Sensor
```

---

## Installation

Install required packages:

```bash
pip install -r requirement.txt
```

---

## Running the Project

```bash
python main.py
```

---

## Sample Results

The updated model reflects practical system behavior where abnormal vibration primarily impacts:

* Turbine (Highest Risk)
* Pump (High Risk)

while the Sensor remains the least affected component.

---

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib

---

## Future Improvements

* Real industrial datasets
* Full Bayesian Network CPT implementation
* Dynamic maintenance decision support
* Sensitivity and uncertainty analysis
* Additional MCDM techniques for comparison

---

## Author

**Kavya Sahu**

Developed as part of a probabilistic risk assessment and decision-support framework integrating Monte Carlo Simulation, Bayesian Inference, and VIKOR-based multi-criteria decision making.

---

## License

This project is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to the conditions of the MIT License.
