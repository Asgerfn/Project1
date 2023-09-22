import pandas as pd

sti = "C:\\Users\\Asger Nielsen\\firms.csv"
df = pd.read_csv(sti)


desired_years = [1968, 1969, 1970]
mask = df['year'].isin(desired_years)

filtered_df = df[mask]

print(filtered_df)
