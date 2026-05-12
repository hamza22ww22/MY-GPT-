# 📥 Installation Guide

Complete installation instructions for Unlimited AI Chat.

---

## ⚡ Quick Install (30 seconds)

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/unlimited-ai-chat.git

# Navigate to directory
cd unlimited-ai-chat

# Run immediately
python ai_chat.py "Hello!"
```

That's it! No dependencies, no setup, no login! 🎉

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation Methods](#installation-methods)
   - [Method 1: Git Clone (Recommended)](#method-1-git-clone-recommended)
   - [Method 2: Manual Download](#method-2-manual-download)
   - [Method 3: pip Install](#method-3-pip-install)
3. [Platform-Specific Instructions](#platform-specific-instructions)
   - [Windows](#windows)
   - [macOS](#macos)
   - [Linux](#linux)
4. [Verification](#verification)
5. [Troubleshooting Installation](#troubleshooting-installation)

---

## ✅ Prerequisites

### Required

- **Python 3.7 or higher**
  - Check version: `python --version` or `python3 --version`
  - Download: [python.org](https://www.python.org/downloads/)

### Optional

- **Git** (for cloning repository)
  - Download: [git-scm.com](https://git-scm.com/)
  
- **requests library** (usually pre-installed)
  - Install: `pip install requests`

---

## 🚀 Installation Methods

### Method 1: Git Clone (Recommended)

#### Step 1: Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/unlimited-ai-chat.git
```

#### Step 2: Navigate to Directory

```bash
cd unlimited-ai-chat
```

#### Step 3: Make Executable (Linux/Mac)

```bash
chmod +x ai_chat.py
```

#### Step 4: Run

```bash
# Option A: Direct execution
python ai_chat.py "Hello!"

# Option B: Interactive mode
python ai_chat.py

# Option C: As executable (Linux/Mac)
./ai_chat.py
```

---

### Method 2: Manual Download

#### Step 1: Download Files

Download these files from the repository:
- `ai_chat.py` (main script)
- `README.md` (documentation)

#### Step 2: Save to Folder

Create a folder and save the files:
```
unlimited-ai-chat/
└── ai_chat.py
```

#### Step 3: Open Terminal

Navigate to the folder:
```bash
cd path/to/unlimited-ai-chat
```

#### Step 4: Run

```bash
python ai_chat.py "Your message"
```

---

### Method 3: pip Install

#### Step 1: Install from GitHub

```bash
pip install git+https://github.com/YOUR_USERNAME/unlimited-ai-chat.git
```

#### Step 2: Run Command

```bash
ai-chat "Hello!"
```

Or use Python module:
```bash
python -m ai_chat "Hello!"
```

---

## 💻 Platform-Specific Instructions

### Windows

#### Option A: Using Command Prompt

```cmd
# Clone repository
git clone https://github.com/YOUR_USERNAME/unlimited-ai-chat.git

# Navigate to directory
cd unlimited-ai-chat

# Run script
python ai_chat.py "Hello!"
```

#### Option B: Using PowerShell

```powershell
# Clone repository
git clone https://github.com/YOUR_USERNAME/unlimited-ai-chat.git

# Navigate to directory
Set-Location unlimited-ai-chat

# Run script
python ai_chat.py "Hello!"
```

#### Installing Python on Windows

1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer
3. ✅ Check "Add Python to PATH"
4. Click "Install Now"
5. Verify: Open CMD and type `python --version`

---

### macOS

#### Using Terminal

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/unlimited-ai-chat.git

# Navigate to directory
cd unlimited-ai-chat

# Make executable
chmod +x ai_chat.py

# Run script
python3 ai_chat.py "Hello!"
```

#### Installing Python on macOS

**Method 1: Homebrew (Recommended)**
```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python

# Verify
python3 --version
```

**Method 2: Official Installer**
1. Download from [python.org](https://www.python.org/downloads/macos/)
2. Open `.pkg` file
3. Follow installation wizard
4. Verify in Terminal: `python3 --version`

---

### Linux

#### Ubuntu/Debian

```bash
# Update package list
sudo apt update

# Install Python (if not installed)
sudo apt install python3 python3-pip

# Install Git (if not installed)
sudo apt install git

# Clone repository
git clone https://github.com/YOUR_USERNAME/unlimited-ai-chat.git

# Navigate to directory
cd unlimited-ai-chat

# Make executable
chmod +x ai_chat.py

# Run script
python3 ai_chat.py "Hello!"
```

#### Fedora/RHEL

```bash
# Install Python
sudo dnf install python3 python3-pip

# Install Git
sudo dnf install git

# Clone and run
git clone https://github.com/YOUR_USERNAME/unlimited-ai-chat.git
cd unlimited-ai-chat
chmod +x ai_chat.py
python3 ai_chat.py "Hello!"
```

#### Arch Linux

```bash
# Install Python
sudo pacman -S python python-pip

# Install Git
sudo pacman -S git

