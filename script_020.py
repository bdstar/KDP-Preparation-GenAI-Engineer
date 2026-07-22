from tokenizers import Tokenizer, models, trainers, pre_tokenizers
 
tokenizer = Tokenizer(models.BPE())
tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()
trainer = trainers.BpeTrainer(vocab_size=5000, special_tokens=["[UNK]", "[PAD]"])
tokenizer.train(["corpus.txt"], trainer)      # learns merges from your text
print(tokenizer.encode("subword tokenization").tokens)
