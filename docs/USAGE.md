# 💡 Usage Guide

Complete guide to using Unlimited AI Chat effectively.

---

## 🚀 Quick Start

```bash
# Single query
python ai_chat.py "What is Python?"

# Interactive mode
python ai_chat.py
```

---

## 📋 Table of Contents

1. [Basic Usage](#basic-usage)
2. [Command-Line Mode](#command-line-mode)
3. [Interactive Mode](#interactive-mode)
4. [Advanced Features](#advanced-features)
5. [Examples](#examples)
6. [Tips & Tricks](#tips--tricks)
7. [Best Practices](#best-practices)

---

## 🎯 Basic Usage

### Method 1: Single Query

Ask a question and get an immediate response:

```bash
python ai_chat.py "Your question here"
```

**Example:**
```bash
python ai_chat.py "Write a poem about coding"
```

### Method 2: Interactive Chat

Start a conversation session:

```bash
python ai_chat.py
```

Then type your messages one by one.

---

## 💻 Command-Line Mode

### Syntax

```bash
python ai_chat.py [options] "your message"
```

### Examples

#### Simple Question
```bash
python ai_chat.py "What is machine learning?"
```

#### Request Code
```bash
python ai_chat.py "Show me a Python function to calculate factorial"
```

#### Creative Writing
```bash
python ai_chat.py "Write a short story about AI"
```

#### Multiple Words
```bash
python ai_chat.py Explain quantum computing in simple terms
```

### Output Format

```
============================================================
UNLIMITED AI CHAT - NO LOGIN REQUIRED
============================================================

You: What is Python?

AI: Python is a high-level, interpreted programming language...
```

---

## 💬 Interactive Mode

### Starting Interactive Mode

```bash
python ai_chat.py
```

### Expected Output

```
============================================================
UNLIMITED AI CHAT - NO LOGIN REQUIRED
============================================================

Type your message (or 'quit' to exit):


You: 
```

### Conversation Flow

```
You: Hello!
AI: Thinking...
AI: Hello! I'm your unlimited AI assistant...

You: Can you write code?
AI: Thinking...
AI: Yes! Here's an example...

You: Thank you!
AI: Thinking...
AI: You're welcome! Ask me anything else.

You: quit

Goodbye!
```

### Exit Commands

Type any of these to exit:
- `quit`
- `exit`
- `q`

### Keyboard Shortcuts

- `Ctrl+C`: Force exit
- `Ctrl+D`: End input (Unix/Linux/Mac)
- `Ctrl+Z`: Suspend (Windows)

---

## 🔥 Advanced Features

### 1. Multi-Line Input

For complex queries, use triple quotes (in interactive mode):

```
You: """
Write a Python program that:
1. Takes user input
2. Processes it
3. Returns formatted output
"""
```

### 2. Batch Processing

Create a text file with queries:

**queries.txt:**
```
What is Python?
Explain recursion
Write hello world program
```

**Process with:**
```bash
while read line; do python ai_chat.py "$line"; done < queries.txt
```

### 3. Save Responses

Redirect output to a file:

```bash
python ai_chat.py "Explain AI" > response.txt
```

Or in interactive mode:
```bash
python ai_chat.py | tee conversation.txt
```

### 4. Pipe Input

Use echo to pipe questions:

```bash
echo "What is 2 + 2?" | python ai_chat.py
```

### 5. Script Integration

Use in your own Python scripts:

```python
import subprocess

def ask_ai(question):
    result = subprocess.run(
        ['python', 'ai_chat.py', question],
        capture_output=True,
        text=True
    )
    return result.stdout

response = ask_ai("What is Docker?")
print(response)
```

---

## 📚 Examples

### Educational

#### Math Help
```bash
python ai_chat.py "Explain Pythagorean theorem"
```

#### Science
```bash
python ai_chat.py "How does photosynthesis work?"
```

#### History
```bash
python ai_chat.py "Who was Albert Einstein?"
```

### Programming

#### Code Generation
```bash
python ai_chat.py "Write a Python function to sort a list"
```

#### Debugging Help
```bash
python ai_chat.py "Why am I getting IndexError in Python?"
```

#### Learning
```bash
python ai_chat.py "Explain object-oriented programming"
```

### Creative

#### Writing
```bash
python ai_chat.py "Write a haiku about technology"
```

#### Ideas
```bash
python ai_chat.py "Give me 5 startup ideas for AI"
```

#### Stories
```bash
python ai_chat.py "Write a short mystery story"
```

### Productivity

#### Email Drafts
```bash
python ai_chat.py "Draft a professional email for meeting request"
```

#### Summaries
```bash
python ai_chat.py "Summarize the benefits of exercise"
```

#### Lists
```bash
python ai_chat.py "List 10 healthy breakfast ideas"
```

---

## 💡 Tips & Tricks

### 1. Be Specific

❌ **Vague:**
```bash
python ai_chat.py "Tell me about code"
```

✅ **Specific:**
```bash
python ai_chat.py "Explain how Python decorators work with examples"
```

### 2. Use Context

Provide context for better answers:

```bash
python ai_chat.py "I'm a beginner programmer. Explain variables in Python"
```

### 3. Request Format

Specify desired output format:

```bash
python ai_chat.py "List 5 benefits of exercise in bullet points"
```

### 4. Ask for Examples

```bash
python ai_chat.py "Show me 3 examples of list comprehension in Python"
```

### 5. Iterative Refinement

If answer isn't perfect, ask follow-up:

```bash
python ai_chat.py "Can you explain that more simply?"
```

### 6. Combine Topics

```bash
python ai_chat.py "How can I use AI in web development?"
```

### 7. Request Step-by-Step

```bash
python ai_chat.py "Explain how to install Python step by step"
```

---

## 🎯 Best Practices

### Do ✅

- Be clear and specific in your questions
- Provide context when needed
- Use proper grammar and spelling
- Ask follow-up questions for clarification
- Save important responses to files

### Don't ❌

- Don't ask overly broad questions
- Don't expect real-time information
- Don't share sensitive personal information
- Don't rely solely on AI for critical decisions
- Don't use for malicious purposes

### Response Quality Tips

| Query Type | Best Practice | Example |
|------------|--------------|---------|
| **Factual** | Be specific | "When was Python first released?" |
| **Creative** | Give direction | "Write a funny poem about coding" |
| **Technical** | Specify level | "Explain APIs to a beginner" |
| **Code** | Language + task | "Python function to reverse string" |

---

## 🐛 Common Usage Issues

### Issue: Slow Response

**Cause:** Online API calls take time  
**Solution:** Normal behavior (2-5 seconds). Local fallback is instant.

### Issue: Generic Response

**Cause:** Using local fallback mode  
**Solution:** Check internet connection or be more specific in query.

### Issue: No Response

**Cause:** Network issues or API down  
**Solution:** System will automatically use local responses.

### Issue: Cut-off Response

**Cause:** Response length limit  
**Solution:** Ask for continuation: "Continue from where you left off"

---

## 🎨 Customization

### Modify Local Responses

Edit `ai_chat.py` to add custom responses:

```python
def generate_local_response(prompt):
    responses = {
        "greeting": "Hello! How can I help you today?",
        "joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
        # Add your own...
    }
```

### Change Default Model

Modify API parameters in `ai_chat.py`:

```python
# In try_huggingface function
payload = {
    "inputs": prompt,
    "parameters": {
        "max_new_tokens": 1000,  # Increase for longer responses
        "temperature": 0.8,       # Higher = more creative
    }
}
```

---

## 📊 Usage Statistics

Track your usage (optional):

```bash
# Count queries
python ai_chat.py "Hello" >> usage.log

# View history
cat usage.log

# Count total queries
wc -l usage.log
```

---

## 🔄 Automation Examples

### Daily Question Script

**daily_question.sh:**
```bash
#!/bin/bash
QUESTIONS=(
    "What is one new thing I can learn today?"
    "Give me a coding challenge"
    "Share an interesting tech fact"
)
RANDOM_QUESTION=${QUESTIONS[$RANDOM % ${#QUESTIONS[@]}]}
python ai_chat.py "$RANDOM_QUESTION"
```

### Auto-Response Bot

```python
import subprocess
import time

questions = [
    "What is AI?",
    "Explain machine learning",
    "What is deep learning?"
]

for q in questions:
    print(f"Q: {q}")
    subprocess.run(['python', 'ai_chat.py', q])
    time.sleep(2)
```

---

## 📱 Mobile Usage

### Termux (Android)

```bash
# Create alias
echo 'alias ai="python /data/data/com.termux/files/home/unlimited-ai-chat/ai_chat.py"' >> ~/.bashrc

# Use shortcut
ai "Hello"
```

### iOS Shortcuts

Create iOS Shortcut:
1. Open Shortcuts app
2. Add action: "Run Pythonista"
3. Select `ai_chat.py` script
4. Add to home screen

---

## 🎓 Learning Path

### Beginner
1. Start with simple questions
2. Try interactive mode
3. Explore different query types

### Intermediate
1. Use batch processing
2. Save and organize responses
3. Integrate with scripts

### Advanced
1. Customize source code
2. Add new API endpoints
3. Build applications on top

---

## 📞 Need Help?

- 📖 Read [FAQ](FAQ.md)
- 🐛 Check [Troubleshooting](TROUBLESHOOTING.md)
- 💬 Ask in [Discussions](https://github.com/YOUR_USERNAME/unlimited-ai-chat/discussions)

---

<div align="center">

**Ready to explore more? → [API Docs](API.md)**

[Back to Docs](README.md) | [View API Reference →](API.md)

</div>
