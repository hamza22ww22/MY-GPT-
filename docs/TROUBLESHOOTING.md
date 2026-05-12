# 🔧 Troubleshooting Guide

Common issues and their solutions for InfinityChat.

## 🚨 Quick Fixes

### Issue: "python: command not found"

**Cause:** Python is not installed or not in PATH

**Solutions:**

#### Windows
```powershell
# Try using 'py' instead
py infinitychat.py --help

# Or add Python to PATH
# 1. Find Python installation
where python

# 2. Add to PATH via System Properties
# Control Panel → System → Advanced → Environment Variables
# Edit "Path" and add Python directory
```

#### Mac/Linux
```bash
# Try python3 instead
python3 infinitychat.py --help

# Install Python if needed
# Mac: brew install python3
# Ubuntu: sudo apt install python3
```

---

### Issue: "Permission denied"

**Cause:** File doesn't have execute permissions (Mac/Linux)

**Solution:**
```bash
chmod +x infinitychat.py
python3 infinitychat.py
```

---

### Issue: Script runs but shows no output

**Cause:** Might be waiting for input or network timeout

**Solutions:**
```bash
# Try with explicit query
python infinitychat.py "Hello"

# Check if stuck in interactive mode
# Press Ctrl+C to exit, then run with a query

# Run with help to verify it works
python infinitychat.py --help
```

---

### Issue: Slow response times

**Cause:** Network latency or API endpoint issues

**Solutions:**

1. **Use a specific model**
   ```bash
   python infinitychat.py --model mistral "Your question"
   ```

2. **Check internet connection**
   ```bash
   ping google.com
   ```

3. **Use offline mode** (instant responses)
   - Just keep using it, will auto-fallback to offline
   - Offline mode is instant but has limited knowledge

4. **Try different time**
   - API servers might be busy during peak hours

---

### Issue: "ModuleNotFoundError"

