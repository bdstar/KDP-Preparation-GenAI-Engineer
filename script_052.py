# Evaluate on your held-out set with the metrics from Chapter 7, and spot-check
# general capability so specialization hasn't caused catastrophic forgetting.
merged = trainer.model.merge_and_unload()   # fold adapters in for zero-overhead serving
merged.save_pretrained("./my-domain-assistant")
tok.save_pretrained("./my-domain-assistant")
