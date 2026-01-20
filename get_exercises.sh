#!/bin/bash
git fetch origin
git merge origin/main --strategy-option theirs -m "Merge new exercises"
