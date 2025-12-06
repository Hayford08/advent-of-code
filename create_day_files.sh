#!/usr/bin/env bash
set -e 

YEAR=$1
DAY=$2

if [ -z "$YEAR" ] || [ -z "$DAY" ]; then
  echo "Usage: $0 <year> <day>"
  echo "Example: $0 2024 5"
  exit 1
fi

DAY_PADDED=$(printf "%02d" "$DAY")
DAY_DIR="$YEAR/Day$DAY_PADDED"
PY_FILE="$DAY_DIR/day${DAY_PADDED}.py"
INPUT_FILE="$DAY_DIR/input.txt"

mkdir -p "$DAY_DIR"
touch "$PY_FILE"
touch "$INPUT_FILE"
cp template.py "$PY_FILE"
code "$DAY_DIR"