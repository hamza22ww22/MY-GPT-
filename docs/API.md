# 🔌 API Documentation

Technical documentation for developers who want to understand or extend the API system.

---

## 📋 Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [API Endpoints](#api-endpoints)
3. [Request/Response Format](#requestresponse-format)
4. [Code Structure](#code-structure)
5. [Adding New APIs](#adding-new-apis)
6. [Error Handling](#error-handling)
7. [Performance Optimization](#performance-optimization)

---

## 🏗️ Architecture Overview

### System Design

```
┌─────────────┐
│  User Input │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│ get_free_ai_response│
└──────────┬──────────┘
           │
    ┌──────┴──────┐
    │             │
    ▼             ▼
┌─────────┐  ┌──────────┐
│Hugging  │  │ MyShell  │
│ Face    │  │ API      │
│ API     │  │          │
└────┬────┘  └────┬─────┘
     │            │
     └─────┬──────┘
           │
           ▼
    ┌──────────────┐
    │   Success?   │──No──→ ┌─────────────┐
    └──────┬───────┘        │   Local     │
           │ Yes            │  Generator  │
           ▼                └──────┬──────┘
    ┌─────────────┐                │
    │   Return    │◄───────────────┘
    │  Response   │
    └─────────────┘
```

### Layers

1. **Layer 1**: Hugging Face Inference API
2. **Layer 2**: MyShell Free API
3. **Layer 3**: Local Response Generator (fallback)

---

## 🌐 API Endpoints

### 1. Hugging Face Inference API

**Endpoint:** `https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct`

**Method:** POST

**Headers:**
```python
headers = {
    "Content-Type": "application/json"
}
```

**Payload:**
```python
payload = {
    "inputs": "Your prompt here",
    "parameters": {
        "max_new_tokens": 500,
        "temperature": 0.7,
        "return_full_text": False
    }
}
```

**Response:**
```json
[
    {
        "generated_text": "AI response text here"
    }
]
```

**Implementation:**
```python
def try_huggingface(prompt):
    try:
        API_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"
        headers = {"Content-Type": "application/json"}
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 500,
                "temperature": 0.7,
                "return_full_text": False
            }
        }
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get('generated_text', '')
            elif isinstance(result, dict):
                return result.get('generated_text', '')
        return None
    except Exception as e:
        print(f"Hugging Face error: {e}")
        return None
```

---

### 2. MyShell API

**Endpoint:** `https://app.myshell.ai/api/v1/chat/completions`

**Method:** POST

**Headers:**
```python
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}
```

**Payload:**
```python
payload = {
    "model": "myshell-dolphin-mixtral-8x7b",
    "messages": [
        {"role": "user", "content": "Your prompt here"}
    ],
    "max_tokens": 500
}
```

**Response:**
```json
{
    "choices": [
        {
            "message": {
                "content": "AI response text here"
            }
        }
    ]
}
```

**Implementation:**
```python
def try_myshell(prompt):
    try:
        url = "https://app.myshell.ai/api/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
        payload = {
            "model": "myshell-dolphin-mixtral-8x7b",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500
        }
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            return result.get('choices', [{}])[0].get('message', {}).get('content', '')
        return None
    except Exception as e:
        print(f"MyShell error: {e}")
        return None
```

---

### 3. Local Response Generator

**No external API calls** - generates responses locally using keyword matching.

**Implementation:**
```python
def generate_local_response(prompt):
    """Generate responses locally without any API"""
    responses = {
        "poem": """In circuits deep where electrons flow...""",
        "hello": "Hello! I'm your unlimited AI assistant...",
        "code": """Here's a simple Python example...""",
    }
    
    prompt_lower = prompt.lower()
    for key, value in responses.items():
        if key in prompt_lower:
            return value
    
    # Default response
    return f"""AI Response (No Login Required):

You asked: "{prompt}"

I'm running on a completely free, unlimited system..."""
```

---

## 📤 Request/Response Format

### Standard Request Flow

```python
def get_free_ai_response(prompt, model="gpt-3.5-turbo"):
    """
    Main function that orchestrates all API attempts
    
    Args:
        prompt (str): User's input message
        model (str): Model identifier (optional)
    
    Returns:
        str: AI response text
    """
    
    # Try Layer 1: Hugging Face
    result = try_huggingface(prompt)
    if result:
        return result
    
    # Try Layer 2: MyShell
    result = try_myshell(prompt)
    if result:
        return result
    
    # Fallback Layer 3: Local
    return generate_local_response(prompt)
```

### Response Processing

```python
# Parse Hugging Face response
if isinstance(result, list) and len(result) > 0:
    return result[0].get('generated_text', '')

# Parse MyShell response
return result.get('choices', [{}])[0].get('message', {}).get('content', '')
```

---

## 📁 Code Structure

### File Organization

```
ai_chat.py
├── Imports
│   ├── requests
│   ├── sys
│   └── json
│
├── Functions
│   ├── get_free_ai_response()
│   │   ├── try_huggingface()
│   │   ├── try_myshell()
│   │   └── generate_local_response()
│   │
│   └── main()
│       ├── Argument parsing
│       └── Interactive loop
│
└── Entry Point
    └── if __name__ == "__main__"
```

### Function Signatures

```python
def get_free_ai_response(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    """Get AI response using free endpoints"""
    pass

def try_huggingface(prompt: str) -> Optional[str]:
    """Try Hugging Face API"""
    pass

def try_myshell(prompt: str) -> Optional[str]:
    """Try MyShell API"""
    pass

def generate_local_response(prompt: str) -> str:
    """Generate local response"""
    pass

def main() -> None:
    """Main entry point"""
    pass
```

---

## ➕ Adding New APIs

### Step-by-Step Guide

#### 1. Create New API Function

```python
def try_your_api(prompt: str) -> Optional[str]:
    """
    Add your custom API endpoint
    
    Args:
        prompt (str): User's input message
        
    Returns:
        str: AI response or None if failed
    """
    try:
        # Define endpoint
        url = "YOUR_API_URL"
        
        # Set headers
        headers = {
            "Content-Type": "application/json",
            # Add any required headers
        }
        
        # Create payload
        payload = {
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 500
        }
        
        # Make request
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        # Check success
        if response.status_code == 200:
            result = response.json()
            # Extract response based on API format
            return result['choices'][0]['message']['content']
        
        return None
        
    except Exception as e:
        print(f"Your API error: {e}")
        return None
```

#### 2. Integrate into Main Function

```python
def get_free_ai_response(prompt, model="gpt-3.5-turbo"):
    # Try existing APIs first
    result = try_huggingface(prompt)
    if result:
        return result
    
    result = try_myshell(prompt)
    if result:
        return result
    
    # Add your new API
    result = try_your_api(prompt)
    if result:
        return result
    
    # Final fallback
    return generate_local_response(prompt)
```

#### 3. Test Your API

```bash
# Test with simple query
python ai_chat.py "Test new API"

# Test error handling
python ai_chat.py ""

# Test interactive mode
python ai_chat.py
```

---

## ⚠️ Error Handling

### Types of Errors

1. **Network Errors**
   - Timeout
   - Connection refused
   - DNS failure

2. **API Errors**
   - 400 Bad Request
   - 401 Unauthorized
   - 429 Rate Limited
   - 500 Server Error

3. **Parsing Errors**
   - Invalid JSON
   - Missing fields
   - Unexpected format

### Error Handling Strategy

```python
def try_api(prompt):
    try:
        # API call
        response = requests.post(url, json=payload, timeout=30)
        
        # Check status
        if response.status_code != 200:
            print(f"API returned status {response.status_code}")
            return None
        
        # Parse response
        result = response.json()
        return extract_content(result)
        
    except requests.Timeout:
        print("Request timed out")
        return None
        
    except requests.ConnectionError:
        print("Connection failed")
        return None
        
    except json.JSONDecodeError:
        print("Invalid JSON response")
        return None
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
```

### Graceful Degradation

```python
# Always have fallback
result = try_primary_api(prompt)
if not result:
    result = try_secondary_api(prompt)
if not result:
    result = generate_local_response(prompt)  # Guaranteed to work
```

---

## ⚡ Performance Optimization

### Timeout Settings

```python
# Optimal timeout values
timeout = 30  # seconds

# For faster fallback
timeout = 10  # quick fail
```

### Connection Pooling

```python
# Create session for reuse
session = requests.Session()

def try_api_with_session(prompt):
    response = session.post(url, json=payload, timeout=30)
    return response
```

### Async Implementation (Advanced)

```python
import asyncio
import aiohttp

async def try_async_api(session, prompt):
    async with session.post(url, json=payload) as response:
        if response.status == 200:
            result = await response.json()
            return result['choices'][0]['message']['content']
    return None

async def get_response_async(prompt):
    async with aiohttp.ClientSession() as session:
        tasks = [
            try_huggingface_async(session, prompt),
            try_myshell_async(session, prompt),
        ]
        
        for coro in asyncio.as_completed(tasks):
            result = await coro
            if result:
                return result
        
        return generate_local_response(prompt)
```

### Caching Responses

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_cached_response(prompt):
    return get_free_ai_response(prompt)
```

---

## 🧪 Testing APIs

### Unit Tests

```python
import unittest

class TestAPIs(unittest.TestCase):
    
    def test_huggingface(self):
        result = try_huggingface("Hello")
        self.assertIsNotNone(result)
    
    def test_myshell(self):
        result = try_myshell("Hi")
        self.assertIsNotNone(result)
    
    def test_local_response(self):
        result = generate_local_response("hello")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
```

### Integration Tests

```python
def test_full_flow():
    prompt = "Write a short poem"
    response = get_free_ai_response(prompt)
    
    assert isinstance(response, str)
    assert len(response) > 0
    print(f"Success! Response length: {len(response)}")
```

---

## 📊 Monitoring & Logging

### Add Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def try_huggingface(prompt):
    logger.info(f"Trying Hugging Face API")
    try:
        # ... API code ...
        logger.info("Hugging Face success")
        return result
    except Exception as e:
        logger.error(f"Hugging Face failed: {e}")
        return None
```

### Track Success Rates

```python
stats = {
    'huggingface': {'success': 0, 'failure': 0},
    'myshell': {'success': 0, 'failure': 0},
    'local': {'success': 0}
}

def track_api_usage(api_name, success):
    if success:
        stats[api_name]['success'] += 1
    else:
        stats[api_name]['failure'] += 1
```

---

## 🔒 Security Considerations

### Best Practices

1. **Never hardcode API keys** (not needed for this project!)
2. **Validate user input** before sending to APIs
3. **Use HTTPS** for all API calls
4. **Set reasonable timeouts** to prevent hangs
5. **Handle errors gracefully**

### Input Sanitization

```python
import html

def sanitize_input(prompt):
    # Remove potentially harmful content
    prompt = html.escape(prompt)
    # Limit length
    prompt = prompt[:5000]
    return prompt
```

---

## 📚 Resources

- [Hugging Face API Docs](https://huggingface.co/docs/api-inference)
- [Requests Library](https://requests.readthedocs.io/)
- [Python asyncio](https://docs.python.org/3/library/asyncio.html)

---

<div align="center">

**Need help? → [Troubleshooting](TROUBLESHOOTING.md)**

[Back to Docs](README.md) | [View Troubleshooting →](TROUBLESHOOTING.md)

</div>
