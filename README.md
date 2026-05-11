<div align="center">
  <h1>🧰 Dev Utilities CLI Toolkit</h1>
  <p><strong>One file. Zero dependencies. Four powerful tools.</strong></p>
  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
    <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.6+-green.svg" alt="Python"></a>
    <img src="https://img.shields.io/badge/dependencies-0-brightgreen" alt="Zero Dependencies">
    <img src="https://img.shields.io/github/stars/Elemperor1/dev-utils-cli-toolkit?style=social" alt="Stars">
    <img src="https://github.com/Elemperor1/dev-utils-cli-toolkit/actions/workflows/ci.yml/badge.svg" alt="CI">
  </p>
</div>

---

**Tired of downloading bloated tools for simple file tasks?** Dev Utilities is a single Python file with zero external dependencies that gives you four essential developer tools:

| Command | What It Does | Why You Need It |
|---------|-------------|-----------------|
| `organize` | Sorts files into categorized folders by type | Un-F your Downloads folder in seconds |
| `dedupe` | Finds + removes duplicates by SHA-256 content hash | Reclaim GBs of wasted space |
| `rename` | Batch rename with prefix, suffix, find/replace, numbering | Stop renaming files one-by-one |
| `gitstats` | Beautiful git repo statistics dashboard | Know who wrote what, when |

## 🚀 Quick Start

```bash
# Download and go — no pip install needed
curl -O https://raw.githubusercontent.com/Elemperor1/dev-utils-cli-toolkit/main/devutils.py

# See all commands
python3 devutils.py help
```

### Organize your Downloads folder (preview first, then commit)
```bash
python3 devutils.py organize ~/Downloads --dry-run    # See what moves
python3 devutils.py organize ~/Downloads               # Actually do it
```

### Find and remove duplicates
```bash
python3 devutils.py dedupe ~/Documents                 # List duplicates
python3 devutils.py dedupe ~/Documents --delete        # Delete them
```

### Batch rename files
```bash
python3 devutils.py rename --prefix 'project_' --number --suffix '_v1'
python3 devutils.py rename --find 'old' --replace 'new'
```

### Git statistics dashboard
```bash
cd my-project && python3 ~/devutils.py gitstats
```
> Shows: top contributors, commit timeline, file type breakdown, bus factor, and more.

## 💻 Requirements

- **Python 3.6+** (pre-installed on macOS, Linux, WSL)
- **No dependencies** — uses only Python standard library

## 📦 What You Get

- `devutils.py` — single file, ~600 lines, MIT licensed
- Free to use, modify, fork, relicense — go wild

## ⚡ Support

If this tool saved you time or disk space, here's how you can say thanks:

| Method | How |
|--------|-----|
| ☕ **PayPal** | [Buy me a coffee ($5)](https://paypal.me/JacobARudolph) |
| ⚡ **Lightning** | *(coming soon — set up your ⚡ address via [GetAlby](https://getalby.com/) and paste it here)* |
| ⭐ **GitHub** | Star the repo — it helps more people find it |

Bitcoin Lightning donations are instant, feeless, and privacy-preserving. ⚡

## 📄 License

MIT — do whatever you want with it.
