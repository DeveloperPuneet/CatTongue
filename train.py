import tensorless as tl

model = tl.train(
    "data/conversations.json",
    task="text-generation",
    out="cat.tl",
    epochs=10,
)

print("CatTongue trained successfully!")