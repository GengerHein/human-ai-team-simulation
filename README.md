# Human–AI Teamwork Simulation with Real Survey Data
This project simulates how different types of human agents (e.g., Engineering, Social Science, etc.) collaborate with AI systems during group decision-making tasks. The simulation uses real survey responses to model key factors such as trust in AI and flexibility in changing opinions.

## Repository Structure
human-ai-team-simulation/
├── data/
│   └── survey_cleaned.csv        # Cleaned survey dataset used for agent parameter initialization
├── scripts/
│   ├── run_simulation.py         # Main simulation script
│   └── utils.py                  # Helper functions for simulation (optional)
├── 01_clean_survey_data.ipynb    # Jupyter Notebook used for cleaning/processing survey data
├── README.md                     # Project overview and instructions

## How to Run the Simulation

Follow the steps below to run the opinion convergence simulation:

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/human-ai-team-simulation.git
cd human-ai-team-simulation

# Survey Simulation Project

This project analyzes and simulates response trends based on a cleaned survey dataset.

python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
pip install pandas numpy matplotlib

## Run the Simulation
cd scripts
python run_simulation.py

