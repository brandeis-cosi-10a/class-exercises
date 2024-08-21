#!/bin/bash
git fetch upstream
git merge upstream/main --strategy-option theirs -m "Merge new exercises"
