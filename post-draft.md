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

## Fiverr Gig Drafts — Python Developer

These gigs turn your Python skills into $5-10 orders.

### Gig 1: Debug Your Python Script ($5)

**Title:**
I will debug your Python script or fix your code errors

**Category:** Programming & Tech > Scripting & Automation

**Description:**
```text
Have a Python script that's broken? Send it over and I'll fix it fast.

What I'll do:
✅ Debug syntax errors, runtime errors, logic bugs
✅ Identify and fix the root cause
✅ Explain what was wrong (so you learn)
✅ Return clean, working code

Perfect for:
• Students stuck on assignments
• Devs with a script that broke after an update
• Anyone who needs a quick Python fix

Just send me your script + error message + what it should do.
Revisions included until it works.
```

**Price:** $5 (30 min delivery) | Extras: +$10 for complex multi-file debugging

### Gig 2: Clean Up and Organize Your Files ($5)

**Title:**
I will organize your messy folders using my CLI tool

**Category:** Lifestyle > Virtual Assistant

**Description:**
```text
Your Downloads folder is a disaster? I'll clean it up in minutes using my custom file organization tool.

What I'll do:
✅ Sort files into folders by type (images, docs, code, audio, etc.)
✅ Find and remove duplicate files wasting your disk space
✅ Rename files into a clean naming convention
✅ Preview everything before making changes

How it works:
1. I'll send you a one-command script (no install needed)
2. Run it with --dry-run to see what would happen
3. Confirm and I'll run the actual cleanup

Safe, reversible, and satisfying to watch.
```

**Price:** $5 (1 day delivery) | Extras: +$10 for scheduled recurring cleanups

### Gig 3: Write a Python Automation Script ($10)

**Title:**
I will write a Python script to automate your repetitive task

**Category:** Programming & Tech > Scripting & Automation

**Description:**
```text
Stop doing the same thing over and over. I'll write a Python script to automate it.

What I can build:
• File processing and renaming automation
• Data extraction from CSVs/Excel/PDFs
• Web scraping scripts (simple sites)
• API integration scripts
• Log analysis and report generation
• Custom CLI tools like my dev-utils toolkit

I build zero-dependency scripts that run anywhere Python does.
```

**Price:** $10 (2 day delivery)

---

## Fiverr Gig Drafts — Cybersecurity

### Gig 4: Basic Website Security Scan ($5)

**Title:**
I will scan your website for common security vulnerabilities

**Category:** Cybersecurity & Data Protection > Vulnerability Assessment

**Description:**
```text
Find out if your website has common security issues before a hacker does.

What I check:
🔍 Missing security headers (CSP, HSTS, X-Frame-Options, etc.)
🔍 Open ports and exposed services
🔍 Outdated software versions
🔍 Common misconfigurations
🔍 SSL/TLS issues

You get a plain-English report with:
• What I found
• How serious each issue is
• How to fix it

⚠️ For educational purposes and your own websites only. Authorization required.
```

**Price:** $5 (1 day delivery)

---

## Bonus: Product Hunt Launch Draft

**Title:** Dev Utils — The zero-dependency CLI toolkit for every developer

**Tagline:** One file. Zero dependencies. Four essential tools. Clean up files, find duplicates, batch rename, and analyze git repos—all with Python stdlib.

**Description:**
```text
Dev Utilities is a single-file (~600 LOC) Python CLI toolkit that does four things well:

📁 organize — Automatically sort files into categorized folders (20+ file types)
🔍 dedupe — Find and remove duplicates by SHA-256 content hash  
✏️ rename — Batch rename files with prefix, suffix, find/replace, and numbering
📊 gitstats — Beautiful git repository statistics dashboard

Why it's different:
• Zero dependencies — uses ONLY Python standard library
• Single file — curl it and go, no pip install
• Safe defaults — --dry-run on destructive operations
• MIT licensed — use it anywhere

Perfect for devs who want to clean up shared servers, organize downloads, or understand their git repos without installing heavy tools.
```

**Topics:** Developer Tools, Open Source, Command Line, Python

---

## ⚡ Lightning Address setup reminder

After you create your Lightning Address at https://getalby.com/:
1. Edit README.md — replace the "(coming soon)" placeholder with your actual address
2. Add it to FUNDING.yml
3. Generate a QR code at https://lightningaddress.com/qr/ and add it to the repo

The Lightning Address format is: yourname@getalby.com
