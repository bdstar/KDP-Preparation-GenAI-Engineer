from sklearn.model_selection import cross_val_score, StratifiedKFold
import numpy as np
 
def cross_validate(model, X, y, folds=5, scoring="f1_macro"):
    cv = StratifiedKFold(n_splits=folds, shuffle=True, random_state=42)  # preserve class balance
    scores = cross_val_score(model, X, y, cv=cv, scoring=scoring)
    print(f"{scoring}: {scores.mean():.3f} ± {scores.std():.3f}  folds={np.round(scores, 3)}")
    return scores
