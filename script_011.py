import matplotlib.pyplot as plt
 
depths = range(1, 12)
train_err, val_err = [], []
for d in depths:
    m = GradientBoostingRegressor(max_depth=d, random_state=42).fit(X_train, y_train)
    train_err.append(rmse(m, X_train, y_train))
    val_err.append(rmse(m, X_val, y_val))
 
plt.plot(list(depths), train_err, label="train")
plt.plot(list(depths), val_err, label="validation")
plt.xlabel("tree depth (model complexity)"); plt.ylabel("RMSE"); plt.legend()
plt.title("Bias-variance trade-off"); plt.savefig("tradeoff.png", dpi=150)
alpha
from sklearn.linear_model import Ridge
 
for alpha in [0.0, 1.0, 10.0, 100.0]:
    m = Ridge(alpha=alpha).fit(X_train, y_train)
    print(f"alpha={alpha:6.1f} | train {rmse(m, X_train, y_train):.3f} | val {rmse(m, X_val, y_val):.3f}")
