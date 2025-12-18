import pandas as pd

# Load raw data
df = pd.read_csv("leads.csv")

# Clean missing values
df = df.fillna("N/A")

# Sort by probability score
if "Probability_Score" in df.columns:
    df = df.sort_values("Probability_Score", ascending=False)

# Export final output
df.to_csv("output_leads.csv", index=False)

print("Output generated: output_leads.csv")
