import tensorless as tl

base_model = tl.pretrain(out="pretrained_base.tl", epochs=70)

model = tl.train(
    "data/conversations.json",
    task="text-generation",
    pretrained="pretrained_base.tl",
    out="cat.tl",
    epochs=70
)

print("CatTongue trained successfully!")
