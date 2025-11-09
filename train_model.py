import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

print("Starting model training...")

# 1. Create our smart training data, based on the REAL data you provided.
# We will use all 7 features:
# - student_percent (Score)
# - relative_to_avg (Score - Avg)
# - relative_to_max (Max - Score)
# - ia1_percent
# - ia2_percent
# - quiz_percent
# - aat_percent
#
# (Max marks: IA1: 20, IA2: 20, Quiz: 10, AAT: 20, Total: 70)
data = {
    # Sub 1 (Calculus): Score: 89%, Avg: 76.4%, Max: 96% | IAs: 20, 19, 8, 15
    'student_percent': [89, 91, 81, 86, 87], 
    'relative_to_avg': [12.6, 16.5, 4.1, 9.1, 10.3], # (e.g., 89 - 76.4 = 12.6)
    'relative_to_max': [7, 0, 10, 5, 0],             # (e.g., 96 - 89 = 7)
    'ia1_percent': [100, 90, 80, 95, 100],           # (e.g., 20/20 = 100%)
    'ia2_percent': [95, 85, 90, 95, 75],             # (e.g., 19/20 = 95%)
    'quiz_percent': [80, 90, 80, 80, 80],            # (e.g., 8/10 = 80%)
    'aat_percent': [75, 100, 75, 70, 90],            # (e.g., 15/20 = 75%)
    'priority': ['Low', 'Low', 'Low', 'Low', 'Low']  # All are 'Low' because the student is doing well
}

# To make the model useful, we MUST add examples of 'Medium' and 'High' priority.
# Let's add two hypothetical "weak" subjects to teach the model.
new_data = {
    # Hypothetical "Medium" subject
    'student_percent': [65], 
    'relative_to_avg': [-10.0],  # 65% vs 75% avg
    'relative_to_max': [25.0],   # 65% vs 90% max
    'ia1_percent': [90],         # Good IA1
    'ia2_percent': [40],         # Bad IA2
    'quiz_percent': [70],
    'aat_percent': [60],
    'priority': ['Medium']
}

# Hypothetical "High" priority subject
new_data_2 = {
    'student_percent': [42], 
    'relative_to_avg': [-33.0],  # 42% vs 75% avg
    'relative_to_max': [48.0],   # 42% vs 90% max
    'ia1_percent': [50],
    'ia2_percent': [30],
    'quiz_percent': [40],
    'aat_percent': [50],
    'priority': ['High']
}

df = pd.DataFrame(data)
df = pd.concat([df, pd.DataFrame(new_data)], ignore_index=True)
df = pd.concat([df, pd.DataFrame(new_data_2)], ignore_index=True)

print("--- Training Data ---")
print(df)
print("---------------------")

# 2. Define our Features (X) and Target (y)
features = ['student_percent', 'relative_to_avg', 'relative_to_max', 'ia1_percent', 'ia2_percent', 'quiz_percent', 'aat_percent']
X = df[features] # The 7 input features
y = df['priority'] # The 1 output label

# 3. Create and Train the Decision Tree model
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X, y)

print("Model trained successfully on YOUR 7 features!")

# 4. Save the trained model to a file
joblib.dump(model, 'priority_model.joblib')

print("Model saved as 'priority_model.joblib'")
print("You can now run the main server.")