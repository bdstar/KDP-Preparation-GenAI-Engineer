from transformers import pipeline
 
classifier = pipeline("sentiment-analysis")
print(classifier("Hugging Face makes NLP wonderfully accessible!"))
# [{'label': 'POSITIVE', 'score': 0.9998}]
AutoTokenizerAutoModelAutoTokenizer
load_dataset("imdb")
