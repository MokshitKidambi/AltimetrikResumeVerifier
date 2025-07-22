import pandas as pd

df = pd.read_csv("UpdatedResumeDataSet.csv")  # Your actual filename

# Extract the 'Resume' column
texts = df['Resume']

real_df = pd.DataFrame({
    "text": texts,
    "label": "real"
})

print(real_df.head())

real_df.to_csv("real_resumes.csv", index=False)
print("Saved real_resumes.csv")
