import tensorless as tl

# Step 1: Pretrain a base language model on Tensorless's built-in English
# starter corpus. Uses Tensorless's own defaults -- no architecture or
# tokenizer overrides.
print("Pretraining base model...")
base_model = tl.pretrain(out="pretrained_base.tl")
print("Base model pretrained -> pretrained_base.tl")

# Step 2: Fine-tune the pretrained model on CatTongue's conversations.
# epochs is raised and val_split is disabled because conversations.json
# is small and stylistically repetitive (short lines, lots of emoji) --
# with the default epoch count and a validation split, early stopping was
# triggering long before the model had actually learned the cat's voice,
# which is why generations were coming out as gibberish.
print("Fine-tuning on cat conversations...")
model = tl.train(
    "data/conversations.json",
    task="text-generation",
    pretrained="pretrained_base.tl",
    out="cat.tl",
    epochs=150,
    val_split=0.0,
)

print("CatTongue trained successfully!")
