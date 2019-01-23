c.qt.force_software_rendering = "chromium"
c.downloads.location.directory = "~/downloads"
c.editor.command = [ "urxvt", "-e", "nvim", "{}" ]
c.editor.encoding = "utf-8"

c.url.searchengines = {
        "DEFAULT" : "https://duckduckgo.com/?q={}",
        "aur" : "https://aur.archlinux.org/packages/?O=0&K={}",
        "aw" : "https://wiki.archlinux.org/?search={}",
        "cpp" : "http://en.cppreference.com/mwiki/index.php?search={}"
}

c.url.start_pages = [ "https://duckduckgo.com" ]

c.fonts.completion.entry = "12px Hack"
c.fonts.completion.category = "12px Hack"
c.fonts.debug_console = "12px Hack"
c.fonts.downloads = "12px Hack"
c.fonts.hints = "12px Hack"
c.fonts.keyhint = "12px Hack"
c.fonts.messages.info = "12px Hack"
c.fonts.messages.error = "12px Hack"
c.fonts.monospace = "Hack"
c.fonts.prompts = "12px Hack"
c.fonts.statusbar = "12px Hack"
c.fonts.tabs = "12px Hack"

c.tabs.padding = {"bottom" : 5, "top" : 5, "left" : 5, "right" : 5 }
c.tabs.last_close = "startpage"

# various shortcuts
config.bind("ec", "config-edit")
config.bind("em", 'spawn mpv {url}')
config.bind("eM", 'hint links spawn mpv {hint-url}')

# qute-pass spawn
config.bind("<Ctrl-l>", "spawn --userscript qute-pass -d dmenu")

# quick subreddit open
config.bind("<Ctrl-r>", "set-cmd-text :open old.reddit.com/r/")
config.bind("<Ctrl-Shift-r>", "set-cmd-text :open -t old.reddit.com/r/")

# quick buku add bookmark
config.bind("gm", "set-cmd-text :spawn buku -a {url}")

# quick marks a'la pentadactyl
qsites = {
        'a': 'allegro.pl',
        'b': 'airdates.tv',
        'c': 'ceneo.pl',
        'd': 'cinkciarz.pl',
        'e': 'coursera.org',
        'f': 'facebook.com',
        'g': 'gmail.com',
        'h': 'filmweb.pl',
        'i': 'imdb.com',
        'j': 'linuxjournal.com',
        'k': 'lkml.org',
        'l': 'linkedin.com',
        'm': 'mailfence.com',
        'n': 'nofluffjobs.com',
        'o': 'maps.openrouteservice.org',
        'p': 'lwn.net',
        'q': 'gcc.godbolt.org',
        'r': 'release24.pl',
        's': 'scnsrc.me',
        't': 'translate.google.com',
        'u': 'trojmiasto.pl',
        'v': 'vimcasts.org',
        'w': 'wiki.archlinux.org',
        'x': 'aliexpress.com',
        'y': 'youtube.com',
        'z': 'mega.nz' }
for k,v in qsites.items():
        config.bind("gc" + k, 'open ' + v)
        config.bind("gn" + k, 'open -t ' + v)

# colors

c.colors.completion.fg = "gray"

# c.colors.completion.bg = "black"

# c.colors.completion.alternate.bg = "#282828"

c.colors.completion.category.fg = "gray"

c.colors.completion.category.border.top = "#282828"

c.colors.completion.category.border.bottom = c.colors.completion.category.border.top

c.colors.completion.item.selected.fg = "#1d2021"

c.colors.completion.item.selected.bg = "#a89984"

c.colors.completion.item.selected.border.top = "#282828"

c.colors.completion.item.selected.border.bottom = c.colors.completion.item.selected.border.top

c.colors.completion.match.fg = "#689d6a"

c.colors.completion.scrollbar.fg = c.colors.completion.fg

# c.colors.completion.scrollbar.bg = c.colors.completion.bg

c.colors.statusbar.normal.fg = "#a89984"

c.colors.statusbar.normal.bg = "#252525"

c.colors.statusbar.private.fg = c.colors.statusbar.normal.fg

c.colors.statusbar.private.bg = "#666666"

c.colors.statusbar.insert.fg = c.colors.statusbar.normal.fg

c.colors.statusbar.insert.bg = "#252525"

c.colors.statusbar.command.fg = c.colors.statusbar.normal.fg

c.colors.statusbar.command.bg = c.colors.statusbar.normal.bg

c.colors.statusbar.command.private.fg = c.colors.statusbar.private.fg

c.colors.statusbar.command.private.bg = c.colors.statusbar.private.bg

c.colors.statusbar.caret.fg = c.colors.statusbar.normal.fg

c.colors.statusbar.caret.bg = "#a89984"

c.colors.statusbar.caret.selection.fg = c.colors.statusbar.normal.fg

c.colors.statusbar.caret.selection.bg = "#458588"

c.colors.statusbar.progress.bg = "#83a598"

c.colors.statusbar.url.fg = c.colors.statusbar.normal.fg

c.colors.statusbar.url.success.http.fg = "#a89984"

c.colors.statusbar.url.success.https.fg = "#689d6a"

c.colors.statusbar.url.error.fg = "#fb4934"

c.colors.statusbar.url.warn.fg = "#b16286"

c.colors.statusbar.url.hover.fg = "#458588"

c.colors.tabs.odd.fg = "#a89984"

c.colors.tabs.odd.bg = "#1d2021"

c.colors.tabs.even.fg = "#a89984"

c.colors.tabs.even.bg = "#1d2021"

c.colors.tabs.selected.odd.fg = "#8ec07c"

c.colors.tabs.selected.odd.bg = "#282828"

c.colors.tabs.selected.even.fg = c.colors.tabs.selected.odd.fg

c.colors.tabs.selected.even.bg = c.colors.tabs.selected.odd.bg

c.colors.tabs.bar.bg = "#1d2021"

c.colors.tabs.indicator.start = "#ebdbb2"

c.colors.tabs.indicator.stop = "#b16286"

c.colors.tabs.indicator.error = "#d65d0e"

c.colors.tabs.indicator.system = "rgb"

c.colors.hints.fg = "#fbf1c7"

c.colors.hints.bg = "#665c54"

c.colors.hints.match.fg = "#fe8019"

c.colors.downloads.bar.bg = "#3c3836"

c.colors.downloads.start.fg = "#ebdbb2"

c.colors.downloads.start.bg = "#d65d0e"

c.colors.downloads.stop.fg = c.colors.downloads.start.fg

c.colors.downloads.stop.bg = "#689d6a"

c.colors.downloads.system.fg = "rgb"

c.colors.downloads.system.bg = "rgb"

c.colors.downloads.error.fg = "#b1a191"

c.colors.downloads.error.bg = "#d79921"

c.colors.webpage.bg = "#fbf1c7"

c.colors.keyhint.fg = "#d33682"

c.colors.keyhint.suffix.fg = "#2aa198"

c.colors.messages.error.fg = "#fdf6e3"

c.colors.messages.error.bg = "#dc322f"

c.colors.messages.error.border = "#fdf6e3"

c.colors.messages.warning.fg = "#859900"

c.colors.messages.warning.bg = "#fdf6e3"

c.colors.messages.warning.border = "#d47300"

c.colors.messages.info.fg = "#a89984"

c.colors.messages.info.bg = "#1d2021"

c.colors.messages.info.border = "#202020"

c.colors.prompts.fg = "#a89984"

c.colors.prompts.bg = "#282828"

c.colors.prompts.selected.bg = "#282828"
