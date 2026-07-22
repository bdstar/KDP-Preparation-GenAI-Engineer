def evaluate(model, X_train, X_test, y_train, y_test, labels=None):
    cross_validate(model, X_train, y_train)                 # generalization + variance
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report_classification(y_test, y_pred, labels)           # per-class truth
    if hasattr(model, "predict_proba"):                     # threshold-independent view
        plot_roc(y_test, model.predict_proba(X_test)[:, 1])
    return model
