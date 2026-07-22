from transformers import pipeline
 
clf = pipeline("sentiment-analysis")
print(clf("This film was a complete waste of time."))
# [{'label': 'NEGATIVE', 'score': 0.9997}]
