source /usr/share/cachyos-fish-config/cachyos-config.fish

# overwrite greeting
# potentially disabling fastfetch
#function fish_greeting
#    # smth smth
#end
set -gx SUDO_EDITOR (which helix)

alias rd="rmdir"
alias md="mkdir -p"
alias rm="rm --interactive"
alias du="dust"
alias df="duf"
alias fd="fd -Lu"
alias bgrep="batgrep"
alias cat="bat --paging=never"
alias less="bat --paging=always"
alias man="batman"
alias diff="batdiff"
alias tldr="PAGER='bat --plain' command tldr"
alias hx="helix"
alias z="zoxide"
alias tree="erd -HI -yinverted -."

fish_config theme choose "Catppuccin Mocha" --color-theme=dark
