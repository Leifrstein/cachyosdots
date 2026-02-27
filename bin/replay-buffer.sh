#!/usr/bin/env bash
PIDFILE="$HOME/.cache/gsrb.pid"

# Prevent more than one instance
if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
    echo "Replay already running."
    exit 1
fi

OUTPUT="$HOME/Videos/VODs/Replays"

gpu-screen-recorder \
  -w DP-2 \
  -r 120 \
  -a default_input\|default_output \
  -c mp4 \
  -k hevc \
  -bm cbr \
  -q 40000 \
  -o "$OUTPUT" &

echo $! > "$PIDFILE"
