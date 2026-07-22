from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt
 
def plot_roc(y_true, y_scores):
    fpr, tpr, thresholds = roc_curve(y_true, y_scores)     # scores, not hard labels
    auc = roc_auc_score(y_true, y_scores)
    plt.plot(fpr, tpr, label=f"AUC = {auc:.3f}")
    plt.plot([0, 1], [0, 1], "--", color="grey", label="chance")
    plt.xlabel("False positive rate"); plt.ylabel("True positive rate")
    plt.legend(); plt.show()
    return auc, thresholds
