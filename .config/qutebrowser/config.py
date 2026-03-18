import os
from urllib.request import urlopen

# load your autoconfig, use this, if the rest of your config is empty!
config.load_autoconfig()

if not os.path.exists(config.configdir / "theme.py"):
    theme = "https://raw.githubusercontent.com/catppuccin/qutebrowser/main/setup.py"
    with urlopen(theme) as themehtml:
        with open(config.configdir / "theme.py", "a") as file:
            file.writelines(themehtml.read().decode("utf-8"))

if os.path.exists(config.configdir / "theme.py"):
    import theme
    theme.setup(c, 'mocha', True)

c.auto_save.session = True

# Quickmarks and bookmarks
config.bind('e', 'cmd-set-text -s :quickmark-load')
config.bind('E', 'cmd-set-text -s :quickmark-load -t')
config.bind('b', 'quickmark-save')
config.bind('B', 'bookmark-add')

# Download videos
config.bind('m', 'hint links spawn --detach yt-download.sh {hint-url}')
config.bind('M', 'spawn --detach yt-download.sh {url}')

# Spawn mpv with hint links
config.bind('<Space>m', 'hint links spawn --detach mpv {hint-url}')
config.bind('<Space>M', 'spawn --detach mpv {url}')

config.set('colors.webpage.darkmode.enabled', False, '*://*.youtube.com/*')
config.set('colors.webpage.darkmode.enabled', False, '*://*.youtube-nocookie.com/*')
print("Webpage dark mode for YouTube: DISABLED (use YouTube's native dark theme)")

c.url.searchengines = {
    'DEFAULT': 'https://startpage.com/do/asearch?q={}',
    '!ddg':   'https://duckduckgo.com/?q={}',
    '!aw':    'https://wiki.archlinux.org/?search={}',
    '!apkg':  'https://archlinux.org/packages/?sort=&q={}',
    '!gh':    'https://github.com/search?o=desc&q={}&s=stars',
    '!yt':    'https://www.youtube.com/results?search_query={}',
    '!r':     'https://www.reddit.com/search?q={}',
    '!so':    'https://stackoverflow.com/search?q={}',
    '!w':     'https://en.wikipedia.org/wiki/Special:Search?search={}',
    '!aur':   'https://aur.archlinux.org/packages?K={}',
    '!g':     'https://www.google.com/search?q={}',
    '!trl':   'https://www.deepl.com/translator#en/ptbr/{}',
    '!trle':  'https://www.deepl.com/translator#pt/en/{}',
    '!dai':   'https://duck.ai/?q={}',
    '!gpt':   'https://chat.openai.com/?q={}',
    '!gem':   'https://gemini.google.com/app?q={}',
    '!nya':   'https://nyaa.si/?q={}'
}

# --- ZEN MODE SETTINGS (Initial State: Hidden) ---
config.set('tabs.show', 'switching')
config.set('statusbar.show', 'in-mode')
config.set('scrolling.bar', 'never')

# --- KEYBINDINGS ---
# Press 'zb' to toggle both the Tab bar and Status bar at once
config.bind('zb', 'config-cycle statusbar.show always in-mode ;; config-cycle tabs.show always switching')

# --- File handler ---
config.set('fileselect.handler', 'external')
config.set('fileselect.single_file.command', ['env', 'GTK_THEME=Adwaita:dark', 'zenity', '--file-selection'])
config.set('fileselect.multiple_files.command', ['env', 'GTK_THEME=Adwaita:dark', 'zenity', '--file-selection', '--multiple'])

# Toggle dark mode and reload the page automatically
config.bind('td', 'config-cycle colors.webpage.darkmode.enabled true false ;; reload')

# Custom function to toggle darkmode for the current domain
for mode in ['true', 'false']:
    config.bind(f't{mode[0]}', f'set -u {{url}} colors.webpage.darkmode.enabled {mode}')

# Toggle dark mode for ONLY the current website and reload
config.bind('tg', 'config-cycle -u {url} colors.webpage.darkmode.enabled true false ;; reload')

# swapforqute
sfq_script_path = "~/.config/qutebrowser/userscripts/sfq.py"
sfq_conf_path = "~/.config/qutebrowser/config.json"
sfq_cmd = "--userscript {} -c {}".format(sfq_script_path, sfq_conf_path)
c.aliases['sfq'] = "cmd-set-text -s :spawn {} --cmd 'open' -u ".format(sfq_cmd)
config.bind('<Space>f', "hint links spawn {} --cmd 'open' -u ".format(sfq_cmd) + " {hint-url}")
config.bind('<Space>F', "hint links spawn {} --cmd 'open -t' -u ".format(sfq_cmd) + " {hint-url}")
