import pandas as pd
import scipy.stats as stats

# Read the data
with open("stat_result.txt", "r") as f:
    lines = f.readlines()

# Parse the data
data = []
for line in lines:
    parts = line.strip().split(" ")
    data.append(
        {
            "qp": int(parts[1].split("=")[1]),
            "ref": int(parts[2].split("=")[1]),
            "subme": int(parts[3].split("=")[1]),
            "threads": int(parts[4].split("=")[1]),
            "input_file": int(parts[5].split("=")[1]),
            "status": parts[6].split("=")[1].strip("'"),
        }
    )

# Create a DataFrame
df = pd.DataFrame(data)

# Perform a chi-square test of independence for each parameter
parameters = ["qp", "ref", "subme", "threads", "input_file"]
for param in parameters:
    contingency_table = pd.crosstab(df[param], df["status"])
    chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
    print(f"Parameter: {param}, Chi-square: {chi2}, p-value: {p}")
