# 📥 Installation Guide

Complete installation instructions for InfinityChat on all platforms.

## 🎯 Prerequisites

Before installing InfinityChat, ensure you have:

- ✅ **Python 3.6 or higher** (Python 3.8+ recommended)
- ✅ **Internet connection** (for initial download and online features)
- ✅ **Terminal/Command Prompt access**

### Check Python Version

```bash
python --version
# or
python3 --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/)

---

## 💻 Platform-Specific Installation

### Windows

#### Method 1: Direct Download

1. **Download the script**
   ```powershell
   # Using PowerShell
   Invoke-WebRequest -Uri "https://raw.githubusercontent.com/yourusername/infinitychat/main/infinitychat.py" -OutFile "infinitychat.py"
   ```

2. **Navigate to the directory**
   ```powershell
   cd C:\path\to\infinitychat
   ```

3. **Run InfinityChat**
   ```powershell
   python infinitychat.py
   ```

#### Method 2: Git Clone

1. **Install Git** (if not already installed)
   - Download from [git-scm.com](https://git-scm.com/download/win)
   - Run the installer with default settings

2. **Clone the repository**
   ```powershell
   git clone https://github.com/yourusername/infinitychat.git
   cd infinitychat
   ```

3. **Run InfinityChat**
   ```powershell
   python infinitychat.py
   ```

#### Method 3: Create a Batch File (Optional)

Create `run_infinitychat.bat`:

```batch
@echo off
echo Starting InfinityChat...
python infinitychat.py
pause
```

Double-click to run!

---

### macOS

#### Method 1: Terminal Download

1. **Open Terminal** (Cmd + Space, type "Terminal")

2. **Download the script**
   ```bash
   curl -O https://raw.githubusercontent.com/yourusername/infinitychat/main/infinitychat.py
   ```

3. **Make executable**
   ```bash
   chmod +x infinitychat.py
   ```

4. **Run InfinityChat**
   ```bash
   python3 infinitychat.py
   ```

#### Method 2: Git Clone

1. **Install Git** (if needed)
   ```bash
   xcode-select --install
   ```

2. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/infinitychat.git
   cd infinitychat
   ```

3. **Run InfinityChat**
   ```bash
   python3 infinitychat.py
   ```

#### Method 3: Homebrew (Optional)

If you use Homebrew:

```bash
# Install Python (if needed)
brew install python

# Clone and run
git clone https://github.com/yourusername/infinitychat.git
cd infinitychat
python3 infinitychat.py
```

---

### Linux

#### Ubuntu/Debian

1. **Install Python** (if needed)
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Download InfinityChat**
   ```bash
   wget https://raw.githubusercontent.com/yourusername/infinitychat/main/infinitychat.py
   ```

3. **Make executable**
   ```bash
   chmod +x infinitychat.py
   ```

4. **Run InfinityChat**
   ```bash
   python3 infinitychat.py
   ```

#### Fedora/RHEL

1. **Install Python** (if needed)
   ```bash
   sudo dnf install python3 python3-pip
   ```

2. **Download and run**
   ```bash
   wget https://raw.githubusercontent.com/yourusername/infinitychat/main/infinitychat.py
   chmod +x infinitychat.py
   python3 infinitychat.py
   ```

#### Arch Linux

1. **Install Python** (if needed)
   ```bash
   sudo pacman -S python python-pip
   ```

2. **Download and run**
   ```bash
   wget https://raw.githubusercontent.com/yourusername/infinitychat/main/infinitychat.py
   chmod +x infinitychat.py
   python3 infinitychat.py
   ```

---

## 🌐 Alternative Installation Methods

### Method 1: GitHub Desktop (All Platforms)

