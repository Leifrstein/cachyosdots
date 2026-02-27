#!/usr/bin/env bash

PIDFILE="$HOME/.cache/gsrb.pid"

if [ -f "$PIDFILE" ]; then
    PID="$(cat "$PIDFILE")"

    if kill -0 "$PID" 2>/dev/null; then
        kill -SIGUSR1 "$PID"
        sleep 1
        kill -SIGINT "$PID"
        rm -f "$PIDFILE"
        echo "Replay buffer stopped."
    else
        echo "Process not running."
        rm -f "$PIDFILE"
    fi
else
    echo "No replay PID file found."
fi
