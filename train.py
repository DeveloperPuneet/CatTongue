import tensorless as tl

model = tl.train(
    "data/conversations.json",
    task="text-generation",
    out="cat.tl",
)

print("CatTongue trained successfully!")