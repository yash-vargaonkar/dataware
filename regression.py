import pandas as pd
import numpy as np

x = 27

df = pd.DataFrame({
    'X': [5, 7, 12, 16, 20],
    'Y': [40, 120, 180, 210, 240]
})

mean_X = df['X'].mean()
mean_Y = df['Y'].mean()

# Calculate a and b
df['a'] = df['X'] - mean_X
df['b'] = df['Y'] - mean_Y

# Calculate a*b and a^2
df['a*b'] = df['a'] * df['b']
df['a^2'] = df['a'] ** 2

# Calculate sums
sum_ab = df['a*b'].sum()
sum_aa = df['a^2'].sum()

# Calculate w1 and w0
w1 = sum_ab / sum_aa
w0 = mean_Y - w1 * mean_X

# Estimated value of y for x = 27
y = w0 + w1 * x

print(f"Estimated value of y for x={x} is {y:.2f}")