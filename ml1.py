# Step 1: Import library
#from sklearn.linear_model import LinearRegression
import numpy as np

# Step 2: Create data
hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
marks = np.array([40, 50, 60, 70, 80])

# Step 3: Create model
model = LinearRegression()

# Step 4: Train model
model.fit(hours, marks)

# Step 5: Predict
predicted_marks = model.predict([[6]])

print("Predicted marks for 6 study hours:", predicted_marks[0])
