#!/usr/bin/env bash
set -e

FILE=${1:-src/scene/recap.py}
SCENE=${2:-RecapCalc1}
QUALITY=${3:-l}

(
  find src -type f \( -name "*.py" -o -name "*.txt" -o -name "*.md" \)
  [ -f manim.cfg ] && echo manim.cfg
) | entr -c bash -lc "manim \"$FILE\" \"$SCENE\" -q$QUALITY -p"
