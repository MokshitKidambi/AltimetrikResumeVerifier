import pandas as pd

fake_df = pd.read_csv("fake_resumes.csv")
real_df = pd.read_csv("real_resumes.csv")

combined_df = pd.concat([fake_df, real_df], ignore_index=True)
combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)

combined_df.to_csv("resume_dataset.csv", index=False)
print("Combined dataset saved as resume_dataset.csv")
