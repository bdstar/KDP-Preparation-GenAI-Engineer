from transformers import AutoTokenizer, AutoModelForSequenceClassification
 
class SentimentClassifier:
    def __init__(self, model_name: str):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
 
    def predict(self, text: str) -> str:
        inputs = self.tokenizer(text, return_tensors="pt")
        logits = self.model(**inputs).logits
        label_id = int(logits.argmax(dim=-1))
        return self.model.config.id2label[label_id]
from_pretrained__init____repr____len__
