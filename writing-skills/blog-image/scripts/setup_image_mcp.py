#!/usr/bin/env python3
"""
Setup script for nanobanana-mcp in claude-blog.

Configures @ycse/nanobanana-mcp in Claude Code's global settings.json
(default) or the project's .mcp.json (with --project flag).

Usage:
    python3 setup_image_mcp.py                    # Interactive (writes global)
    python3 setup_image_mcp.py --key YOUR_KEY     # Non-interactive
    python3 setup_image_mcp.py --check            # Verify existing setup
    python3 setup_image_mcp.py --remove           # Remove MCP config
    python3 setup_image_mcp.py --project          # Write to project .mcp.json (env-expansion only)
    python3 setup_image_mcp.py --help             # Show usage
"""

import json
import sys
import os
from pathlib import Path

MCP_NAME = "nanobanana-mcp"
MCP_PACKAGE = "@ycse/nanobanana-mcp"
DEFAULT_MODEL = "gemini-3.1-flash-image-preview"
PINNED_PACKAGE = "@ycse/nanobanana-mcp@1.1.1"  # latest stable as of 2026-04-27
ENV_PLACEHOLDER = "${GOOGLE_AI_API_KEY}"
PLUGIN_NAME = "claude-blog"
GLOBAL_SETTINGS_PATH = Path.home() / ".claude" / "settings.json"


def find_project_mcp_json() -> Path:
    """Find the project-level .mcp.json by locating .claude-plugin/plugin.json with name=='claude-blog'."""
    def matches(plugin_path: Path) -> bool:
        try:
            import json as _json
            with open(plugin_path) as f:
                return _json.load(f).get("name") == PLUGIN_NAME
        except (OSError, _json.JSONDecodeError):
            return False
    for start in (Path(__file__).resolve().parent, Path.cwd()):
        current = start
        for _ in range(5):
            candidate = current / ".claude-plugin" / "plugin.json"
            if candidate.exists() and matches(candidate):
                return current / ".mcp.json"
            parent = current.parent
            if parent == current:
                break
            current = parent
    return None


def get_config_path(use_global: bool) -> Path:
    """Get the appropriate config file path."""
    if use_global:
        return GLOBAL_SETTINGS_PATH
    project_path = find_project_mcp_json()
    if project_path:
        return project_path
    print("Warning: Could not find project root (.claude-plugin/plugin.json).")
    print("Falling back to global settings.")
    return GLOBAL_SETTINGS_PATH


def load_config(path: Path) -> dict:
    """Load config file."""
    if not path.exists():
        return {}
    with open(path, "r") as f:
        return json.load(f)


