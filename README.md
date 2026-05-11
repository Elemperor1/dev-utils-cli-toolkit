# Dev Utilities CLI Toolkit

<p align="center">
  <strong>🧰 A powerful all-in-one CLI toolkit for every developer</strong><br>
  Organize files · Find duplicates · Batch rename · Git statistics
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.6+-green.svg" alt="Python"></a>
</p>

---

## ✨ Features

| Command | Description |
|---------|-------------|
| `organize` | Automatically sort files into categorized folders by type |
| `dedupe` | Find and remove duplicate files by content hash |
| `rename` | Batch rename files with prefix, suffix, find/replace, or numbering |
| `gitstats` | Beautiful git repository statistics dashboard |

## 🚀 Quick Start

```bash
# Download and run
python3 devutils.py help

# Organize your Downloads folder
python3 devutils.py organize ~/Downloads

# Find duplicates in Documents
python3 devutils.py dedupe ~/Documents

# Batch rename files
python3 devutils.py rename --prefix 'project_' --number

# View git repository stats
python3 devutils.py gitstats ~/my-project
```

## 📖 Examples

**Organize files (preview before moving):**
```bash
python3 devutils.py organize ~/Downloads --dry-run
```

**Safely find duplicates:**
```bash
python3 devutils.py dedupe ~/Documents
```
Then review and delete with:
```bash
python3 devutils.py dedupe ~/Documents --delete
```

**Smart batch rename:**
```bash
python3 devutils.py rename --prefix 'backup_' --suffix '_v1' --number
```

**Quick git repo overview:**
```bash
python3 devutils.py gitstats
```

## 💻 Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## 📦 What's Included

- `devutils.py` — The full CLI toolkit (single file, ~500 lines)
- MIT License — Free to use, modify, and share

## 🤝 Support

If you find this tool useful, consider sponsoring:

[https://github.com/sponsors/Elemperor1](https://github.com/sponsors/Elemperor1)

## 📄 License

MIT — do whatever you want with it!
