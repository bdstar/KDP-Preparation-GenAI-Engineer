from trl import SFTTrainer, SFTConfig
 
cfg = SFTConfig(
    learning_rate=2e-4,                  # adapters tolerate a higher LR
    num_train_epochs=2,                  # few epochs — watch validation loss
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,       # effective batch of 8
    bf16=True,
)
trainer = SFTTrainer(model=model, args=cfg, peft_config=lora,
                     train_dataset=train_ds, eval_dataset=val_ds)
trainer.train()
