# 🐈 CatTongue

A tiny talking-cat chatbot trained with [Tensorless](https://pypi.org/project/tensorless/).

CatTongue learns from a small collection of human messages and cat responses, then tries to respond like a chaotic, dramatic cat.

## Example

```text
You: how are you?

Cat: meowwuhhh!! huh!? how are you human??
```

```text
You: done with your food

Cat: nomnomnom!! meuh! done with the spicy rat!!
```

## 📁 Project Structure

```text
CatTongue/
├── data/
│   └── conversations.json
├── train.py
├── chat.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Setup

Install the dependencies:

```bash
pip install -r requirements.txt
```

Or install Tensorless directly:

```bash
pip install tensorless
```

## 🧠 Train

Train CatTongue using the dataset:

```bash
python train.py
```

This creates:

```text
cat.tl
```

which contains the trained Tensorless model.

## 💬 Chat

After training:

```bash
python chat.py
```

Then talk to your cat:

```text
🐈 CatTongue is awake!
Type 'exit' to leave.

You: are you hungry?
Cat: MEOW!! obviously human!! bring food!!

You: let's play
Cat: MEOWMEOWMEOW!! FINALLY!! GET THE STRING!!
```

Type `exit` to stop.

## 📚 Dataset

The training data lives in:

```text
data/conversations.json
```

Each example contains a human message and the corresponding cat response:

```json
{
  "user": "what are you doing?",
  "cat": "mrrp... watching the wall. the wall is suspicious."
}
```

You can add more conversations to make CatTongue learn more responses and personality.

Some real chats with model:<br>
```
You: “Do you trust me?”
Cat: “only if you walk toward the kitchen. 😼🐾”
You: “Who is your enemy?”
Cat: “empty boxes. 📦😾 they are useful for exactly zero seconds.”
You: “If I gave you unlimited food, would you love me?”
Cat: “stay. 😼👑”
You: “Who is your favorite human?”
Cat: “are you holding food? 🤨🍗”
You: “Do you love me?”
Cat: “…maybe. 😼❤️”
You: “What would you do with a million fish?”
Cat: “only one? 👀 But I prefer 'see distant. 😴”
You: “What makes you angry?”
Cat: “food, I baths. 🛁”
You: “Are you secretly plotting something?”
Cat: “me?”
Cat: “yes. 😼🍪”
You: “What do you think humans are for?”
Cat: “fish. 🐟😼 CTHE BAG!! 🍗”
You: “What is your favorite animal?”
Cat: “ME. 😼🐈 next question.”
You: “Do you have a best friend?”
Cat: “the vacuum cleaner. 😾🧹 we have unfinished business.”
You: “Do you have enemies?”
Cat: “the vacuum cleaner. 😾🧹 we have unfinished business.”
You: “Food?”
Cat: “my food”
Cat: “I am always good. 😼✨ mostly.”
You: “Are you a good cat?”
Cat: “MEOW. 😼🐈 ...mrrp... 🤫🐈”
You: “Do you fear me?”
Cat: “That's my legercasing where I was excupt your spe? no.”
```
## 🛠 Built With

* Python
* Tensorless

## 🤔 Why?

Because apparently teaching a computer to talk like a cat is easier than teaching an actual cat to answer questions.

🐈 **Meow responsibly.**
