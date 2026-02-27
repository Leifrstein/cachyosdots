#!/bin/bash
backup_dir="$HOME/Packages"
filename="$backup_dir/AUR-packages-$(date +%F).lst"
pacman -Qqem > "$filename"
# keep only the last 8 files
ls -1tr $backup_dir/AUR-packages-*.lst | head -n -8 | xargs -r rm --
