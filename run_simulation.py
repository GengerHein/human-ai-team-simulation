import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('../data/survey_cleaned.csv')

# Simulation logic
def simulate_response_change(df, rounds=10, decay=0.9):
    columns = ['Engineering', 'Social Science', 'Computer Science', 'Other']
    simulation = pd.DataFrame(columns=['round'] + columns)
    initial_values = [df[col].mean() for col in columns]

    for r in range(1, rounds + 1):
        values = [val * (decay ** (r - 1)) for val in initial_values]
        simulation = simulation.append(dict(round=r, **dict(zip(columns, values))), ignore_index=True)

    return simulation

# Run and save simulation
simulation_df = simulate_response_change(df)
simulation_df.to_csv('../data/simulation_output.csv', index=False)
print("Simulation complete. Results saved to /data/simulation_output.csv")
