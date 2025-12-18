import pandas as pd

# Load raw data
df = pd.read_csv("leads.csv")

# Convert Probability_Score to numeric (invalid → NaN)
if "Probability_Score" in df.columns:
    df["Probability_Score"] = pd.to_numeric(
        df["Probability_Score"], errors="coerce"
    )
    df = df.sort_values("Probability_Score", ascending=False)

# Fill remaining NaNs for display
df = df.fillna("N/A")


# Save output
df.to_csv("output_leads.csv", index=False)

print("Output generated: output_leads.csv")
