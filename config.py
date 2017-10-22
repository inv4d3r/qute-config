c.downloads.location.directory = "~/downloads"
c.editor.command = [ "termite", "-e", "vim -f {}"]
c.editor.encoding = "utf-8"

c.url.searchengines = {
        "DEFAULT" : "https://duckduckgo.com/?q={}",
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

# quick url shortcuts

# for quick subreddit open
config.bind("<Ctrl-r>", "set-cmd-text :open reddit.com/r/")
config.bind("<Ctrl-Shift-r>", "set-cmd-text :open -t reddit.com/r/")

config.bind("gia", "open allegro.pl")
config.bind("gna", "open -t allegro.pl")
config.bind("gib", "open benchmark.pl")
config.bind("gnb", "open -t benchmark.pl")
config.bind("gic", "open ceneo.pl")
config.bind("gnc", "open -t ceneo.pl")
config.bind("gid", "open cinkciarz.pl")
config.bind("gnd", "open -t cinkciarz.pl")
config.bind("gie", "open encrypted.google.com")
config.bind("gne", "open -t encrypted.google.com")
config.bind("gif", "open facebook.com")
config.bind("gnf", "open -t facebook.com")
config.bind("gig", "open gmail.com")
config.bind("gng", "open -t gmail.com")
config.bind("gih", "open github.com")
config.bind("gnh", "open -t github.com")
config.bind("gii", "open imdb.com")
config.bind("gni", "open -t imdb.com")
config.bind("gij", "open yahoo.com")
config.bind("gnj", "open -t yahoo.com")
config.bind("gik", "open lkml.org")
config.bind("gnk", "open -t lkml.org")
config.bind("gil", "open linkedin.com")
config.bind("gnl", "open -t linkedin.com")
config.bind("gim", "open angrymetalguy.com")
config.bind("gnm", "open -t angrymetalguy.com")
config.bind("gin", "open privateinternetaccess.com")
config.bind("gnn", "open -t privateinternetaccess.com")
config.bind("gio", "open olkb.com")
config.bind("gno", "open -t olkb.com")
config.bind("gip", "open pimpmykeyboard.com")
config.bind("gnp", "open -t pimpmykeyboard.com")
config.bind("giq", "open qutebrowser.org")
config.bind("gnq", "open -t qutebrowser.org")
config.bind("gir", "open release24.pl")
config.bind("gnr", "open -t release24.pl")
config.bind("gis", "open coursera.org")
config.bind("gns", "open -t coursera.org")
config.bind("git", "open thepiratebay.org")
config.bind("gnt", "open -t thepiratebay.org")
config.bind("giu", "open openrouteservice.org")
config.bind("gnu", "open -t openrouteservice.org")
config.bind("giv", "open vimcasts.org")
config.bind("gnv", "open -t vimcasts.org")
config.bind("giw", "open vim.wikia.com")
config.bind("gnw", "open -t vim.wikia.com")
config.bind("gix", "open aliexpress.com")
config.bind("gnx", "open -t aliexpress.com")
config.bind("giy", "open youtube.com")
config.bind("gny", "open -t youtube.com")
config.bind("giz", "open gcc.godbolt.org")
config.bind("gnz", "open -t gcc.godbolt.org")

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
