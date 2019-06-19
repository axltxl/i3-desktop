#!/bin/bash
set +x

# Make sure that the working directory is the app root dir
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export HOME=$SCRIPT_DIR
Xephyr :5 -screen 1280x1024 & sleep 1 ; DISPLAY=:5 i3
