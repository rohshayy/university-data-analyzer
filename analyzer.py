import pandas as pd

#Load the data
df=pd.read_csv("mock_student_data.csv")
print(df.to_string())

# 1. Calculate and print the Mean for each subject (for your reference)
print("Mean Scores (Before Filling)")
print(f"Calculus: {df["Calculus"].mean():.2f}")
print(f"LA: {df["Linear_Algebra"].mean():.2f}")
print(f"PF: {df["Programming_Fundamentals"].mean():.2f}")
print(f"NC: {df["Numerical_Computing"].mean():.2f}")

# 2. Fill missing values with the Median
# Logic: We use Median because it is robust against outliers (like Student 108).
# While a Mean would be skewed by very low or very high scores,
# the Median represents the 'typical' student performance more accurately.
df["Calculus"] = df["Calculus"].fillna(df["Calculus"].median())
df["Linear_Algebra"] = df["Linear_Algebra"].fillna(df["Linear_Algebra"].median())
df["Programming_Fundamentals"] = df["Programming_Fundamentals"].fillna(df["Programming_Fundamentals"].median())
df["Numerical_Computing"] = df["Numerical_Computing"].fillna(df["Numerical_Computing"].median())
print("Data After Filling Missing Values")
print(df.to_string())



# 3. Filter out any rows that are still incomplete
# (e.g., Row 110 which might have had too many NaN values to be useful)
df_cleaned=df.dropna()
print("Cleaned Data (Missing Values Filled with Median)")
print(df_cleaned.to_string())


# Save the cleaned data for your GitHub project
df_cleaned.to_csv("cleaned_student_data.csv", index=False)