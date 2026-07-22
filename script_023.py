trainer.save_model("my-sentiment-model")
finetuned = pipeline("sentiment-analysis", model="my-sentiment-model", tokenizer=tok)
print(finetuned("An absolute masterpiece, beautifully acted."))