1. **Download GitHub Desktop**
   - Visit [desktop.github.com](https://desktop.github.com/)
   - Install for your platform

2. **Clone the repository**
   - Open GitHub Desktop
   - File → Clone Repository
   - Enter: `https://github.com/yourusername/infinitychat.git`
   - Choose local path
   - Click Clone

3. **Run from terminal**
   ```bash
   cd path/to/infinitychat
   python infinitychat.py
   ```

### Method 2: Manual Download

1. **Download from GitHub**
   - Visit the repository on GitHub
   - Click "Code" button
   - Download ZIP
   - Extract to desired location

2. **Run**
   ```bash
   cd extracted-folder
   python infinitychat.py
   ```

### Method 3: pip Installation (Future)

When published to PyPI:

```bash
pip install infinitychat

# Run from anywhere
infinitychat
```

---

## ✅ Verify Installation

After installation, verify everything works:

### Test 1: Check Help

```bash
python infinitychat.py --help
```

Expected output: Full help guide with usage instructions

### Test 2: List Models

```bash
python infinitychat.py --models
```

Expected output: Table of available AI models

### Test 3: Ask a Question

```bash
python infinitychat.py "Hello, how are you?"
```

Expected output: Friendly AI response

### Test 4: Interactive Mode

```bash
python infinitychat.py
```

Expected output: Interactive chat interface

Type `/exit` to quit

---

## 🔧 Troubleshooting Installation

### Issue: "python: command not found"

**Solution:**
- **Windows**: Add Python to PATH during installation, or use `py` instead of `python`
- **Mac/Linux**: Try `python3` instead of `python`

### Issue: "Permission denied"

**Solution:**
```bash
# Mac/Linux
chmod +x infinitychat.py
```

### Issue: "ModuleNotFoundError"

**Solution:**
InfinityChat uses only standard library modules. If you see this error:
- Ensure you downloaded the complete file
- Check Python version (needs 3.6+)

### Issue: Download fails

**Solution:**
- Check internet connection
- Try alternative download method
- Use GitHub Desktop application

### Issue: Old Python version

**Solution:**
```bash
# Check version
python --version

# If below 3.6, update Python
# Visit python.org/downloads
```

---

## 🚀 Post-Installation Setup

### Optional: Add to PATH

#### Windows

1. Find Python installation path:
   ```powershell
   where python
   ```

2. Add to PATH:
   - Right-click "This PC" → Properties
   - Advanced System Settings
   - Environment Variables
   - Edit "Path" variable
   - Add Python directory

#### Mac/Linux

Add to `~/.bashrc` or `~/.zshrc`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Create Alias (Optional)

#### Windows (PowerShell Profile)

Add to `$PROFILE`:
```powershell
function ic { python "C:\path\to\infinitychat.py" $args }
```

#### Mac/Linux

Add to `~/.bashrc` or `~/.zshrc`:
```bash
alias ic='python3 ~/path/to/infinitychat.py'
```

Then reload:
```bash
source ~/.bashrc  # or source ~/.zshrc
```

Now you can run:
```bash
ic "Your question"
```

---

## 📱 Mobile Installation (Advanced)

### Android (Termux)

1. **Install Termux** from F-Droid or Play Store

2. **Update packages**
   ```bash
   pkg update && pkg upgrade
   ```

3. **Install Python**
   ```bash
   pkg install python
   ```

4. **Download InfinityChat**
   ```bash
   wget https://raw.githubusercontent.com/yourusername/infinitychat/main/infinitychat.py
   ```

5. **Run**
   ```bash
   python infinitychat.py
   ```

### iOS (a-Shell)

1. **Install a-Shell** from App Store

2. **Download script** using built-in browser

3. **Run**
   ```python
   python infinitychat.py
   ```

---

## 🎓 Next Steps

Congratulations! You've successfully installed InfinityChat! 🎉

### What's Next?

1. **Read the [Usage Guide](USAGE.md)** - Learn how to use all features
2. **Try examples** - Start chatting with different queries
3. **Explore AI models** - See which model works best for you
4. **Check FAQ** - Answers to common questions

### Quick Commands

```bash
# Get help
python infinitychat.py --help

# See models
python infinitychat.py --models

# Start chatting
python infinitychat.py

# Ask a question
python infinitychat.py "What is machine learning?"
```

---

<div align="center">

**Need more help?** → [Troubleshooting](TROUBLESHOOTING.md) | [FAQ](FAQ.md)

[Back to Documentation Index](README.md)

</div>
