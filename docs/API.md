# 🔧 API Reference

Technical documentation for developers who want to understand or extend InfinityChat.

## 📖 Table of Contents

- [Architecture Overview](#architecture-overview)
- [Core Classes](#core-classes)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Data Structures](#data-structures)
- [Extending InfinityChat](#extending-infinitychat)
- [Code Examples](#code-examples)

---

## 🏗️ Architecture Overview

InfinityChat follows a modular architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                    ChatInterface                             │
│  (User interaction, CLI parsing, output formatting)          │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    ModelManager                              │
│  (Model selection, API calls, fallback logic, statistics)    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│              LocalBrain + Online APIs                        │
│  (Offline knowledge base + Multiple API endpoints)           │
└─────────────────────────────────────────────────────────────┘
```

### Components

1. **Config** - Application constants and settings
2. **LocalBrain** - Offline knowledge base
3. **ModelManager** - AI model orchestration
4. **ChatInterface** - User interaction layer

---

## 📦 Core Classes

### Config

Application configuration and constants.

#### Attributes

```python
class Config:
    VERSION = "2.0.0"              # App version
    APP_NAME = "InfinityChat"       # Application name
    DESCRIPTION = "Unlimited AI..." # Tagline
    
    MODELS = {                      # Available AI models dict
        "default": {...},
        "llama": {...},
        ...
    }
    
    API_ENDPOINTS = [...]           # List of API URLs
    TIMEOUT = 30                    # Request timeout (seconds)
    MAX_RETRIES = 3                 # Max retry attempts
    USER_AGENT = "InfinityChat/2.0.0"
```

#### Usage

```python
from infinitychat import Config

print(f"Version: {Config.VERSION}")
print(f"Models: {list(Config.MODELS.keys())}")
```

---

### LocalBrain

Offline AI knowledge base for instant responses without internet.

#### Methods

##### `__init__()`

Initializes greetings, farewells, jokes, and knowledge base.

##### `get_response(query: str) -> str`

Generates response from local knowledge.

**Parameters:**
- `query` (str): User's question

**Returns:**
- `str`: Generated response

**Logic:**
1. Checks for greeting keywords → returns random greeting
2. Checks for farewell keywords → returns random farewell
3. Checks for joke keywords → returns random joke
4. Searches knowledge base by topic keywords
5. Returns default helpful response if no match

**Example:**

```python
brain = LocalBrain()
response = brain.get_response("Tell me a joke")
print(response)
# Output: "Why do programmers prefer dark mode?..."
```

---

### ModelManager

Manages multiple AI models with automatic failover.

#### Attributes

- `local_brain` - LocalBrain instance
- `current_model` - Currently selected model ID
- `model_history` - List of usage history entries
- `successful_responses` - Count of successful API calls
- `failed_attempts` - Count of failed API calls

#### Methods

##### `__init__()`

Initializes the model manager with local brain and empty history.

##### `select_best_model(query: str) -> str`

Intelligently selects the best model for a query.

**Parameters:**
- `query` (str): User's question

**Returns:**
- `str`: Recommended model ID

**Selection Logic:**
```python
if "code" in query or "program" in query:
    return "llama"
elif "calculate" in query or "math" in query:
    return "gpt-free"
elif "story" in query or "poem" in query:
    return "claude-mini"
elif "science" in query or "physics" in query:
    return "gemini-lite"
else:
    return "default"
```

**Example:**

```python
manager = ModelManager()
model = manager.select_best_model("Write a Python function")
print(model)  # Output: "llama"
```

##### `generate_response(query: str, model: str = None) -> Dict`

Generates AI response with multiple fallback strategies.

**Parameters:**
- `query` (str): User's question
- `model` (str, optional): Specific model to use

**Returns:**
```python
{
    "success": bool,
    "response": str,
    "model_used": str,
    "source": str,  # "online" or "offline"
    "response_time": float,
    "confidence": float,
    "note": str  # optional
}
```

**Strategy:**
1. Auto-select model if not specified
2. Try online APIs (multiple endpoints)
3. If all fail, fallback to LocalBrain
4. Return formatted response dict

**Example:**

```python
manager = ModelManager()
result = manager.generate_response("What is Python?")

print(result["response"])
print(f"Model: {result['model_used']}")
print(f"Time: {result['response_time']}s")
```

##### `_try_online_apis(query: str, model: str) -> Optional[Dict]`

Attempts to get response from online API endpoints.

**Parameters:**
- `query` (str): User's question
- `model` (str): Model ID to use

**Returns:**
- `Dict` with response text if successful
- `None` if all endpoints fail

**Process:**
1. Iterate through API_ENDPOINTS list
2. Send POST request with query and model
3. Parse JSON response
4. Return first successful response
5. Continue to next endpoint on failure

##### `get_model_info() -> List[Dict]`

Gets information about all available models.

**Returns:**
```python
[
    {
        "id": "llama",
        "name": "Llama 3",
        "description": "...",
        "provider": "Meta AI",
        "speed": "Medium",
        "quality": "Very High",
        "status": "available"
    },
    ...
]
```

##### `get_stats() -> Dict`

Gets usage statistics.

**Returns:**
```python
{
    "total_requests": int,
    "successful_responses": int,
    "failed_attempts": int,
    "success_rate": float,  # percentage
    "average_response_time": float,
    "model_usage": {"llama": 5, "local": 10, ...},
    "current_model": str
}
```

---

### ChatInterface

User-friendly chat interface handling CLI and interactive modes.

#### Attributes

- `model_manager` - ModelManager instance
- `chat_history` - List of conversation entries
- `is_interactive` - Boolean flag for interactive mode

#### Methods

##### `display_banner()`

Displays application banner with logo and version.

##### `display_models()`

Shows table of available AI models.

##### `display_help()`

Shows comprehensive help guide.

##### `display_stats()`

Shows usage statistics from ModelManager.

##### `process_query(query: str, model: str = None) -> str`

Processes user query and returns formatted response.

**Handles:**
- Special commands (/models, /stats, etc.)
- Empty queries
- Normal questions

**Returns:**
- Formatted response string
- Empty string for command outputs
- "exit_command" for exit requests

##### `run_interactive()`

Starts interactive chat session.

**Features:**
- Continuous input loop
- Command processing
- Graceful exit handling
- Chat history tracking

##### `run_single_query(query: str, model: str = None)`

Executes single query from command line.

**Process:**
1. Display banner
2. Show question
3. Process query
4. Display answer
5. Exit

---

## ⚙️ Configuration

### Models Configuration

Add or modify models in `Config.MODELS`:

```python
MODELS = {
    "model-id": {
        "name": "Display Name",
        "description": "What this model does",
        "provider": "Company/Organization",
        "speed": "Fast|Medium|Slow|Instant",
        "quality": "High|Very High|Good"
    }
}
```

### API Endpoints

Configure API endpoints in `Config.API_ENDPOINTS`:

```python
API_ENDPOINTS = [
    "https://api.example.com/v1/chat",
    "https://backup-api.example.com/chat",
    # Add more endpoints for redundancy
]
```

**Endpoint Requirements:**
- Accept POST requests
- Content-Type: application/json
- Return JSON with "response", "answer", or "text" field

**Request Format:**
```json
{
    "query": "User's question",
    "model": "model-id",
    "max_tokens": 1024,
    "temperature": 0.7,
    "stream": false
}
```

**Response Format:**
```json
{
    "response": "AI's answer",
    "usage": {...}  # optional
}
```

### Timeout and Retries

```python
TIMEOUT = 30      # Seconds before request times out
MAX_RETRIES = 3   # Number of retry attempts per endpoint
```

---

## 🌐 API Endpoints

### Current Endpoints

```python
API_ENDPOINTS = [
    "https://api.neuro.ai/chat",
    "https://api.ai-chat.org/v1/completions",
    "https://free-api.llm-services.net/chat",
    "https://open-source-ai.api.completions.io/v1"
]
```

### Adding Custom Endpoints

1. Ensure endpoint accepts POST with JSON
2. Add to API_ENDPOINTS list
3. Test with curl:

```bash
curl -X POST https://your-api.com/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "test", "model": "default"}'
```

### Implementing API Handler

For custom API integration:

```python
def _try_online_apis(self, query: str, model: str):
    headers = {
        "User-Agent": Config.USER_AGENT,
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"  # if needed
    }
    
    payload = {
        "query": query,
        "model": model,
        "max_tokens": 1024,
        "temperature": 0.7
    }
    
    # Your custom API logic here
    # ...
```

---

## 📊 Data Structures

### Response Dictionary

```python
{
    "success": True,
    "response": "The AI's answer text...",
    "model_used": "llama",
    "source": "online",  # or "offline"
    "response_time": 1.23,
    "confidence": 0.95,
    "note": "Optional note"  # only if present
}
```

### Model Info Dictionary

```python
{
    "id": "llama",
    "name": "Llama 3",
    "description": "Meta's powerful open-source language model",
    "provider": "Meta AI",
    "speed": "Medium",
    "quality": "Very High",
    "status": "available"
}
```

### Statistics Dictionary

```python
{
    "total_requests": 100,
    "successful_responses": 95,
    "failed_attempts": 5,
    "success_rate": 95.0,
    "average_response_time": 0.85,
    "model_usage": {
        "llama": 30,
        "local": 50,
        "gpt-free": 20
    },
    "current_model": "llama"
}
```

### Chat History Entry

```python
{
    "query": "User's question",
    "response": "AI's answer",
    "model": "llama",
    "timestamp": "2024-01-15T10:30:00.123456"
}
```

---

## 🔨 Extending InfinityChat

### Adding a New Model

1. **Add to Config.MODELS:**

```python
MODELS = {
    # ... existing models ...
    "new-model": {
        "name": "New Model",
        "description": "Description of the model",
        "provider": "Provider Name",
        "speed": "Fast",
        "quality": "High"
    }
}
```

2. **Update select_best_model():**

```python
def select_best_model(self, query: str) -> str:
    # ... existing logic ...
    
    if "specialty" in query_lower:
        return "new-model"
    
    return "default"
```

3. **Add API endpoint if needed**

### Adding New Commands

1. **Add to process_query():**

```python
def process_query(self, query: str, model=None):
    if query.strip().startswith('/'):
        command = query.strip()[1:].lower()
        
        if command == 'newcommand':
            self.do_something()
            return ""
```

2. **Document in help:**

Update `display_help()` to include new command.

### Custom Knowledge Base

Extend LocalBrain:

```python
class LocalBrain:
    def __init__(self):
        # Add your custom knowledge
        self.knowledge_base["my_topic"] = {
            "keywords": ["keyword1", "keyword2"],
            "response": "Your detailed response..."
        }
```

---

## 💻 Code Examples

### Basic Usage

```python
from infinitychat import ChatInterface

# Create interface
chat = ChatInterface()

# Single query
response = chat.process_query("What is Python?")
print(response)
```

### Programmatic Access

```python
from infinitychat import ModelManager, Config

# Initialize manager
manager = ModelManager()

# Get model info
models = manager.get_model_info()
for model in models:
    print(f"{model['name']}: {model['description']}")

# Generate response
result = manager.generate_response("Hello!")
print(f"Response: {result['response']}")
print(f"Model: {result['model_used']}")
print(f"Time: {result['response_time']}s")

# Get statistics
stats = manager.get_stats()
print(f"Success rate: {stats['success_rate']}%")
```

### Integration Example

```python
#!/usr/bin/env python3

from infinitychat import ChatInterface, Config

def main():
    chat = ChatInterface()
    
    print(f"Welcome to {Config.APP_NAME} v{Config.VERSION}")
    print("=" * 60)
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit']:
                print("Goodbye!")
                break
            
            response = chat.process_query(user_input)
            
            if response:
                print(f"\nAI: {response}")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### Batch Processing

```python
from infinitychat import ModelManager

manager = ModelManager()

questions = [
    "What is 2 + 2?",
    "Explain quantum physics",
    "Write a hello world program"
]

for q in questions:
    result = manager.generate_response(q)
    print(f"Q: {q}")
    print(f"A: {result['response'][:100]}...")
    print(f"Model: {result['model_used']}, Time: {result['response_time']}s")
    print("-" * 60)
```

### Custom Model Selection

```python
from infinitychat import ModelManager

manager = ModelManager()

# Force specific model
result = manager.generate_response(
    query="Write a sorting algorithm",
    model="llama"
)

print(result['response'])
```

---

## 🧪 Testing

### Unit Test Example

```python
import unittest
from infinitychat import Config, LocalBrain, ModelManager

class TestInfinityChat(unittest.TestCase):
    
    def test_config_version(self):
        self.assertEqual(Config.VERSION, "2.0.0")
    
    def test_local_brain_greeting(self):
        brain = LocalBrain()
        response = brain.get_response("hello")
        self.assertIn(response, brain.greetings)
    
    def test_model_selection(self):
        manager = ModelManager()
        model = manager.select_best_model("write code")
        self.assertEqual(model, "llama")
    
    def test_generate_response(self):
        manager = ModelManager()
        result = manager.generate_response("Hello")
        self.assertTrue(result["success"])
        self.assertIn("response", result)

if __name__ == '__main__':
    unittest.main()
```

---

## 📝 Best Practices

### For Developers

1. **Always handle exceptions** when calling APIs
2. **Check response success** before using result
3. **Use type hints** for better code clarity
4. **Log errors** for debugging
5. **Test offline mode** regularly

### For Contributors

1. **Follow existing code style**
2. **Add docstrings** to new functions
3. **Update documentation** when adding features
4. **Test thoroughly** before submitting PR
5. **Keep dependencies minimal** (standard library only)

---

<div align="center">

**Need more help?** → [Usage Guide](USAGE.md) | [Contributing](../CONTRIBUTING.md)

[Back to Documentation Index](README.md)

</div>
