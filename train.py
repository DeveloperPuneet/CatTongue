import tensorless as tl

print("Pretraining base model...")
base_model = tl.pretrain(out="pretrained_base.tl", max_seq_len=30)
print("Base model pretrained -> pretrained_base.tl")

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
