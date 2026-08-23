import tensorless as tl
model = tl.pretrain(out="english.tl", max_seq_len=40)
model = tl.train(
    "data/conversations.json",
    task="text-generation",
    out="cat.tl",
)

print("CatTongue trained successfully!")