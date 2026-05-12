# 💻 Usage Guide

Complete guide to using InfinityChat effectively.

## 🚀 Quick Start

### Basic Usage

```bash
# Interactive mode (recommended for beginners)
python infinitychat.py

# Single question
python infinitychat.py "What is quantum physics?"
```

That's it! You're ready to chat! 🎉

---

## 📋 Command Line Options

### All Available Commands

| Command | Short Form | Description | Example |
|---------|------------|-------------|---------|
| `--help` | `-h` | Display complete help guide | `python infinitychat.py --help` |
| `--models` | `-m` | List all available AI models | `python infinitychat.py --models` |
| `--stats` | `-s` | Show usage statistics | `python infinitychat.py --stats` |
| `--model <id>` | `--ml <id>` | Use specific AI model | `python infinitychat.py --model llama "Write code"` |
| `<query>` | - | Ask a single question | `python infinitychat.py "Hello!"` |

### Detailed Examples

#### 1. Get Help

```bash
python infinitychat.py --help
```

Shows comprehensive usage guide with examples.

#### 2. View Available Models

```bash
python infinitychat.py --models
```

Output:
```
🤖 AVAILABLE AI MODELS:

ID              NAME                 PROVIDER        SPEED      QUALITY     
----------------------------------------------------------------------------------
default         Smart Auto-Select    Multi-Provider  Fast       High        
gpt-free        GPT-Free             Open Source     Fast       High        
llama           Llama 3              Meta AI         Medium     Very High   
mistral         Mistral 7B           Mistral AI      Fast       High        
gemini-lite     Gemini Lite          Google          Very Fast  High        
claude-mini     Claude Mini          Anthropic       Fast       Very High   
local           Local Brain          Built-in        Instant    Good        

💡 Tip: Use '--model <model_id>' to select a specific model
   Default: 'default' (auto-selects best model)
```

#### 3. Check Statistics

```bash
python infinitychat.py --stats
```

Shows your usage history and performance metrics.

#### 4. Use Specific Model

```bash
# For coding tasks
python infinitychat.py --model llama "Write a Python function to sort a list"

# For creative writing
python infinitychat.py --model claude-mini "Write a poem about AI"

# For science questions
python infinitychat.py --model gemini-lite "Explain black holes"

# For math problems
python infinitychat.py --model gpt-free "Calculate 25 × 17"
```

---

## 💬 Interactive Mode

### Starting Interactive Mode

```bash
python infinitychat.py
```

### Interface Overview

When you start interactive mode, you'll see:

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   🚀 InfinityChat v2.0.0                                  ║
║   Unlimited AI Chat - No Login Required                   ║
║                                                           ║
║   ✨ NO LOGIN REQUIRED • UNLIMITED USE FOREVER ✨         ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

💬 Enter your questions below. Type '/exit' to quit.

------------------------------------------------------------
```

### Interactive Commands

While in chat, use these special commands:

| Command | Action |
|---------|--------|
| `/models` | Display all available AI models |
| `/stats` | Show your usage statistics |
| `/clear` | Clear chat history |
| `/help` | Show help guide |
| `/exit` | Exit the program |
| `quit` | Also exits |
| `exit` | Also exits |

### Example Session

```
👤 You: Hello!

🤖 AI: Hello! I'm InfinityChat, your unlimited AI assistant. How can I help you today?

---
🤖 Model: local | ⏱️ 0.00s | 💯 Confidence: 75%

👤 You: Tell me a joke

🤖 AI: Why do programmers prefer dark mode? Because light attracts bugs! 🐛

---
🤖 Model: local | ⏱️ 0.00s | 💯 Confidence: 75%

👤 You: /stats

📊 USAGE STATISTICS

Total Requests:      2
Successful:          2
Failed Attempts:     0
Success Rate:        100.0%
Avg Response Time:   0.00s
Current Model:       local

Model Usage:
  • local: 2 requests

👤 You: /exit

