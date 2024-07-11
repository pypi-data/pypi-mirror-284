# Mem0: Long-Term Memory for LLMs

Mem0 provides a smart, self-improving memory layer for Large Language Models, enabling personalized AI experiences across applications.

## Features

- Persistent memory for users, sessions, and agents
- Self-improving personalization
- Simple API for easy integration
- Cross-platform consistency

## Quick Start

### Installation


```bash
pip install mem0ai
```

## Usage

### Instantiate

```python
from mem0 import Memory

m = Memory()
```

If you want to use Qdrant in server mode, use the following method to instantiate.

Run qdrant first:

```bash
docker pull qdrant/qdrant

docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```

Then, instantiate memory with qdrant server:

```python
from mem0 import Memory

config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
        }
    },
}

m = Memory.from_config(config)
```

### Store a Memory

```python
m.add("Likes to play cricket over weekend", user_id="alex", metadata={"foo": "bar"})
# Output:
# [
#   {
#     'id': 'm1',
#     'event': 'add',
#     'data': 'Likes to play cricket over weekend'
#   }
# ]

# Similarly, you can store a memory for an agent
m.add("Agent X is best travel agent in Paris", agent_id="agent-x", metadata={"type": "long-term"})
```

### Retrieve all memories

#### 1. Get all memories
```python
m.get_all()
# Output:
# [
#   {
#     'id': 'm1',
#     'text': 'Likes to play cricket over weekend',
#     'metadata': {
#       'data': 'Likes to play cricket over weekend'
#     }
#   },
#   {
#     'id': 'm2',
#     'text': 'Agent X is best travel agent in Paris',
#     'metadata': {
#       'data': 'Agent X is best travel agent in Paris'
#     }
#   }
# ]

```
#### 2. Get memories for specific user

```python
m.get_all(user_id="alex")
```

#### 3. Get memories for specific agent

```python
m.get_all(agent_id="agent-x")
```

#### 4. Get memories for a user during an agent run

```python
m.get_all(agent_id="agent-x", user_id="alex")
```

### Retrieve a Memory

```python
memory_id = "m1"
m.get(memory_id)
# Output:
# {
#   'id': '1',
#   'text': 'Likes to play cricket over weekend',
#   'metadata': {
#     'data': 'Likes to play cricket over weekend'
#   }
# }
```

### Search for related memories

```python
m.search(query="What is my name", user_id="deshraj")
```

### Update a Memory

```python
m.update(memory_id="m1", data="Likes to play tennis")
```

### Get history of a Memory

```python
m.history(memory_id="m1")
# Output:
# [
#   {
#     'id': 'h1',
#     'memory_id': 'm1',
#     'prev_value': None,
#     'new_value': 'Likes to play cricket over weekend',
#     'event': 'add',
#     'timestamp': '2024-06-12 21:00:54.466687',
#     'is_deleted': 0
#   },
#   {
#     'id': 'h2',
#     'memory_id': 'm1',
#     'prev_value': 'Likes to play cricket over weekend',
#     'new_value': 'Likes to play tennis',
#     'event': 'update',
#     'timestamp': '2024-06-12 21:01:17.230943',
#     'is_deleted': 0
#   }
# ]
```

### Delete a Memory

#### Delete specific memory

```python
m.delete(memory_id="m1")
```

#### Delete memories for a user or agent

```python
m.delete_all(user_id="alex")
m.delete_all(agent_id="agent-x")
```

#### Delete all Memories

```python
m.reset()
```

## License

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
