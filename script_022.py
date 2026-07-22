from datasets import load_dataset
from transformers import (AutoTokenizer, AutoModelForSequenceClassification,
                          TrainingArguments, Trainer)
 
ds = load_dataset("imdb")
tok = AutoTokenizer.from_pretrained("distilbert-base-uncased")
 
def tokenize(batch):
    return tok(batch["text"], truncation=True, padding="max_length", max_length=256)
 
ds = ds.map(tokenize, batched=True)
small_train = ds["train"].shuffle(seed=42).select(range(2000))
small_eval = ds["test"].shuffle(seed=42).select(range(1000))
 
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased", num_labels=2)
 
args = TrainingArguments(output_dir="out", num_train_epochs=1,
                         per_device_train_batch_size=16,
                         learning_rate=2e-5, eval_strategy="epoch")
 
trainer = Trainer(model=model, args=args,
                  train_dataset=small_train, eval_dataset=small_eval)
trainer.train()
