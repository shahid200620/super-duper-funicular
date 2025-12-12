import pandas as pd
import numpy as np

np.random.seed(42)
n = 300

age = np.random.randint(20, 80, n)
weight = np.random.randint(45, 110, n)
height = np.random.randint(150, 190, n)
systolic = np.random.randint(100, 180, n)
diastolic = np.random.randint(60, 110, n)
cholesterol = np.random.randint(150, 300, n)
glucose = np.random.randint(70, 200, n)
smoker = np.random.randint(0, 2, n)
exercise = np.random.randint(1, 6, n)
comorbidity = np.random.randint(0, 5, n)
treatment = np.random.choice(["A", "B"], n)

# Outcome logic (some realism)
outcome = (
    (age < 60).astype(int)
    + (systolic < 140).astype(int)
    + (cholesterol < 220).astype(int)
    + (exercise > 2).astype(int)
)
outcome = (outcome >= 2).astype(int)

df = pd.DataFrame({
    "age": age,
    "weight": weight,
    "height": height,
    "systolic": systolic,
    "diastolic": diastolic,
    "cholesterol": cholesterol,
    "glucose": glucose,
    "smoker": smoker,
    "exercise_level": exercise,
    "comorbidity_score": comorbidity,
    "treatment_type": treatment,
    "outcome": outcome
})

df.to_csv("health_data.csv", index=False)
print("health_data.csv created!")
