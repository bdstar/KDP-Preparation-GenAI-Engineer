best = GradientBoostingRegressor(max_depth=4, random_state=42).fit(X_train, y_train)
print(f"FINAL test RMSE: {rmse(best, X_test, y_test):.3f}")
tradeoff.png
