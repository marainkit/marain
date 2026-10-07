#!/usr/bin/env bash
# tools/skill/install.sh — install repo skills into ~/.claude/skills/<name>/SKILL.md
#
# Usage:
#   ./tools/skill/install.sh           # install all skills
#   ./tools/skill/install.sh marain    # install one skill by name
#
# Each skill lives at tools/skill/<name>/SKILL.md. The installed SKILL.md is a
# symlink, so edits in the repo apply immediately.

set -euo pipefail

SKILLS_DIR="$HOME/.claude/skills"
REPO_SKILL_DIR="$(cd "$(dirname "$0")" && pwd)"

mkdir -p "$SKILLS_DIR"

install_skill() {
    local name="$1"
    local src="$REPO_SKILL_DIR/$name/SKILL.md"
    local dst_dir="$SKILLS_DIR/$name"
    local dst="$dst_dir/SKILL.md"

    if [[ ! -f "$src" ]]; then
        echo "ERROR: $src not found" >&2
        return 1
    fi

    mkdir -p "$dst_dir"
    if [[ -L "$dst" ]]; then
        rm "$dst"
    elif [[ -f "$dst" ]]; then
        echo "SKIP: $dst exists and is not a symlink — remove it manually to replace" >&2
        return 0
    fi

    ln -s "$src" "$dst"
    echo "installed: $src → $dst"
}

if [[ $# -gt 0 ]]; then
    install_skill "$1"
else
    installed=0
    for skill_dir in "$REPO_SKILL_DIR"/*/; do
        name="$(basename "$skill_dir")"
        if [[ -f "$skill_dir/SKILL.md" ]]; then
            install_skill "$name"
            installed=$((installed + 1))
        fi
    done
    echo "$installed skill(s) installed."
fi