def save_config(path: Path, config: dict) -> None:
    """Save config file. Sets restrictive permissions if the file may contain secrets."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump(config, f, indent=2)
        f.write("\n")
    os.chmod(path, 0o600)  # belt-and-braces if file pre-existed
    print(f"Config saved to {path}")


def _mask_api_key(key: str) -> str:
    """Mask an API key for safe display (VULN-S01).

    Shows the first 4 and last 4 chars with stars between. For short keys
    (<10 chars), returns a length-only placeholder so we never reveal more
    than half the key. Terminal scrollback, tmux logs, and screen recordings
    all preserve stdout; this helper keeps the literal key out of the echo.
    """
    if not key:
        return "(not set)"
    if len(key) < 10:
        return f"<{len(key)} chars>"
    return f"{key[:4]}****{key[-4:]}"


def _is_git_tracked(path: Path) -> bool:
    """Return True if path is tracked by git in its containing repo."""
    import subprocess
    try:
        result = subprocess.run(
            ["git", "ls-files", "--error-unmatch", path.name],
            cwd=path.parent,
            capture_output=True,
            text=True,
        )
        return result.returncode == 0
    except (OSError, FileNotFoundError):
        return False


def check_setup(use_global: bool) -> bool:
    """Check if MCP is already configured."""
    # Check project-level first, then global
    paths_to_check = []
    if not use_global:
        project_path = find_project_mcp_json()
        if project_path:
            paths_to_check.append(("Project .mcp.json", project_path))
    paths_to_check.append(("Global settings.json", GLOBAL_SETTINGS_PATH))

    for label, path in paths_to_check:
        config = load_config(path)
        servers = config.get("mcpServers", {})
        if MCP_NAME in servers:
            env = servers[MCP_NAME].get("env", {})
            key = env.get("GOOGLE_AI_API_KEY", "")
            # Closes audit VULN-032: don't leak last-4 of API key. Length-only.
            masked = f"<{len(key)} chars, set>" if key else "(not set)"
            print(f"MCP server '{MCP_NAME}' found in {label}.")
            print(f"  Path:    {path}")
            print(f"  Package: {MCP_PACKAGE}")
            print(f"  API Key: {masked}")
            print(f"  Model:   {env.get('NANOBANANA_MODEL', DEFAULT_MODEL)}")
            return True

    print(f"MCP server '{MCP_NAME}' is NOT configured.")
    return False


def remove_mcp(use_global: bool) -> None:
    """Remove MCP configuration."""
    path = get_config_path(use_global)
    config = load_config(path)
    servers = config.get("mcpServers", {})
    if MCP_NAME in servers:
        del servers[MCP_NAME]
        config["mcpServers"] = servers
        save_config(path, config)
        print(f"Removed '{MCP_NAME}' from {path}.")
    else:
        print(f"'{MCP_NAME}' not found in {path}.")


def setup_mcp(api_key: str, use_global: bool) -> None:
    """Configure MCP server. Project mode uses env-expansion only (never literal key)."""
    if not api_key or not api_key.strip():
        print("Error: API key cannot be empty.")
        sys.exit(1)
    api_key = api_key.strip()
    path = get_config_path(use_global)

    # Safety: project mode must never write a literal key into a tracked file.
    if not use_global and _is_git_tracked(path):
        gitignore = path.parent / ".gitignore"
        ignored = ".mcp.json" in gitignore.read_text() if gitignore.exists() else False
        if not ignored:
            print(f"REFUSING: {path} is tracked by git and .gitignore does not exclude .mcp.json.")
            print("Either:")
            print(f"  1. Add '.mcp.json' to {gitignore} and run: git rm --cached .mcp.json")
            print(f"  2. Use --global to write to ~/.claude/settings.json instead (recommended).")
            sys.exit(2)

    config = load_config(path)
    config.setdefault("mcpServers", {})

    # Project mode: env-expansion only. Global mode: literal value (file is user-private + chmod 600).
    key_value = ENV_PLACEHOLDER if not use_global else api_key

    config["mcpServers"][MCP_NAME] = {
        "command": "npx",
        "args": ["-y", PINNED_PACKAGE],
        "env": {
            "GOOGLE_AI_API_KEY": key_value,
            "NANOBANANA_MODEL": DEFAULT_MODEL,
        },
    }
    save_config(path, config)

    print(f"\nMCP server '{MCP_NAME}' configured successfully!")
    print(f"  Package: {PINNED_PACKAGE}")
    print(f"  Model:   {DEFAULT_MODEL}")
    print(f"  Config:  {path}")
    if not use_global:
        print()
        print("Project mode uses env-expansion (never writes literal key).")
        print("Add this line to your shell rc (~/.bashrc or ~/.zshrc),")
        print("substituting the API key you just entered for <YOUR_KEY>:")
        # VULN-S01 (v1.9.1): do NOT echo the literal key. Terminal scrollback,
        # tmux logs, and recording sessions all preserve stdout. Mask the
        # value; the user already entered it, so a placeholder + first/last
        # 4-char hint is enough to confirm the intended export.
        masked = _mask_api_key(api_key)
        print(f"  export GOOGLE_AI_API_KEY=<YOUR_KEY>   # hint: {masked}")
        print("Then restart your shell + Claude Code.")
    else:
        print()
        print(f"File mode set to 0600 (user-private).")
        print("Restart Claude Code for changes to take effect.")
    print(f"Generated images saved to: ~/Documents/nanobanana_generated/")


def main() -> None:
    args = sys.argv[1:]
    # Safer default: --global (writes user-private ~/.claude/settings.json).
    # --project opts in to project-local config (with safety guards).
    use_global = "--project" not in args

    if "--help" in args or "-h" in args:
        print("Usage: python3 setup_image_mcp.py [OPTIONS]")
        print()
        print("Options:")
        print("  --key KEY        Provide API key non-interactively")
        print("  --check          Verify existing setup")
        print("  --remove         Remove MCP configuration")
        print("  --project        Write to project .mcp.json (default: ~/.claude/settings.json)")
        print("  --help, -h       Show this help message")
        print()
        print("Get a free API key at: https://aistudio.google.com/apikey")
        sys.exit(0)

    if "--check" in args:
        check_setup(use_global)
        return

    if "--remove" in args:
        remove_mcp(use_global)
        return

    # Get API key
    api_key = None
    for i, arg in enumerate(args):
        if arg == "--key" and i + 1 < len(args):
            api_key = args[i + 1]
            break

    if not api_key:
        api_key = os.environ.get("GOOGLE_AI_API_KEY")

    if not api_key:
        print("claude-blog - Image Generation MCP Setup")
        print("=" * 45)
        print(f"\nGet your free API key at: https://aistudio.google.com/apikey")
        print()
        try:
            api_key = input("Enter your Google AI API key: ")
        except (EOFError, KeyboardInterrupt):
            print("\nError: No input received. Provide a key with --key or set GOOGLE_AI_API_KEY env var.")
            sys.exit(1)

    setup_mcp(api_key, use_global)


if __name__ == "__main__":
    main()
