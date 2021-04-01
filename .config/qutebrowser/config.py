# Load settings added with ui
# See <https://github.com/qutebrowser/qutebrowser/blob/master/doc/help/configuring.asciidoc#loading-autoconfigyml>
config.load_autoconfig()

# Search engines
c.url.searchengines = {
        "DEFAULT": "https://duckduckgo.com/?q={}",
        "aw": "https://wiki.archlinux.org/?search={}",
        "gw": "https://wiki.gentoo.org/?search-{}",
        "yt": "https://youtube.com/results?search_query={}",
        "w": "https://en.wikipedia.org/?search={}",
        "g": "https://www.google.fi/search?q={}",
        "dgi": "https://duckduckgo.com/?q=!ddgi {}",
        "tw": "twitter.com/{}",
        "dick": "http://en.wiktionary.org/?search={}",
        "r": "https://reddit.com/r/{}",
}

## Aliases
c.aliases = {
    "w": "session-save",
    "wq": "quit --save",
    "mpv": "spawn -d mpv --force-window=immediate {url}",
    'gh': "open -t https://github.com/hoaxdream",
    'wh': "open -t https://alpha.wallhaven.cc/search?q=&categories=111&purity=100&topRange=1y&sorting=toplist&order=desc&colors=336600&page=1",
    'wt': "open -t https://www.webtoons.com/en/",
    'fb': "open -t https://facebook.com/",
    'ux': "open -t https://www.reddit.com/r/unixporn/",
    'tr': "open -t https://1337x.to/",
    'cc': "open -t https://jonasjacek.github.io/colors/",
    'tag': "open -t http://www.tagged.com/home.html",
    'suck': "open -t http://suckless.org/",
}

#c.colors.webpage.darkmode.enabled = True  # This will break my startpage
#c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.bg = 'black'

c.url.start_pages = ['~/.config/startpage/index.html']
c.editor.command = ["st", "-e", "nvim '{}'"]
c.downloads.location.directory = '~/.config/dl'
c.downloads.location.prompt = False
c.scrolling.smooth = False
c.content.notifications = False
c.tabs.last_close = "close"
c.tabs.select_on_remove = "prev"
c.confirm_quit = ["downloads"]
c.completion.height = "20%"
c.completion.show = "always"
c.content.cookies.accept = 'no-3rdparty'
c.content.dns_prefetch = True
c.content.ssl_strict = False
c.downloads.remove_finished = 1000
c.hints.scatter = True
c.content.autoplay = False
c.content.pdfjs = True

# Define font and colors values
monospace = "16px 'Noto Sans Mono'"
bg = "#1d2021"
fg = "#ebdbb2"
base01 = "#1d2021" # black
base02 = "#cc241d" # red
base03 = "#98971a" # green
base04 = "#d79921" # yellow
base05 = "#458588" # blue
base06 = "#b16286" # magenta
base07 = "#689d6a" # cyan
base08 = "#a89984" # white
base09 = "#928374" # black
base10 = "#fb4934" # red
base11 = "#b8bb26" # green
base12 = "#fabd2f" # yellow
base13 = "#83a598" # blue
base14 = "#d3869b" # magenta
base15 = "#8ec07c" # cyan
base16 = "#ebdbb2" # white

c.fonts.completion.category = f"bold {monospace}" # font used in the completion categories
c.fonts.completion.entry = monospace              # font used in the completion widget
c.fonts.debug_console = monospace                 # font used for the debugging console
c.fonts.downloads = monospace                     # font used for the downloadbar
c.fonts.keyhint = monospace                       # font used in the keyhint widget
c.fonts.messages.error = monospace                # font used for error messages
c.fonts.messages.info = monospace                 # font used for info messages
c.fonts.messages.warning = monospace              # font used for warning messages
c.fonts.prompts = monospace                       # font used for prompts
c.fonts.statusbar = monospace                     # font used in the statusbar
c.fonts.hints = monospace                         # font used for the hints

# Context menu
c.colors.contextmenu.menu.bg = bg
c.colors.contextmenu.menu.fg = fg
c.colors.contextmenu.selected.bg = base05
c.colors.contextmenu.selected.fg = bg

# Completion
c.colors.completion.category.bg = base01          # background color of the completion widget category headers.


## bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = base01

## top border color of the completion widget category headers.
c.colors.completion.category.border.top = base01

## foreground color of completion widget category headers.
c.colors.completion.category.fg = fg

## background color of the completion widget for even rows.
c.colors.completion.even.bg = bg

## background color of the completion widget for odd rows.
c.colors.completion.odd.bg = bg

## text color of the completion widget.
c.colors.completion.fg = fg

## background color of the selected completion item.
c.colors.completion.item.selected.bg = base05

## bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = base09

## top border color of the completion widget category headers.
c.colors.completion.item.selected.border.top = base09

## foreground color of the selected completion item.
c.colors.completion.item.selected.fg = base01

## foreground color of the matched text in the completion.
c.colors.completion.match.fg = base11

## color of the scrollbar in completion view.
c.colors.completion.scrollbar.bg = base01

## color of the scrollbar handle in completion view.
c.colors.completion.scrollbar.fg = base09

## Downloads
## background color for the download bar.
c.colors.downloads.bar.bg = bg

## background color for active download bar.
c.colors.downloads.start.bg = bg

## foreground color for active download bar.
c.colors.downloads.start.fg = base04

## background color for downloads with errors.
c.colors.downloads.error.bg = base02

## foreground color for downloads with errors.
c.colors.downloads.error.fg = base01

## color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = bg

## color gradient stop for download foregrounds.
c.colors.downloads.stop.fg = base11

