import tensorless as tl

model = tl.load("cat.tl")

print("🐈 CatTongue is awake!")
print("Type 'exit' to leave.\n")

while True:
    user = input("You: ").strip()

    if user.lower() == "exit":
        print("Cat: mrrp... finally. 🐈")
        break

    prompt = f"Human: {user}\nCat:"

    response = model.generate(
        prompt,
        max_new_tokens=80,
    )

    # Remove the prompt if the model repeats it
    if response.startswith(prompt):
        response = response[len(prompt):]

    # Remove accidental conversation labels
    response = response.replace("Human:", "")
    response = response.replace("Cat:", "")
    response = response.replace("Cart:", "")

    response = response.strip()

    print(f"Cat: {response}\n")