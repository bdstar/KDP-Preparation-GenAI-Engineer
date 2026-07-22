from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
 
def rmse(model, X, y):
    return mean_squared_error(y, model.predict(X)) ** 0.5
 
linear = LinearRegression().fit(X_train, y_train)
boosted = GradientBoostingRegressor(random_state=42).fit(X_train, y_train)
 
for name, m in [("linear", linear), ("boosted", boosted)]:
    print(f"{name}: train RMSE {rmse(m, X_train, y_train):.3f} | val RMSE {rmse(m, X_val, y_val):.3f}")