👋 Goodbye! Thanks for using InfinityChat!
```

---

## 💡 Usage Examples by Category

### 🧮 Mathematics

```bash
# Basic arithmetic
python infinitychat.py "What is 25 + 17?"
python infinitychat.py "Calculate 100 - 37"
python infinitychat.py "What's 15 × 8?"
python infinitychat.py "Divide 144 by 12"

# Advanced math
python infinitychat.py "What is 2 to the power of 10?"
python infinitychat.py "Calculate the square root of 144"
python infinitychat.py "Solve x² = 81"
python infinitychat.py "What is the factorial of 5?"
```

### 💻 Programming & Code

```bash
# Python code
python infinitychat.py "Write a Python function to calculate factorial"
python infinitychat.py "Create a Python script to read a CSV file"
python infinitychat.py "How do I reverse a string in Python?"
python infinitychat.py "Explain list comprehensions with examples"

# JavaScript
python infinitychat.py "Write a JavaScript function to sort an array"
python infinitychat.py "How to fetch data from an API in JavaScript?"
python infinitychat.py "Create a React component example"

# Debugging
python infinitychat.py "Debug this code: [paste your code]"
python infinitychat.py "Why am I getting a null pointer exception?"

# Algorithms
python infinitychat.py "Implement binary search in Python"
python infinitychat.py "Write a sorting algorithm"
python infinitychat.py "Explain dynamic programming"
```

### 🔬 Science

```bash
# Physics
python infinitychat.py "Explain quantum entanglement"
python infinitychat.py "What is the theory of relativity?"
python infinitychat.py "How does gravity work?"
python infinitychat.py "Describe the double-slit experiment"

# Chemistry
python infinitychat.py "What is the structure of an atom?"
python infinitychat.py "Explain chemical bonding"
python infinitychat.py "What are isotopes?"

# Biology
python infinitychat.py "How does photosynthesis work?"
python infinitychat.py "Explain DNA replication"
python infinitychat.py "What is natural selection?"

# Astronomy
python infinitychat.py "What is a black hole?"
python infinitychat.py "How are stars formed?"
python infinitychat.py "Describe the Big Bang theory"
```

### 📜 History & General Knowledge

```bash
# History
python infinitychat.py "Tell me about ancient Egypt"
python infinitychat.py "Who was Julius Caesar?"
python infinitychat.py "What caused World War II?"
python infinitychat.py "Explain the Renaissance period"

# Geography
python infinitychat.py "What is the capital of Australia?"
python infinitychat.py "How many continents are there?"
python infinitychat.py "Describe the Amazon rainforest"

# General knowledge
python infinitychat.py "Who invented the telephone?"
python infinitychat.py "What is the speed of light?"
python infinitychat.py "How many bones are in the human body?"
```

### ✍️ Writing & Creative

```bash
# Creative writing
python infinitychat.py "Write a short story about a robot"
python infinitychat.py "Create a poem about nature"
python infinitychat.py "Write a haiku about coding"

# Professional writing
python infinitychat.py "Write a professional email template"
python infinitychat.py "Create a resume summary"
python infinitychat.py "Draft a cover letter"

# Content creation
python infinitychat.py "Generate blog post ideas about AI"
python infinitychat.py "Write social media posts"
python infinitychat.py "Create a product description"
```

### 😄 Entertainment

```bash
# Jokes
python infinitychat.py "Tell me a joke"
python infinitychat.py "Give me a programming joke"
python infinitychat.py "Make me laugh"

# Fun facts
python infinitychat.py "Tell me an interesting fact"
python infinitychat.py "What's a fun fact about space?"
python infinitychat.py "Share a weird historical fact"

