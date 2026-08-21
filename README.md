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

## 🛠 Built With

* Python
* Tensorless

## 🤔 Why?

Because apparently teaching a computer to talk like a cat is easier than teaching an actual cat to answer questions.

🐈 **Meow responsibly.**
