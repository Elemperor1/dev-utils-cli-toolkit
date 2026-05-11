#!/usr/bin/env python3
"""
Dev Utilities CLI Toolkit v1.0
A collection of powerful command-line tools for every developer.

Usage:
    python3 devutils.py <command> [options]

Commands:
    organize    Organize files in a directory by type
    dedupe      Find and remove duplicate files
    rename      Batch rename files with patterns
    gitstats    Show git repository statistics
    help        Show this help message

Author: Jacob Rudolph
License: MIT
"""

import os
import sys
import hashlib
import json
import shutil
import subprocess
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

# ─── Terminal Colors ───────────────────────────────────────────────────────────

class Style:
    """Terminal styling for beautiful CLI output."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GRAY = "\033[90m"

    @staticmethod
    def ok(text): return f"{Style.GREEN}{Style.BOLD}✓{Style.RESET} {text}"
    @staticmethod
    def info(text): return f"{Style.BLUE}{Style.BOLD}ℹ{Style.RESET} {text}"
    @staticmethod
    def warn(text): return f"{Style.YELLOW}{Style.BOLD}⚠{Style.RESET} {text}"
    @staticmethod
    def err(text): return f"{Style.RED}{Style.BOLD}✗{Style.RESET} {text}"
    @staticmethod
    def header(text): return f"\n{Style.CYAN}{Style.BOLD}{'─'*50}{Style.RESET}\n{Style.BOLD}{text}{Style.RESET}\n{Style.CYAN}{Style.BOLD}{'─'*50}{Style.RESET}"
    @staticmethod
    def title(text): return f"\n{Style.MAGENTA}{Style.BOLD}{text}{Style.RESET}"
    @staticmethod
    def progress(text): return f"  {Style.CYAN}→{Style.RESET} {text}"
    @staticmethod
    def stat(key, value): return f"  {Style.GRAY}{key}:{Style.RESET} {Style.BOLD}{value}{Style.RESET}"


# ─── Utility Functions ─────────────────────────────────────────────────────────

FILE_CATEGORIES = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico', '.tiff', '.raw', '.heic', '.avif'],
    "Videos": ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm', '.m4v', '.mpeg', '.3gp'],
    "Audio": ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.opus', '.aiff'],
    "Documents": ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.rtf', '.odt', '.csv', '.tsv'],
    "Archives": ['.zip', '.tar', '.gz', '.bz2', '.xz', '.7z', '.rar', '.tgz', '.zst'],
    "Code": ['.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.c', '.cpp', '.h', '.hpp', '.cs', '.go', '.rs', '.rb', '.php', '.swift', '.kt', '.scala', '.sh', '.bash', '.zsh', '.pl', '.lua', '.r', '.m', '.sql'],
    "Web": ['.html', '.htm', '.css', '.scss', '.sass', '.less', '.json', '.xml', '.yaml', '.yml', '.toml', '.md', '.markdown'],
    "Config": ['.env', '.gitignore', '.dockerignore', '.editorconfig', '.ini', '.cfg', '.conf', '.npmrc', '.eslintrc', '.prettierrc'],
    "Executables": ['.exe', '.msi', '.app', '.dmg', '.deb', '.rpm', '.apk', '.bin', '.out'],
    "Fonts": ['.ttf', '.otf', '.woff', '.woff2', '.eot'],
    "3D Models": ['.obj', '.fbx', '.glb', '.gltf', '.blend', '.stl', '.3ds', '.dae'],
    "Design": ['.psd', '.ai', '.xd', '.fig', '.sketch', '.afdesign', '.afphoto'],
    "Virtual Machines": ['.iso', '.vmdk', '.vdi', '.vhd', '.ova', '.vagrant'],
}


def get_file_category(filename):
    """Determine file category by extension."""
    ext = Path(filename).suffix.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Other"


def format_size(size_bytes):
    """Format file size in human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} PB"


def format_time(seconds):
    """Format seconds into human-readable duration."""
    if seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        m, s = divmod(seconds, 60)
        return f"{int(m)}m {int(s)}s"
    else:
        h, m = divmod(seconds, 3600)
        return f"{int(h)}h {int(m)}m"


# ─── COMMAND: organize ─────────────────────────────────────────────────────────