**Cause:** Missing dependencies (shouldn't happen - uses only standard library)

**Solution:**
```bash
# Verify you have the complete file
# The file should be ~20KB

# Check Python version (needs 3.6+)
python --version

# Re-download if file is corrupted
curl -O https://raw.githubusercontent.com/yourusername/infinitychat/main/infinitychat.py
```

---

## 🔍 Error Messages

### SSL/Certificate Errors

**Error:** `ssl.SSLCertVerificationError`

**Solution:** This is handled automatically in the code. If you still see it:

```bash
# Update Python's certificates
# Mac: /Applications/Python\ 3.x/Install\ Certificates.command
# Or reinstall Python
```

### Connection Timeout

**Error:** `urllib.error.URLError: <urlopen error timed out>`

**Solution:**
```bash
# Check internet connection
ping google.com

# Try offline mode (automatic fallback)
# Just keep asking questions, it will switch to offline

# Increase timeout (edit the script)
# Change TIMEOUT = 30 to TIMEOUT = 60 in Config class
```

### JSON Decode Error

**Error:** `json.decoder.JSONDecodeError`

**Solution:**
- This is handled by try-except blocks
- Will automatically fallback to next API endpoint
- If all fail, uses offline mode

---

## 🌐 Network Issues

### Issue: All online APIs failing

**Symptoms:**
- Always shows "Using offline mode"
- No online responses

**Solutions:**

1. **Check firewall settings**
   ```bash
   # Temporarily disable firewall to test
   # Windows: Windows Defender Firewall
   # Mac: System Preferences → Security & Privacy
   ```

2. **Check proxy settings**
   ```bash
   # If behind corporate proxy
   export HTTP_PROXY=http://proxy.company.com:port
   export HTTPS_PROXY=https://proxy.company.com:port
   ```

3. **DNS issues**
   ```bash
   # Try changing DNS to Google DNS
   # 8.8.8.8 and 8.8.4.4
   ```

4. **Network restrictions**
   - Some networks block AI APIs
   - Try mobile hotspot
   - Use VPN if allowed

---

## 💻 Platform-Specific Issues

### Windows

#### Issue: PowerShell execution policy

**Error:** `cannot be loaded because running scripts is disabled`

**Solution:**
```powershell
# Run as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Or use Command Prompt instead
cmd
python infinitychat.py
```

#### Issue: Unicode/encoding errors

**Solution:**
```powershell
# Set UTF-8 encoding
$env:PYTHONIOENCODING="utf-8"
python infinitychat.py
```

### macOS

#### Issue: Gatekeeper blocking

**Solution:**
```bash
# Right-click → Open instead of double-click
# Or:
xattr -d com.apple.quarantine infinitychat.py
```

#### Issue: Python 2 vs Python 3

**Solution:**
```bash
# Always use python3 on Mac
python3 infinitychat.py

# Create alias
echo "alias python=python3" >> ~/.zshrc
source ~/.zshrc
```

### Linux

#### Issue: Missing pip or packages

**Solution:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip

# Arch
sudo pacman -S python python-pip
```

#### Issue: Permissions in home directory

**Solution:**
```bash
# Make sure you own the file
chown $USER:$USER infinitychat.py
chmod +x infinitychat.py
```

---

## 🤖 Model Issues

### Issue: Specific model not working

**Solution:**
```bash
# List available models
python infinitychat.py --models

# Try default model (auto-selects)
python infinitychat.py "Your question"

# Try different model
python infinitychat.py --model mistral "Your question"
```

### Issue: Responses seem generic

**Cause:** Using offline mode

**Solution:**
- Check internet connection
- Online models provide more detailed responses
- Offline mode is best for quick answers

---

## 📊 Performance Issues

### Issue: High memory usage

**Solution:**
```bash
# Restart the program
# Clear chat history in interactive mode: /clear

# For long sessions, restart periodically
```

### Issue: CPU spike

**Cause:** Usually happens during SSL handshake

**Solution:**
- Normal, temporary spike
- Wait a few seconds
- If persistent, use offline mode

---

## 🔄 Update Issues

### Issue: Old version running

**Solution:**
```bash
# Check version
python infinitychat.py --help
# Should show v2.0.0

# Re-download latest version
curl -O https://raw.githubusercontent.com/yourusername/infinitychat/main/infinitychat.py

# Verify file size (~20KB)
ls -lh infinitychat.py
```

---

## 🆘 Still Having Issues?

### Diagnostic Steps

1. **Verify Python version**
   ```bash
   python --version
   # Should be 3.6 or higher
   ```

2. **Test basic functionality**
   ```bash
   python infinitychat.py --help
   python infinitychat.py --models
   python infinitychat.py "Hello"
   ```

3. **Check file integrity**
   ```bash
   # File should be ~20KB
   ls -lh infinitychat.py
   
   # Count lines (should be ~695)
   wc -l infinitychat.py
   ```

4. **Test network**
   ```bash
   ping google.com
   curl https://api.neuro.ai/chat
   ```

5. **Try offline mode explicitly**
   ```bash
   # Disconnect internet temporarily
   # Run a question - should work instantly
   python infinitychat.py "Tell me a joke"
   ```

### Getting Help

If none of the above solutions work:

1. **Check FAQ** - [FAQ.md](FAQ.md)
2. **GitHub Issues** - Report your issue with:
   - Your OS and Python version
   - Exact error message
   - What you tried
   - Steps to reproduce

3. **Include diagnostic info:**
   ```bash
   python --version
   python infinitychat.py --help | head -5
   ```

---

## ✅ Success Indicators

You know it's working when you see:

```
╔═══════════════════════════════════════════════════════════╗
║   🚀 InfinityChat v2.0.0                                  ║
║   Unlimited AI Chat - No Login Required                   ║
╚═══════════════════════════════════════════════════════════╝
```

And get responses like:

```
🤖 Answer: [Helpful response]

---
🤖 Model: [model_name] | ⏱️ [time]s | 💯 Confidence: [percentage]%
```

---

<div align="center">

**Still stuck?** → [FAQ](FAQ.md) | [GitHub Issues](https://github.com/yourusername/infinitychat/issues)

[Back to Documentation Index](README.md)

</div>
