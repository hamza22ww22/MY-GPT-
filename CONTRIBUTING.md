# Contributing to Unlimited AI Chat

Thank you for your interest in contributing to Unlimited AI Chat! This document provides guidelines and instructions for contributing.

## 🎯 How Can I Contribute?

### 1. Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected behavior** vs **actual behavior**
- **Environment details** (OS, Python version, etc.)
- **Screenshots or logs** if applicable

**Example:**
```markdown
**Bug Description**
The script fails when using Hugging Face API

**Steps to Reproduce**
1. Run `python ai_chat.py "Hello"`
2. Wait for response
3. See error

**Expected Behavior**
Should get AI response

**Actual Behavior**
Connection timeout error

**Environment**
- OS: Windows 10
- Python: 3.9.7
```

### 2. Suggesting Features

Feature suggestions are welcome! Please provide:

- **Use case**: Why is this feature needed?
- **Proposed solution**: How should it work?
- **Alternatives considered**: Other approaches you thought about

### 3. Code Contributions

#### Development Setup

```bash
# Fork the repository
git fork https://github.com/YOUR_USERNAME/unlimited-ai-chat.git

# Clone your fork
git clone https://github.com/YOUR_USERNAME/unlimited-ai-chat.git
cd unlimited-ai-chat

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install requests

# Create a branch
git checkout -b feature/your-feature-name
```

#### Coding Guidelines

- **Follow PEP 8** style guidelines
- **Write docstrings** for all functions and classes
- **Add comments** for complex logic
- **Keep functions small** and focused
- **Use meaningful variable names**
- **Handle errors gracefully**

#### Testing Your Changes

```bash
# Test command-line mode
python ai_chat.py "Test message"

# Test interactive mode
python ai_chat.py

# Test edge cases
python ai_chat.py ""
python ai_chat.py "Very long message..." 
```

#### Commit Messages

Write clear, concise commit messages:

```
✅ Good: "Add new API endpoint for better fallback"
❌ Bad: "fixed stuff"

✅ Good: "Fix connection timeout handling"
❌ Bad: "bug fix"
```

### 4. Documentation Improvements

Documentation is crucial! You can help by:

- Fixing typos or unclear explanations
- Adding examples
- Translating to other languages
- Improving code comments

## 🔄 Pull Request Process

1. **Fork** the repository
2. **Create a branch** from `main`
3. **Make your changes**
4. **Test thoroughly**
5. **Update documentation** if needed
6. **Submit PR** with clear description
7. **Respond to feedback** promptly

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
Describe how you tested your changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No new warnings
```

## 📋 Code Review Guidelines

When reviewing code, consider:

- **Functionality**: Does it work as intended?
- **Code Quality**: Is it clean and maintainable?
- **Performance**: Are there efficiency concerns?
- **Security**: Any potential vulnerabilities?
- **Documentation**: Is it well-documented?

## 🎨 Architecture Overview

```
ai_chat.py
├── get_free_ai_response()
│   ├── try_huggingface()
│   ├── try_myshell()
│   └── generate_local_response()
└── main()
    ├── Command-line mode
    └── Interactive mode
```

### Adding New API Endpoints

```python
def try_new_api(prompt):
    """
    Add your new API endpoint here
    
    Args:
        prompt (str): User's input message
        
    Returns:
        str: AI response or None if failed
    """
    try:
        # Your API implementation
        url = "YOUR_API_URL"
        headers = {"Content-Type": "application/json"}
        payload = {"messages": [{"role": "user", "content": prompt}]}
        
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        return None
    except Exception as e:
        print(f"New API error: {e}")
        return None

# Add to get_free_ai_response()
result = try_new_api(prompt)
if result:
    return result
```

## 🚀 Release Process

Releases follow semantic versioning (MAJOR.MINOR.PATCH):

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

## 💬 Community Guidelines

- Be respectful and inclusive
- Help newcomers
- Stay on topic in discussions
- Give constructive feedback
- Celebrate contributions

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and ideas
- **Email**: your.email@example.com (for sensitive matters)

## 🙏 Thank You!

Every contribution makes this project better. Whether it's a typo fix or a major feature, we appreciate your time and effort!

---

<div align="center">

**Happy Contributing! 🎉**

[Back to README](README.md)

</div>
