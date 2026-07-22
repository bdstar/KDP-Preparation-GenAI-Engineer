import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
 
X, y = fetch_california_housing(return_X_y=True)
X_train, X_tmp, y_train, y_tmp = train_test_split(X, y, test_size=0.30, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_tmp, y_tmp, test_size=0.50, random_state=42)