## color gradient interpolation system for download backgrounds.
c.colors.downloads.system.bg = 'none'

## Hints
## background color for hints. use rgba value for transparency.
c.colors.hints.bg = bg

## font color for hints.
c.colors.hints.fg = fg

## hints
c.hints.border = '1px solid ' + base01

## font color for the matched part of hints.
c.colors.hints.match.fg = base11

## background color of the keyhint widget.
c.colors.keyhint.bg = bg

## text color for the keyhint widget.
c.colors.keyhint.fg = fg

## highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = fg

## Info and error messages
## background color of an error message.
c.colors.messages.error.bg = base02

## border color of an error message.
c.colors.messages.error.border = base10

## foreground color of an error message.
c.colors.messages.error.fg = base16

## background color of an info message.
c.colors.messages.info.bg = base01

## border color of an info message.
c.colors.messages.info.border = base01

## foreground color an info message.
c.colors.messages.info.fg = base16

## background color of a warning message.
c.colors.messages.warning.bg = base06

## border color of a warning message.
c.colors.messages.warning.border = base12

## foreground color a warning message.
c.colors.messages.warning.fg = base16

## Prompt
## background color for prompts.
c.colors.prompts.bg = base09

## border used around UI elements in prompts.
c.colors.prompts.border = '1px solid ' + base01

## foreground color for prompts.
c.colors.prompts.fg = fg

## background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = bg

## Caret
## background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = bg

## foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = fg

## background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = bg

## foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = fg

## Statusbar
## background color of the statusbar in command mode.
c.colors.statusbar.command.bg = base01

## foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = fg

## background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = bg

## foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = fg

## background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = base11

## foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = bg

## background color of the statusbar.
c.colors.statusbar.normal.bg = bg

## foreground color of the statusbar.
c.colors.statusbar.normal.fg = fg

## background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = base05

## foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = base16

## background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = bg

## foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = fg

## background color of the progress bar.
c.colors.statusbar.progress.bg = base16

## foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = base06

## default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = base16

## foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = base09

## foreground color of the URL in the statusbar on successful load
c.colors.statusbar.url.success.http.fg = base11

## foreground color of the URL in the statusbar on successful load
c.colors.statusbar.url.success.https.fg = base11

## foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = base04

## status bar padding.
c.statusbar.padding = {
    "top": 5,
    "right": 5,
    "bottom": 5,
    "left": 5,
}

## Tabs
## background color of the tab bar.
## type: qtcolor
c.colors.tabs.bar.bg = bg

## background color of unselected even tabs.
## type: qtcolor
c.colors.tabs.even.bg = bg

## Foreground color of unselected even tabs.
## type: qtcolor
c.colors.tabs.even.fg = base16

## color for the tab indicator on errors.
## type: qtcolor
c.colors.tabs.indicator.error = base02

## color gradient start for the tab indicator.
## type: qtcolor
c.colors.tabs.indicator.start = base05

## color gradient end for the tab indicator.
## type: qtcolor
c.colors.tabs.indicator.stop = base11

## color gradient interpolation system for the tab indicator.
## type: colorsystem
c.colors.tabs.indicator.system = 'none'

## background color of unselected odd tabs.
## type: qtcolor
c.colors.tabs.odd.bg = bg

## foreground color of unselected odd tabs.
## type: qtcolor
c.colors.tabs.odd.fg = base16

## background color of selected even tabs.
## type: qtcolor
c.colors.tabs.selected.even.bg = bg

## foreground color of selected even tabs.
## type: qtcolor
c.colors.tabs.selected.even.fg = base11

## background color of selected odd tabs.
## type: qtcolor
c.colors.tabs.selected.odd.bg = bg

## foreground color of selected odd tabs.
## type: qtcolor
c.colors.tabs.selected.odd.fg = base11

## tab padding.
c.tabs.padding = {
    "top": 5,
    "right": 5,
    "bottom": 5,
    "left": 5,
}

c.tabs.indicator.width = 1
c.tabs.favicons.scale = 1

## Mappings
ESC_BIND = 'clear-keychain ;; search ;; fullscreen --leave'
c.bindings.commands['normal'] = {
'<ctrl-x>': ESC_BIND,
}

config.bind('<ctrl-x>', 'leave-mode')
config.bind("K", "tab-next")
config.bind("J", "tab-prev")
config.bind("O", "set-cmd-text :open {url:pretty}")
config.bind("T", "set-cmd-text :open -t {url:pretty}")
config.bind("t", "set-cmd-text -s :open -t")
config.bind("z+", "zoom-in")
config.bind("z-", "zoom-out")
config.bind("zz", "zoom")
config.bind("h", "scroll-px -300 0")
config.bind("j", "scroll-px 0 300")
config.bind("k", "scroll-px 0 -300")
config.bind("l", "scroll-px 300 0")

config.bind('<Escape>', 'leave-mode ;; jseval -q document.activeElement.blur()', mode='insert')
config.bind('<Ctrl-x>', 'leave-mode ;; jseval -q document.activeElement.blur()', mode='insert')

c.bindings.commands['hint'] = {
        # escape hatch
        '<ctrl-x>': 'leave-mode',
}

c.bindings.commands['caret'] = {
        # escape hatch
        '<ctrl-x>': 'leave-mode',
}

c.bindings.commands['prompt'] = {
        # escape hatch
        '<ctrl-x>': 'leave-mode',
}

c.bindings.commands['command'] = {
        # escape hatch
        '<ctrl-x>': 'leave-mode',
}

c.bindings.commands['insert'] = {
        # escape hatch
        '<ctrl-x>': 'leave-mode',
}
