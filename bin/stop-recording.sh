#!/usr/bin/env bash

PIDFILE="$HOME/.cache/gsr.pid"

if [ -f "$PIDFILE" ]; then
    PID="$(cat "$PIDFILE")"

    if kill -0 "$PID" 2>/dev/null; then
        kill -SIGINT "$PID"
        rm -f "$PIDFILE"
        echo "Capture stopped."
    else
        echo "Process not running."
        rm -f "$PIDFILE"
    fi
else
    echo "No GSR PID file found."
fi