def cmd_organize(args):
    """Organize files in a directory into categorized folders."""
    target_dir = Path(args[0]) if args else Path.cwd()
    if not target_dir.exists():
        print(Style.err(f"Directory not found: {target_dir}"))
        return 1

    dry_run = '--dry-run' in sys.argv or '-n' in sys.argv
    quiet = '--quiet' in sys.argv or '-q' in sys.argv

    print(Style.header(f"📂 Organizing: {target_dir.resolve()}"))
    if dry_run:
        print(Style.warn("Dry run mode - no files will be moved"))
    print()

    # Collect files (non-recursive by default)
    recursive = '--recursive' in sys.argv or '-r' in sys.argv
    pattern = None
    if '--pattern' in sys.argv:
        idx = sys.argv.index('--pattern')
        if idx + 1 < len(sys.argv):
            pattern = sys.argv[idx + 1]

    files_moved = 0
    categories_found = defaultdict(list)

    files = list(target_dir.iterdir())
    total = len([f for f in files if f.is_file()])

    for i, f in enumerate(files):
        if not f.is_file() or f.name.startswith('.'):
            continue
        if pattern and pattern not in f.name:
            continue

        cat = get_file_category(f.name)
        categories_found[cat].append(f)
        cat_dir = target_dir / cat

        if not dry_run:
            cat_dir.mkdir(exist_ok=True)
            dest = cat_dir / f.name
            if dest.exists():
                base = f.stem
                dest = cat_dir / f"{base}_{i}{f.suffix}"
            f.rename(dest)

        files_moved += 1

        if not quiet:
            print(Style.progress(f"[{files_moved}/{total}] {f.name} → {cat}/"))

    print()
    print(Style.ok(f"Organized {Style.BOLD}{files_moved}{Style.RESET} files into {Style.BOLD}{len(categories_found)}{Style.RESET} categories"))
    if categories_found:
        print()
        for cat, flist in sorted(categories_found.items()):
            print(Style.stat(cat, f"{len(flist)} files"))

    return 0


# ─── COMMAND: dedupe ───────────────────────────────────────────────────────────

def cmd_dedupe(args):
    """Find and optionally remove duplicate files."""
    target_dir = Path(args[0]) if args else Path.cwd()
    if not target_dir.exists():
        print(Style.err(f"Directory not found: {target_dir}"))
        return 1

    delete = '--delete' in sys.argv or '-d' in sys.argv
    dry_run = '--dry-run' in sys.argv or '-n' in sys.argv
    quiet = '--quiet' in sys.argv or '-q' in sys.argv

    if delete:
        print(Style.header(f"🗑️  Finding duplicates in: {target_dir.resolve()}"))
    else:
        print(Style.header(f"🔍 Scanning for duplicates: {target_dir.resolve()}"))
    if dry_run and delete:
        print(Style.warn("Dry run mode - no files will be deleted"))
    print()

    # Phase 1: Group files by size
    print(Style.info("Phase 1: Grouping files by size..."))
    size_groups = defaultdict(list)
    file_count = 0
    for f in target_dir.rglob('*'):
        if f.is_file() and not f.name.startswith('.'):
            size_groups[f.stat().st_size].append(f)
            file_count += 1

    print(Style.ok(f"Scanned {Style.BOLD}{file_count}{Style.RESET} files"))

    # Phase 2: Hash files with same size
    print(Style.info("Phase 2: Computing file hashes..."))
    hash_groups = defaultdict(list)
    checked = 0
    total_to_check = sum(len(files) for files in size_groups.values() if len(files) > 1)

    for size, files in size_groups.items():
        if len(files) < 2:
            continue
        for f in files:
            h = hashlib.md5(f.read_bytes()).hexdigest()
            hash_groups[h].append(f)
            checked += 1
            if not quiet:
                print(Style.progress(f"Progress: {checked}/{total_to_check}"), end='\r')

    if not quiet:
        print()

    # Find duplicates
    duplicates = {h: flist for h, flist in hash_groups.items() if len(flist) > 1}

    if not duplicates:
        print()
        print(Style.ok("No duplicate files found!"))
        return 0

    total_dup_size = 0
    print()
    print(Style.title(f"Found {len(duplicates)} groups of duplicate files:"))
    print()

    for i, (h, flist) in enumerate(duplicates.items(), 1):
        size = flist[0].stat().st_size
        total_dup_size += size * (len(flist) - 1)
        print(f"  {Style.YELLOW}Group {i}{Style.RESET} ({format_size(size)} each):")
        for j, f in enumerate(flist):
            marker = Style.RED + " [KEEP]" if j == 0 else Style.DIM + " [DELETE]" if delete else ""
            print(f"    {j+1}. {f.resolve()}{Style.RESET}{marker}")
        print()

    print(Style.warn(f"Wasted space: {Style.BOLD}{format_size(total_dup_size)}{Style.RESET}"))

    if delete:
        if dry_run:
            print(Style.info(f"Would delete {Style.BOLD}{sum(len(flist)-1 for flist in duplicates.values())}{Style.RESET} files"))
        else:
            deleted = 0
            for h, flist in duplicates.items():
                for f in flist[1:]:
                    f.unlink()
                    deleted += 1
                    if not quiet:
                        print(Style.progress(f"Deleted: {f.name}"))
            print()
            print(Style.ok(f"Deleted {Style.BOLD}{deleted}{Style.RESET} duplicate files"))
            print(Style.ok(f"Recovered {Style.BOLD}{format_size(total_dup_size)}{Style.RESET} of space"))

    return 0


