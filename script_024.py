from sklearn.metrics import confusion_matrix, classification_report
 
def report_classification(y_true, y_pred, labels=None):
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    print("Confusion matrix (rows = true, cols = predicted):\n", cm)
    # Per-class precision/recall/F1 — never trust a single averaged number.
    print(classification_report(y_true, y_pred, target_names=labels, digits=3))
    return cm
