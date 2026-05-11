# Post Draft — Dev Utilities CLI Toolkit

---

## Version A: Reddit (r/Python)

**Title:**
I built a zero-dependency Python CLI toolkit that organizes files, finds duplicates, batch renames, and analyzes git repos — all in one file (~600 lines)

**Post body:**

```text
I got tired of installing separate tools for basic file operations, so I wrote a single-file Python CLI that does four things well:

📁 organize — Sorts files into categorized folders by type (images, docs, code, archives, etc.)
🔍 dedupe — Finds duplicate files by SHA-256 hash and optionally deletes them
✏️ rename — Batch renames with prefix/suffix/find-replace/auto-numbering
📊 gitstats — Beautiful git repo statistics dashboard (top contributors, commit timeline, file breakdown)

The whole thing is one file (~600 lines) with zero external dependencies — just Python stdlib.

```bash
curl -O https://raw.githubusercontent.com/Elemperor1/dev-utils-cli-toolkit/main/devutils.py
python3 devutils.py organize ~/Downloads --dry-run
```

My favorite feature is `organize --dry-run` — it shows you exactly what would move before actually doing it. Saved me from nuking my Downloads folder more than once.

Also works great for cleaning up shared drives and server directories where you don't want to install anything.

Would love feedback! https://github.com/Elemperor1/dev-utils-cli-toolkit
```

---

## Version B: Hacker News (Show HN)

**Title:**
Show HN: Dev Utils – Zero-dependency Python CLI (organize, dedupe, rename, gitstats)

**Post body:**

```text
Single-file Python CLI toolkit (~600 LOC, stdlib only) with 4 commands:

- organize: sorts files into type-based categories
- dedupe: SHA-256-based duplicate detection + deletion
- rename: batch rename with multiple modes
- gitstats: git repo analytics (contribution distribution, timelines, file diversity, bus factor)

Design goals:
- Zero dependencies (pip install nothing)
- Safe defaults (dry-run mode before destructive operations)
- Single file (curl it and go)

I use it for keeping shared dev servers tidy without installing anything. The `gitstats` command was surprisingly useful for understanding contribution distribution across repos.

https://github.com/Elemperor1/dev-utils-cli-toolkit

Curious what other commands people would find useful in a tool like this.
```

---

## Where to post

| Platform | Subreddit/Area | Best Time (ET) | Notes |
|----------|---------------|----------------|-------|
| Reddit | r/Python | Mon-Thu 8-11am | Largest dev audience |
| Reddit | r/commandline | Anytime | Smaller but engaged |
| Reddit | r/devtools | Anytime | Niche but directly relevant |
| Hacker News | Show HN | Weekdays 7-9am | Highest quality traffic |
| Twitter/X | #Python #cli | Anytime | Tag @python_tip etc |

## Pro tip: comment on your own post

After posting on Reddit, immediately add a comment like:
"Happy to answer questions or take feature requests — this is my first public tool so be gentle 😅"

This boosts engagement signals and keeps the post alive longer.

---

## ⚡ Lightning Address setup reminder

After you create your Lightning Address at https://getalby.com/:
1. Edit README.md — replace the "(coming soon)" placeholder with your actual address
2. Add it to FUNDING.yml
3. Generate a QR code at https://lightningaddress.com/qr/ and add it to the repo

The Lightning Address format is: yourname@getalby.com