# ─── COMMAND: rename ───────────────────────────────────────────────────────────

def cmd_rename(args):
    """Batch rename files using patterns."""
    target_dir = Path(args[0]) if args else Path.cwd()
    if not target_dir.exists():
        print(Style.err(f"Directory not found: {target_dir}"))
        return 1

    # Parse options
    prefix = None
    suffix = None
    replace_from = None
    replace_to = None
    number = False
    ext_filter = None

    if '--prefix' in sys.argv:
        prefix = sys.argv[sys.argv.index('--prefix') + 1]
    if '--suffix' in sys.argv:
        suffix = sys.argv[sys.argv.index('--suffix') + 1]
    if '--replace' in sys.argv:
        idx = sys.argv.index('--replace')
        parts = sys.argv[idx + 1].split(',')
        if len(parts) == 2:
            replace_from, replace_to = parts
    if '--number' in sys.argv or '-n' in sys.argv:
        number = True
    if '--ext' in sys.argv:
        ext_filter = sys.argv[sys.argv.index('--ext') + 1]

    if not any([prefix, suffix, replace_from, number]):
        print(Style.err("No rename operation specified!"))
        print("  Use: --prefix TEXT, --suffix TEXT, --replace OLD,NEW, --number")
        print("  Example: python3 devutils.py rename --prefix 'project_' --number")
        return 1

    dry_run = '--dry-run' in sys.argv or '-n' not in sys.argv and '--dry-run' not in sys.argv and sys.argv.count('-n') == 0
    dry_run = '--dry-run' in sys.argv
    quiet = '--quiet' in sys.argv or '-q' in sys.argv

    # If --dry-run is not specified and we have --number, we should do it (not dry run)
    if '--number' in sys.argv or '-n' in sys.argv:
        dry_run = '--dry-run' in sys.argv

    print(Style.header(f"✏️  Renaming files in: {target_dir.resolve()}"))

    files = sorted([f for f in target_dir.iterdir() if f.is_file()])
    if ext_filter:
        files = [f for f in files if f.suffix.lstrip('.') == ext_filter.lstrip('.')]

    renamed = 0
    for i, f in enumerate(files):
        if f.name.startswith('.'):
            continue

        name = f.stem
        ext = f.suffix

        if replace_from is not None:
            name = name.replace(replace_from, replace_to)

        if prefix:
            name = prefix + name
        if suffix:
            name = name + suffix
        if number:
            name = f"{name}_{i+1:03d}"

        new_name = name + ext
        new_path = f.parent / new_name

        if new_path.exists():
            new_path = f.parent / f"{name}_{i+1:02d}{ext}"

        if not quiet:
            print(Style.progress(f"{f.name} → {new_path.name}"))

        if not dry_run:
            f.rename(new_path)

        renamed += 1

    print()
    if dry_run:
        print(Style.info(f"Would rename {Style.BOLD}{renamed}{Style.RESET} files"))
        print(Style.info("Run without --dry-run to apply changes"))
    else:
        print(Style.ok(f"Renamed {Style.BOLD}{renamed}{Style.RESET} files"))

    return 0