# Games
python infinitychat.py "Let's play 20 questions"
python infinitychat.py "Give me a riddle"
python infinitychat.py "Play word association"
```

### ⏰ Time & Date

```bash
python infinitychat.py "What time is it?"
python infinitychat.py "What's today's date?"
python infinitychat.py "How many days until Christmas?"
```

---

## 🎯 Tips for Best Results

### 1. Be Specific

❌ Vague: "Tell me about Python"  
✅ Specific: "Explain Python decorators with examples"

### 2. Provide Context

❌ Less effective: "Fix this"  
✅ More effective: "Fix this Python error: IndexError: list index out of range"

### 3. Break Down Complex Questions

Instead of one huge question, ask multiple focused questions:

```bash
python infinitychat.py "What is machine learning?"
python infinitychat.py "What are the types of machine learning?"
python infinitychat.py "Give me a simple ML example in Python"
```

### 4. Use the Right Model

- **Coding** → `--model llama`
- **Math** → `--model gpt-free`
- **Creative** → `--model claude-mini`
- **Science** → `--model gemini-lite`
- **General** → `--model default` (auto-selects)

### 5. Try Different Phrasings

If you don't get the answer you want, rephrase:

```bash
# First attempt
python infinitychat.py "Explain recursion"

# If too technical
python infinitychat.py "Explain recursion like I'm 5"

# If need examples
python infinitychat.py "Explain recursion with Python examples"
```

---

## 📊 Understanding Responses

### Response Format

Each response includes:

```
[AI Response Content]

---
🤖 Model: llama | ⏱️ 0.45s | 💯 Confidence: 95%
```

### What the Metrics Mean

- **Model**: Which AI model generated the response
- **Response Time**: How long it took (lower is faster)
- **Confidence**: Model's confidence in the answer (higher is better)

### Online vs Offline Mode

**Online Mode** (when APIs available):
```
🤖 Model: llama | ⏱️ 1.23s | 💯 Confidence: 95%
```

**Offline Mode** (fallback to Local Brain):
```
🤖 Model: local | ⏱️ 0.00s | 💯 Confidence: 75%

⚠️ Using offline mode. Online services temporarily unavailable.
```

Both modes provide helpful responses!

---

## 🔧 Advanced Usage

### Scripting with InfinityChat

You can use InfinityChat in shell scripts:

#### Bash Script (Linux/Mac)

```bash
#!/bin/bash

QUESTION="What is 2 + 2?"
ANSWER=$(python infinitychat.py "$QUESTION" 2>&1 | grep -A 100 "Answer:" | tail -n +2)

echo "Question: $QUESTION"
echo "Answer: $ANSWER"
```

#### PowerShell Script (Windows)

```powershell
$question = "What is the capital of France?"
$output = python infinitychat.py $question

Write-Host "Question: $question"
Write-Host "Answer: $output"
```

### Batch Processing

Create a file `questions.txt`:

```
What is Python?
Explain machine learning
Tell me a joke
```

Process all questions:

```bash
while read question; do
    echo "Q: $question"
    python infinitychat.py "$question"
    echo "---"
done < questions.txt
```

---

## 🎓 Best Practices

### ✅ Do's

- ✅ Be clear and specific in your questions
- ✅ Use appropriate models for different tasks
- ✅ Try interactive mode for conversations
- ✅ Check `/stats` to monitor usage
- ✅ Use `/help` when unsure

### ❌ Don'ts

- ❌ Don't ask overly vague questions
- ❌ Don't expect perfect accuracy (it's AI)
- ❌ Don't share sensitive personal information
- ❌ Don't use for critical decisions without verification

---

## 🆘 Getting Help

### In-App Help

```bash
# Command line
python infinitychat.py --help

# Interactive mode
/ help
```

### Documentation

- **[Installation Guide](INSTALLATION.md)** - Setup instructions
- **[API Reference](API.md)** - Technical details
- **[Troubleshooting](TROUBLESHOOTING.md)** - Common issues
- **[FAQ](FAQ.md)** - Frequently asked questions

### Community Support

- GitHub Issues: Report bugs or request features
- Discussions: Ask questions and share ideas

---

<div align="center">

**Ready to chat?** Start with `python infinitychat.py`

[Back to Documentation Index](README.md)

</div>
