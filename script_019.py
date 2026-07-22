from transformers import AutoTokenizer
 
tok = AutoTokenizer.from_pretrained("bert-base-uncased")
print(tok.tokenize("Tokenization handles unseen words gracefully."))
# ['token', '##ization', 'handles', 'un', '##seen', 'words', 'gracefully', '.']