# ─── COMMAND: gitstats ─────────────────────────────────────────────────────────

def cmd_gitstats(args):
    """Show git repository statistics with a beautiful dashboard."""
    target_dir = Path(args[0]) if args else Path.cwd()

    # Ensure we're in a git repo
    git_dir = target_dir
    while git_dir != git_dir.parent:
        if (git_dir / '.git').exists():
            break
        git_dir = git_dir.parent
    else:
        print(Style.err(f"No git repository found in: {target_dir}"))
        return 1

    print(Style.header(f"📊 Git Repository Statistics"))
    print(f"  {Style.GRAY}Repository:{Style.RESET} {git_dir.resolve()}")
    print()

    def run_git(*cmd):
        try:
            result = subprocess.run(
                ['git'] + list(cmd),
                capture_output=True, text=True, cwd=str(git_dir),
                timeout=30
            )
            return result.stdout.strip()
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return ""

    # Basic info
    remote = run_git('config', '--get', 'remote.origin.url') or "None"
    branch = run_git('rev-parse', '--abbrev-ref', 'HEAD') or "unknown"

    stats = {
        'remote': remote,
        'branch': branch,
    }

    # Commit count
    total_commits = run_git('rev-list', '--count', 'HEAD')
    stats['total_commits'] = total_commits or "0"

    # Author count
    authors = run_git('shortlog', '-sn', 'HEAD')
    author_count = len([l for l in authors.split('\n') if l.strip()]) if authors else 0
    stats['authors'] = str(author_count)

    # File count
    file_count = run_git('ls-files', '--cached', '|', 'wc', '-l')
    if not file_count:
        try:
            result = subprocess.run(
                ['git', 'ls-files'], capture_output=True, text=True, cwd=str(git_dir), timeout=15
            )
            file_count = str(len(result.stdout.splitlines()))
        except:
            file_count = "?"
    stats['files'] = file_count

    # Lines of code
    try:
        result = subprocess.run(
            ['git', 'ls-files'], capture_output=True, text=True, cwd=str(git_dir), timeout=15
        )
        total_lines = 0
        for filepath in result.stdout.splitlines()[:200]:  # Limit to 200 files
            try:
                with open(git_dir / filepath, 'r', errors='ignore') as f:
                    total_lines += sum(1 for _ in f)
            except:
                pass
        stats['lines'] = format_number(total_lines)
    except:
        stats['lines'] = "?"

    # Contributors
    top_contributors = []
    for line in authors.split('\n')[:5]:
        if line.strip():
            parts = line.strip().split('\t')
            if len(parts) == 2:
                top_contributors.append((parts[0].strip(), parts[1]))

    # Commit dates
    first_commit = run_git('log', '--reverse', '--format=%ad', '--date=short', 'HEAD' ) 
    if first_commit:
        first_date = first_commit.split('\n')[0] if '\n' in first_commit else first_commit
    else:
        first_date = "?"
    last_commit = run_git('log', '--format=%ad', '--date=short', '-1', 'HEAD')
    stats['first_commit'] = first_date
    stats['last_commit'] = last_commit or "?"

    # Uncommitted changes
    changes = run_git('status', '--porcelain')
    uncommitted = len([l for l in changes.split('\n') if l.strip()]) if changes else 0
    stats['uncommitted'] = str(uncommitted)

    # Print dashboard
    print(f"  {Style.BOLD}{'REPO INFO':<20}{Style.RESET} {'VALUE':<40}")
    print(f"  {'─'*60}")
    print(Style.stat("Remote", stats['remote']))
    print(Style.stat("Branch", stats['branch']))
    print(Style.stat("Total Commits", stats['total_commits']))
    print(Style.stat("Authors", stats['authors']))
    print(Style.stat("Tracked Files", stats['files']))
    print(Style.stat("Lines of Code", stats['lines']))
    print(Style.stat("First Commit", stats['first_commit']))
    print(Style.stat("Last Commit", stats['last_commit']))
    print(Style.stat("Uncommitted", stats['uncommitted']))

    # Top contributors
    if top_contributors:
        print()
        print(f"  {Style.BOLD}Top Contributors{Style.RESET}")
        for i, (count, author) in enumerate(top_contributors, 1):
            bar_len = min(int(count) // 2, 30)
            bar = '█' * bar_len
            print(f"  {i}. {author:<25} {count:>6} commits  {bar}")

    return 0


def format_number(n):
    """Format large numbers with commas."""
    if isinstance(n, str):
        try:
            n = int(n)
        except:
            return n
    return f"{n:,}"


# ─── COMMAND: help ─────────────────────────────────────────────────────────────

def cmd_help(args):
    """Show help with all available commands."""
    print(Style.header("Dev Utilities CLI Toolkit v1.0"))
    print()
    print(f"  {Style.DIM}A collection of powerful CLI tools for every developer.{Style.RESET}")
    print()
    print(f"  {Style.BOLD}Usage:{Style.RESET}")
    print(f"    python3 devutils.py <command> [options] [path]")
    print()
    print(f"  {Style.BOLD}Commands:{Style.RESET}")
    print()
    print(f"    {Style.CYAN}organize{Style.RESET}    Organize files by type into categorized folders")
    print(f"                 {Style.GRAY}Options: --dry-run, -n, --recursive, -r, --pattern, --quiet, -q{Style.RESET}")
    print()
    print(f"    {Style.CYAN}dedupe{Style.RESET}      Find and remove duplicate files")
    print(f"                 {Style.GRAY}Options: --delete, -d, --dry-run, -n, --quiet, -q{Style.RESET}")
    print()
    print(f"    {Style.CYAN}rename{Style.RESET}      Batch rename files with prefix/suffix/replace/number")
    print(f"                 {Style.GRAY}Options: --prefix, --suffix, --replace OLD,NEW, --number, --ext, --dry-run, --quiet, -q{Style.RESET}")
    print()
    print(f"    {Style.CYAN}gitstats{Style.RESET}    Show beautiful git repository statistics dashboard")
    print(f"                 {Style.GRAY}Example: python3 devutils.py gitstats /path/to/repo{Style.RESET}")
    print()
    print(f"    {Style.CYAN}help{Style.RESET}        Show this help message")
    print()
    print(f"  {Style.BOLD}Examples:{Style.RESET}")
    print(f"    python3 devutils.py organize ~/Downloads")
    print(f"    python3 devutils.py organize ~/Downloads --dry-run")
    print(f"    python3 devutils.py dedupe ~/Documents")
    print(f"    python3 devutils.py dedupe ~/Documents --delete")
    print(f"    python3 devutils.py rename --prefix 'project_' --number")
    print(f"    python3 devutils.py rename --replace 'draft,final'")
    print(f"    python3 devutils.py gitstats")
    print(f"    python3 devutils.py gitstats ~/my-project")
    print()
    print(f"  {Style.BOLD}Package:{Style.RESET}")
    print(f"    Includes: devutils.py, README.md")
    print(f"    Requirements: Python 3.6+")
    print(f"    License: MIT")
    return 0


# ─── Main ──────────────────────────────────────────────────────────────────────

COMMANDS = {
    'organize': cmd_organize,
    'dedupe': cmd_dedupe,
    'rename': cmd_rename,
    'gitstats': cmd_gitstats,
    'help': cmd_help,
}

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ('--help', '-h'):
        return cmd_help([])

    command = sys.argv[1]
    args = sys.argv[2:]

    # Filter out flags for the path argument
    path_args = [a for a in args if not a.startswith('-') and a not in ('--delete', '-d', '--dry-run', '-n', '--quiet', '-q', '--recursive', '-r', '--number') and not a.startswith('--prefix') and not a.startswith('--suffix') and not a.startswith('--replace') and not a.startswith('--pattern') and not a.startswith('--ext')]

    # Handle flags that take values
    skip_next = False
    clean_args = []
    for i, a in enumerate(args):
        if skip_next:
            skip_next = False
            continue
        if a in ('--prefix', '--suffix', '--replace', '--pattern', '--ext'):
            skip_next = True
            continue
        clean_args.append(a)

    if command in COMMANDS:
        try:
            return COMMANDS[command](path_args)
        except KeyboardInterrupt:
            print()
            print(Style.warn("Operation cancelled by user"))
            return 130
        except Exception as e:
            print(Style.err(f"Error: {e}"))
            return 1
    else:
        print(Style.err(f"Unknown command: {command}"))
        print(f"  Run '{sys.argv[0]} help' for available commands")
        return 1


if __name__ == '__main__':
    sys.exit(main())
