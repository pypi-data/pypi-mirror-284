# chat-user

Streamlit component that allows you to do X

## Installation instructions

```sh
pip install chat-user
```

## Usage instructions

```python
import streamlit as st

from chat_user import chat_user

user1 = {
  "id": 1,
  "name": "user1",
  "socket": "",
  "admin": False,
}

user2 = {
  "id": 2,
  "name": "user2",
  "socket": "",
  "admin": False,
}

u1 = chat_user(user1, True)
print(u1)

u2 = chat_user(user2, False)
print(u2)
```