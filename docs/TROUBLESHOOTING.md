# 🐛 Troubleshooting Guide

Common issues and their solutions for Unlimited AI Chat.

---

## 📋 Table of Contents

1. [Installation Issues](#installation-issues)
2. [Runtime Errors](#runtime-errors)
3. [API Problems](#api-problems)
4. [Performance Issues](#performance-issues)
5. [Output Problems](#output-problems)
6. [Platform-Specific Issues](#platform-specific-issues)
7. [Network Issues](#network-issues)

---

## 🔧 Installation Issues

### Issue: "python: command not found"

**Symptoms:**
```bash
$ python ai_chat.py "Hello"
bash: python: command not found
```

**Solutions:**

1. **Try python3 instead:**
   ```bash
   python3 ai_chat.py "Hello"
   ```

2. **Check Python installation:**
   ```bash
   which python
   which python3
   ```

3. **Install Python:**
   - Windows: Download from [python.org](https://www.python.org/downloads/)
   - Mac: `brew install python`
   - Linux: `sudo apt install python3`

4. **Add to PATH (Windows):**
   - Reinstall Python
   - Check "Add Python to PATH" during installation

---

### Issue: "ModuleNotFoundError: No module named 'requests'"

**Symptoms:**
```python
ModuleNotFoundError: No module named 'requests'
```

**Solutions:**

1. **Install requests:**
   ```bash
   pip install requests
   ```

2. **Use pip3:**
   ```bash
   pip3 install requests
   ```

3. **Run without internet (uses local fallback):**
   ```bash
   python ai_chat.py "Hello"
   # Local responses don't need requests library
   ```

4. **Verify installation:**
   ```bash
   python -c "import requests; print(requests.__version__)"
   ```

---

### Issue: Permission denied (Linux/Mac)

**Symptoms:**
```bash
$ ./ai_chat.py
bash: ./ai_chat.py: Permission denied
```

**Solutions:**

1. **Make executable:**
   ```bash
   chmod +x ai_chat.py
   ```

2. **Run with python directly:**
   ```bash
   python ai_chat.py "Hello"
   ```

3. **Use sudo (not recommended):**
   ```bash
   sudo chmod +x ai_chat.py
   ```

---

### Issue: Git not found

**Symptoms:**
```bash
$ git clone https://github.com/...
git: command not found
```

**Solutions:**

1. **Install Git:**
   - Windows: [git-scm.com](https://git-scm.com/)
   - Mac: `xcode-select --install`
   - Ubuntu: `sudo apt install git`
   - Fedora: `sudo dnf install git`

2. **Manual download instead:**
   - Download ZIP from GitHub
   - Extract files
   - Run directly

---

## ⚠️ Runtime Errors

### Issue: Script crashes immediately

**Symptoms:**
```python
Traceback (most recent call last):
  File "ai_chat.py", line X, in <module>
    main()
  ...
```

**Solutions:**

1. **Check Python version:**
   ```bash
   python --version
   # Should be 3.7 or higher
   ```

2. **Check file integrity:**
   ```bash
   # Re-download ai_chat.py
   # Make sure it's complete
   ```

3. **Run with verbose output:**
   ```bash
   python -v ai_chat.py "Hello"
   ```

4. **Check syntax:**
   ```bash
   python -m py_compile ai_chat.py
   ```

---

### Issue: KeyboardInterrupt errors

**Symptoms:**
```python
KeyboardInterrupt
```

**Solutions:**

1. **Normal behavior** - Press Ctrl+C exits gracefully
2. **Wait for response** - Don't interrupt during API calls
3. **Use quit command** instead:
   ```
   You: quit
   ```

---

### Issue: Infinite loop

**Symptoms:**
- Script doesn't respond
- CPU usage high
- No output

**Solutions:**

1. **Force exit:**
   - Press `Ctrl+C`
   - Or `Ctrl+Z` (Windows)

2. **Check input:**
   - Avoid empty strings
   - Use proper quotes

3. **Restart script:**
   ```bash
   python ai_chat.py
   ```

---

## 🌐 API Problems

### Issue: All APIs failing

**Symptoms:**
```
AI: Thinking...
AI: [Generic local response]
```

**Solutions:**

1. **Check internet connection:**
   ```bash
   ping google.com
   ```

2. **Test APIs manually:**
   ```bash
   curl https://api-inference.huggingface.co
   ```

3. **Firewall issues:**
   - Allow Python through firewall
   - Disable proxy temporarily
   - Check antivirus settings

4. **DNS problems:**
   ```bash
   nslookup api-inference.huggingface.co
   ```

5. **Use offline mode:**
   - Local responses always work
   - No internet needed

---

### Issue: Slow responses

**Symptoms:**
- Takes 10+ seconds
- Sometimes times out

**Solutions:**

1. **Normal behavior:**
   - Online APIs take 2-5 seconds
   - First request may be slower

2. **Check network speed:**
   ```bash
   speedtest-cli
   ```

3. **Increase timeout:**
   Edit `ai_chat.py`:
   ```python
   timeout = 60  # Increase from 30
   ```

4. **Use local fallback:**
   - Disconnect internet
   - Instant responses

---

### Issue: API rate limiting

**Symptoms:**
```json
{"error": "Rate limit exceeded"}
```

**Solutions:**

1. **Wait and retry:**
   - Wait 1-2 minutes
   - Try again

2. **Local fallback activates automatically**

3. **Reduce frequency:**
   - Wait between requests
   - Batch queries

---

## ⚡ Performance Issues

### Issue: High memory usage

**Symptoms:**
- System slows down
- Memory warning

**Solutions:**

1. **Restart script:**
   ```bash
   # Exit and restart
   ```

2. **Clear conversation history:**
   - Start new session
   - Don't run for hours

3. **Check for memory leaks:**
   ```bash
   top  # Monitor memory
   ```

---

### Issue: Slow startup

**Symptoms:**
- Takes long to show prompt

**Solutions:**

1. **Normal import time:**
   - First run is slower
   - Subsequent runs faster

2. **Check disk speed:**
   ```bash
   hdparm -T /dev/sda
   ```

3. **SSD recommended** for best performance

---

## 📝 Output Problems

### Issue: Garbled text

**Symptoms:**
- Strange characters
- Encoding issues

**Solutions:**

1. **Set encoding:**
   ```bash
   export PYTHONIOENCODING=utf-8
   python ai_chat.py "Hello"
   ```

2. **Terminal encoding:**
   - Windows: `chcp 65001`
   - Mac/Linux: Usually UTF-8 by default

3. **Update terminal:**
   - Use modern terminal emulator
   - Enable UTF-8 support

---

### Issue: Cut-off responses

**Symptoms:**
- Response ends abruptly
- Incomplete sentences

**Solutions:**

1. **Request continuation:**
   ```
   You: Continue from where you left off
   ```

2. **Ask for shorter responses:**
   ```
   You: Explain briefly in 2-3 sentences
   ```

3. **Increase max tokens:**
   Edit `ai_chat.py`:
   ```python
   "max_new_tokens": 1000  # Increase from 500
   ```

---

### Issue: No output at all

**Symptoms:**
- Silent execution
- No response shown

**Solutions:**

1. **Check stdout:**
   ```bash
   python ai_chat.py "Hello" > output.txt
   cat output.txt
   ```

2. **Disable buffering:**
   ```bash
   python -u ai_chat.py "Hello"
   ```

3. **Add debug prints:**
   Edit `ai_chat.py` to add:
   ```python
   print("Debug: Starting...")
   ```

---

## 💻 Platform-Specific Issues

### Windows Issues

#### Issue: PowerShell execution policy

**Symptoms:**
```
running scripts is disabled on this system
```

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Issue: Path too long

**Symptoms:**
```
The specified path, file name, or both are too long
```

**Solution:**
- Move to shorter path
- Example: `C:\ai-chat\`

#### Issue: Command Prompt encoding

**Symptoms:**
- Special characters display incorrectly

**Solution:**
```cmd
chcp 65001
```

---

### macOS Issues

#### Issue: Certificate verification failed

**Symptoms:**
```
ssl.SSLCertVerificationError
```

**Solution:**
```bash
# Install certificates
/Applications/Python\ 3.x/Install\ Certificates.command
```

#### Issue: Gatekeeper blocking

**Symptoms:**
- App can't be opened

**Solution:**
- System Preferences → Security & Privacy
- Allow Python

---

### Linux Issues

#### Issue: SELinux blocking

**Symptoms:**
- Permission denied despite correct permissions

**Solution:**
```bash
# Check SELinux status
getenforce

# Temporarily disable
sudo setenforce 0
```

#### Issue: Missing dependencies

**Symptoms:**
```
libpython3.x.so: cannot open shared object file
```

**Solution:**
```bash
sudo apt install libpython3.x
```

---

## 🌍 Network Issues

### Issue: Proxy required

**Symptoms:**
- Behind corporate firewall
- Direct connection blocked

**Solutions:**

1. **Set proxy:**
   ```bash
   export HTTP_PROXY=http://proxy.company.com:8080
   export HTTPS_PROXY=https://proxy.company.com:8080
   python ai_chat.py "Hello"
   ```

2. **Windows CMD:**
   ```cmd
   set HTTP_PROXY=http://proxy.company.com:8080
   set HTTPS_PROXY=https://proxy.company.com:8080
   ```

3. **Authentication:**
   ```bash
   export HTTP_PROXY=http://user:pass@proxy:port
   ```

---

### Issue: SSL/TLS errors

**Symptoms:**
```
ssl.SSLError: CERTIFICATE_VERIFY_FAILED
```

**Solutions:**

1. **Update certificates:**
   ```bash
   pip install --upgrade certifi
   ```

2. **Disable verification (not recommended):**
   ```python
   # In ai_chat.py, add:
   verify=False
   ```

3. **Corporate certificate:**
   - Install company CA certificate
   - Add to trust store

---

### Issue: Connection timeout

**Symptoms:**
```
requests.exceptions.ConnectionTimeout
```

**Solutions:**

1. **Increase timeout:**
   ```python
   timeout = 60  # In ai_chat.py
   ```

2. **Check connectivity:**
   ```bash
   ping api-inference.huggingface.co
   ```

3. **Retry logic:**
   - Script automatically retries with fallback
   - Local responses work offline

---

## 🧪 Diagnostic Commands

### Check System Status

```bash
# Python version
python --version

# Check requests library
python -c "import requests; print(requests.__version__)"

# Test internet
ping -c 4 google.com

# Test API endpoint
curl -I https://api-inference.huggingface.co

# Check file permissions
ls -la ai_chat.py

# View error logs
python ai_chat.py 2>&1 | tee error.log
```

### Debug Mode

Add to `ai_chat.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Add debug statements
logger.debug(f"Trying API with prompt: {prompt}")
```

---

## 🆘 Still Having Issues?

### Collect Information

Before asking for help, gather:

1. **System info:**
   ```bash
   python --version
   uname -a  # or ver on Windows
   ```

2. **Error message:**
   - Full traceback
   - Screenshot if helpful

3. **Steps to reproduce:**
   - Exact commands used
   - Expected vs actual behavior

4. **Environment:**
   - OS version
   - Python version
   - Network setup

### Get Help

1. **Check existing issues:**
   [GitHub Issues](https://github.com/YOUR_USERNAME/unlimited-ai-chat/issues)

2. **Create new issue:**
   - Use template
   - Include diagnostic info
   - Be specific

3. **Ask in discussions:**
   [GitHub Discussions](https://github.com/YOUR_USERNAME/unlimited-ai-chat/discussions)

---

## 📞 Quick Reference

| Problem | Quick Fix |
|---------|-----------|
| Python not found | Try `python3` or install Python |
| No requests module | `pip install requests` |
| Permission denied | `chmod +x ai_chat.py` |
| Slow responses | Normal, or use offline mode |
| No internet | Local fallback works automatically |
| Garbled text | Set `PYTHONIOENCODING=utf-8` |
| API errors | Check internet, firewall, proxy |

---

<div align="center">

**Still stuck? → [FAQ](FAQ.md)**

[Back to Docs](README.md) | [View FAQ →](FAQ.md)

</div>