# Clone and run
git clone https://github.com/YOUR_USERNAME/unlimited-ai-chat.git
cd unlimited-ai-chat
chmod +x ai_chat.py
python3 ai_chat.py "Hello!"
```

---

## ✅ Verification

### Test Installation

Run these commands to verify everything works:

```bash
# Check Python version
python --version
# Expected: Python 3.7.0 or higher

# Test script with simple query
python ai_chat.py "Hello"
# Expected: AI response

# Test interactive mode
python ai_chat.py
# Expected: Interactive prompt

# Type "quit" to exit
```

### Expected Output

```
============================================================
UNLIMITED AI CHAT - NO LOGIN REQUIRED
============================================================

Type your message (or 'quit' to exit):

You: Hello
AI: Thinking...
AI: Hello! I'm your unlimited AI assistant. No login required, 
    no limits imposed. Ask me anything!
```

---

## 🐛 Troubleshooting Installation

### Issue: "python: command not found"

**Solution:**
```bash
# Try python3 instead
python3 ai_chat.py "Hello"

# Or add Python to PATH
# Windows: Reinstall Python and check "Add to PATH"
# Mac/Linux: Edit .bashrc or .zshrc
export PATH="$HOME/.local/bin:$PATH"
```

### Issue: "ModuleNotFoundError: No module named 'requests'"

**Solution:**
```bash
# Install requests library
pip install requests

# Or use pip3
pip3 install requests

# Or run without internet (uses local fallback)
python ai_chat.py "Hello"
```

### Issue: Permission denied (Linux/Mac)

**Solution:**
```bash
# Make script executable
chmod +x ai_chat.py

# Or run with python directly
python ai_chat.py "Hello"
```

### Issue: Git not found

**Solution:**
```bash
# Install Git
# Windows: Download from git-scm.com
# Mac: xcode-select --install
# Ubuntu: sudo apt install git
# Fedora: sudo dnf install git

# Or use manual download method instead
```

### Issue: Python version too old

**Solution:**
```bash
# Check version
python --version

# If below 3.7, upgrade Python
# Download latest from python.org
```

### Issue: Firewall blocking requests

**Solution:**
- Allow Python through firewall
- Or use offline mode (local responses work without internet)
- Configure proxy if needed:
  ```bash
  export HTTP_PROXY=http://proxy:port
  export HTTPS_PROXY=https://proxy:port
  python ai_chat.py "Hello"
  ```

---

## 🎯 Post-Installation Setup

### Optional: Add to PATH

Make the script accessible from anywhere:

#### Windows

```cmd
# Add to system PATH
setx PATH "%PATH%;C:\path\to\unlimited-ai-chat"
```

#### Linux/Mac

```bash
# Add to .bashrc or .zshrc
echo 'alias ai-chat="python /path/to/ai_chat.py"' >> ~/.bashrc
source ~/.bashrc

# Now you can run from anywhere
ai-chat "Hello"
```

### Create Desktop Shortcut (Optional)

#### Windows

1. Right-click on desktop
2. New → Shortcut
3. Browse to `ai_chat.py`
4. Name it "Unlimited AI Chat"

#### macOS

1. Create Automator application
2. Run shell script: `python3 /path/to/ai_chat.py`
3. Save to Applications

#### Linux

1. Create `.desktop` file
2. Add to applications menu

---

## 📱 Mobile Installation

### Android (Termux)

```bash
# Install Termux from F-Droid or Play Store

# Update packages
pkg update && pkg upgrade

# Install Python
pkg install python

# Install Git
pkg install git

# Clone repository
git clone https://github.com/YOUR_USERNAME/unlimited-ai-chat.git

# Navigate and run
cd unlimited-ai-chat
python ai_chat.py "Hello"
```

### iOS (Pythonista)

1. Install Pythonista from App Store
2. Download `ai_chat.py`
3. Open in Pythonista
4. Run script

---

## 🎓 Next Steps

After installation:

1. ✅ **Test basic usage**: `python ai_chat.py "Hello"`
2. 📖 **Read documentation**: See [USAGE.md](USAGE.md)
3. 🎮 **Try interactive mode**: `python ai_chat.py`
4. 🔧 **Customize**: Edit local responses in code
5. 🤝 **Contribute**: See [CONTRIBUTING.md](../CONTRIBUTING.md)

---

## 📞 Need Help?

If you encounter issues:

- 📖 Check [Troubleshooting Guide](TROUBLESHOOTING.md)
- ❓ Read [FAQ](FAQ.md)
- 🐛 Open [GitHub Issue](https://github.com/YOUR_USERNAME/unlimited-ai-chat/issues)
- 💬 Ask in [Discussions](https://github.com/YOUR_USERNAME/unlimited-ai-chat/discussions)

---

<div align="center">

**Installation complete? → [Start Using!](USAGE.md)**

[Back to README](../README.md) | [View Usage Guide →](USAGE.md)

</div>
