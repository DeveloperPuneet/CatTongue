import tensorless as tl

model = tl.load("cat.tl")

print("🐈 CatTongue is awake!")
print("Type 'exit' to leave.\n")

while True:
    user = input("You: ").strip()

    if user.lower() == "exit":
        print("Cat: mrrp... finally. 🐈")
        break

    if not user:
        continue

    prompt = f"Human: {user}\nCat:"

    # Keep generating until we get something
    while True:
        response = model.generate(
            prompt,
            max_new_tokens=80,
        )

        if response.startswith(prompt):
            response = response[len(prompt):]

        response = response.strip()

        if "Human:" in response:
            response = response.split("Human:", 1)[0].strip()

        if response.startswith("Cat:"):
            response = response[4:].strip()

        # Empty → generate again
        if response == "":
            continue

        # Got a response → leave retry loop
        break

    print(f"Cat: {response}\n")