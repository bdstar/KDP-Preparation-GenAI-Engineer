from peft import LoraConfig
 
lora = LoraConfig(
    r=16, lora_alpha=32,                 # alpha ~= 2 * r
    target_modules="all-linear",         # adapt all linear layers
    lora_dropout=0.05,
    task_type="CAUSAL_LM",
    # use_dora=True,                      # optional: the DoRA refinement
)
