"""
Unlimited AI Chat - No Login Required

A completely free, unlimited AI chat system that requires NO login, 
NO API keys, and NO registration.

For full documentation, see README.md
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="unlimited-ai-chat",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Free unlimited AI chat with no login required",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/unlimited-ai-chat",
    py_modules=["ai_chat"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    entry_points={
        "console_scripts": [
            "ai-chat=ai_chat:main",
        ],
    },
    keywords="ai chat unlimited free no-login huggingface myshell",
)
