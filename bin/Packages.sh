#!/bin/bash
backup_dir="$HOME/Packages"
filename="$backup_dir/Packages-$(date +%F).lst"
pacman -Qqen > "$filename"
# keep only the last 8 files
ls -1tr $backup_dir/Packages-*.lst | head -n -8 | xargs -r rm --
