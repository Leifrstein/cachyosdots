#!/usr/bin/env bash
PIDFILE="$HOME/.cache/gsr.pid"

# Prevent more than one instance
if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
    echo "Already recording."
    exit 1
fi

OUTPUT="$HOME/Videos/VODs/vod-$(date +%Y-%m-%d_%H-%M-%S).mp4"

gpu-screen-recorder \
  -w DP-2 \
  -a default_output\|default_input \
  -c mp4 \
  -k hevc \
  -o "$OUTPUT" &

echo $! > "$PIDFILE"
