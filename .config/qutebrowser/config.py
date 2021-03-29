# Load settings added with ui
# See <https://github.com/qutebrowser/qutebrowser/blob/master/doc/help/configuring.asciidoc#loading-autoconfigyml>
config.load_autoconfig()

# Start page
c.url.start_pages = ['~/.config/qutebrowser/start.html']

# Set default editor.
c.editor.command = ["st", "-e", "nvim '{}'"]

# Download path
c.downloads.location.directory = '~/.config/dl'

# Dark mode
c.colors.webpage.darkmode.enabled = True

c.colors.webpage.preferred_color_scheme = 'dark'

# Disables smooth scrolling
c.scrolling.smooth = False

# definitions of search engines which can be used via the address bar.
#"DEFAULT": "https://www.google.fi/search?q={}",
#"DEFAULT": "https://duckduckgo.com/?q={}",
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

## uncomment to set start page to blank
#c.url.start_pages = "about:blank"

## behavior when the last tab is closed.
##   * ignore: don't do anything.
##   * blank: load a blank page.
##   * startpage: load the start page.  - default-page: load the default page.  - close: close the window.
c.tabs.last_close = "close"

## which tab to select when the focused tab is removed.
##   * prev: select the tab which came before the closed one (left in horizontal, above in vertical).
##   * next: select the tab which came after the closed one (right in horizontal, below in vertical).
##   * last-used: select the previously selected tab.
c.tabs.select_on_remove = "prev"

## whether quitting the application requires a confirmation.
##   * always: always show a confirmation.
##   * multiple-tabs: show a confirmation if multiple tabs are opened.
##   * downloads: show a confirmation if downloads are running
##   * never: never show a confirmation.
c.confirm_quit = ["downloads"]

## the height of the completion, in px or as percentage of the window.
c.completion.height = "20%"

## when to show the autocompletion window.
##   * always: whenever a completion is available.
##   * auto: whenever a completion is requested.
##   * never: never.
c.completion.show = "always"

## control which cookies to accept.
##   * all: accept all cookies.
##   * no-3rdparty: accept cookies from the same origin only.
##   * no-unknown-3rdparty: accept cookies from the same origin only, unless a cookie is already set for the domain.
##   * never: don't accept cookies at all.
c.content.cookies.accept = 'no-3rdparty'

## try to pre-fetch DNS entries to speed up browsing.
c.content.dns_prefetch = True

## validate SSL handshakes.
##   * true
##   * false
##   * ask
c.content.ssl_strict = False

## number of milliseconds to wait before removing finished downloads.
## if set to -1, downloads are never removed.
c.downloads.remove_finished = 1000

## scatter hint key chains (like vimium).
## ignore for number hints.
c.hints.scatter = True

# Fonts
# Font variable
monospace = "14px 'Noto Sans Mono'"

## font used in the completion categories.
c.fonts.completion.category = f"bold {monospace}"

## font used in the completion widget.
c.fonts.completion.entry = monospace

## font used for the debugging console.
c.fonts.debug_console = monospace

## font used for the downloadbar.
c.fonts.downloads = monospace

## font used in the keyhint widget.
c.fonts.keyhint = monospace

## font used for error messages.
c.fonts.messages.error = monospace

## font used for info messages.
c.fonts.messages.info = monospace

## font used for warning messages.
c.fonts.messages.warning = monospace

## font used for prompts.
c.fonts.prompts = monospace

## font used in the statusbar.
c.fonts.statusbar = monospace

## font used for the hints.
c.fonts.hints = monospace

# Colors
# Context menu
c.colors.contextmenu.menu.bg = '#191c25'
c.colors.contextmenu.menu.fg = '#96b5b4'
c.colors.contextmenu.selected.bg = '#4c597d'
c.colors.contextmenu.selected.fg = '#96b5b4'

# Completion
## background color of the completion widget category headers.
c.colors.completion.category.bg = '#101010'

## bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = '#101010'

## top border color of the completion widget category headers.
c.colors.completion.category.border.top = '#191c25'

## foreground color of completion widget category headers.
c.colors.completion.category.fg = '#96b5b4'

## background color of the completion widget for even rows.
c.colors.completion.even.bg = '#191c25'

## background color of the completion widget for odd rows.
c.colors.completion.odd.bg = '#191c25'

## text color of the completion widget.
c.colors.completion.fg = '#96b5b4'

## background color of the selected completion item.
c.colors.completion.item.selected.bg = '#4c597d'

## bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = '#4c597d'

## top border color of the completion widget category headers.
c.colors.completion.item.selected.border.top = '#4c597d'

## foreground color of the selected completion item.
c.colors.completion.item.selected.fg = '#96b5b4'

## foreground color of the matched text in the completion.
c.colors.completion.match.fg = "#a3be8c"

## color of the scrollbar in completion view.
c.colors.completion.scrollbar.bg = '#101010'

## color of the scrollbar handle in completion view.
c.colors.completion.scrollbar.fg = '#4c597d'

## Downloads
## background color for the download bar.
c.colors.downloads.bar.bg = '#191c25'

## background color for active download bar.
c.colors.downloads.start.bg = '#191c25'

## foreground color for active download bar.
c.colors.downloads.start.fg = '#ffcb6b'

## background color for downloads with errors.
c.colors.downloads.error.bg = '#f07178'

## foreground color for downloads with errors.
c.colors.downloads.error.fg = '#101010'

## color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = '#191c25'

## color gradient stop for download foregrounds.
c.colors.downloads.stop.fg = '#a3be8c'

## color gradient interpolation system for download backgrounds.
c.colors.downloads.system.bg = 'none'

## Hints
## background color for hints. use rgba value for transparency.
c.colors.hints.bg = '#191c25'

## font color for hints.
c.colors.hints.fg = '#96b5b4'

## hints
c.hints.border = '1px solid ' + '#101010'

## font color for the matched part of hints.
c.colors.hints.match.fg = '#a3be8c'

## background color of the keyhint widget.
c.colors.keyhint.bg = '#191c25'

## text color for the keyhint widget.
c.colors.keyhint.fg = '#96b5b4'

## highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = '#96b5b4'

## Info and error messages
## background color of an error message.
c.colors.messages.error.bg = '#f07178'

## border color of an error message.
c.colors.messages.error.border = '#ff8b92'

## foreground color of an error message.
c.colors.messages.error.fg = '#d0d0d0'

## background color of an info message.
c.colors.messages.info.bg = '#101010'

## border color of an info message.
c.colors.messages.info.border = '#101010'

## foreground color an info message.
c.colors.messages.info.fg = '#d0d0d0'

## background color of a warning message.
c.colors.messages.warning.bg = '#924441'

## border color of a warning message.
c.colors.messages.warning.border = '#d47300'

## foreground color a warning message.
c.colors.messages.warning.fg = '#d0d0d0'

## Prompt
## background color for prompts.
c.colors.prompts.bg = '#4c597d'

## border used around UI elements in prompts.
c.colors.prompts.border = '1px solid ' + '#101010'

## foreground color for prompts.
c.colors.prompts.fg = '#96b5b4'

## background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = '#191c25'

## Caret
## background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = '#191c25'

## foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = '#96b5b4'

## background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = '#191c25'

## foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = '#96b5b4'

## Statusbar
## background color of the statusbar in command mode.
c.colors.statusbar.command.bg = '#101010'

## foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = '#96b5b4'

## background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = '#191c25'

## foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = '#96b5b4'

## background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = '#a3be8c'

## foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = '#191c25'

## background color of the statusbar.
c.colors.statusbar.normal.bg = '#191c25'

## foreground color of the statusbar.
c.colors.statusbar.normal.fg = '#96b5b4'

## background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = '#82aaff'

## foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = '#d0d0d0'

## background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = '#191c25'

## foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = '#96b5b4'

## background color of the progress bar.
c.colors.statusbar.progress.bg = '#d0d0d0'

## foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = '#924441'

## default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = '#d0d0d0'

## foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = '#4c597d'

## foreground color of the URL in the statusbar on successful load
c.colors.statusbar.url.success.http.fg = '#a3be8c'

## foreground color of the URL in the statusbar on successful load
c.colors.statusbar.url.success.https.fg = '#a3be8c'

## foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = '#ffcb6b'

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
c.colors.tabs.bar.bg = '#191c25'

## background color of unselected even tabs.
## type: qtcolor
c.colors.tabs.even.bg = '#191c25'

## Foreground color of unselected even tabs.
## type: qtcolor
c.colors.tabs.even.fg = '#d0d0d0'

## color for the tab indicator on errors.
## type: qtcolor
c.colors.tabs.indicator.error = '#f07178'

## color gradient start for the tab indicator.
## type: qtcolor
c.colors.tabs.indicator.start = '#82aaff'

## color gradient end for the tab indicator.
## type: qtcolor
c.colors.tabs.indicator.stop = '#a3be8c'

## color gradient interpolation system for the tab indicator.
## type: colorsystem
c.colors.tabs.indicator.system = 'none'

## background color of unselected odd tabs.
## type: qtcolor
c.colors.tabs.odd.bg = '#191c25'

## foreground color of unselected odd tabs.
## type: qtcolor
c.colors.tabs.odd.fg = '#d0d0d0'

## background color of selected even tabs.
## type: qtcolor
c.colors.tabs.selected.even.bg = '#191c25'

## foreground color of selected even tabs.
## type: qtcolor
c.colors.tabs.selected.even.fg = '#a3be8c'

## background color of selected odd tabs.
## type: qtcolor
c.colors.tabs.selected.odd.bg = '#191c25'

## foreground color of selected odd tabs.
## type: qtcolor
c.colors.tabs.selected.odd.fg = '#a3be8c'

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

## Aliases
c.aliases = {
    "w": "session-save",
    "wq": "quit --save",
    "mpv": "spawn -d mpv --force-window=immediate {url}",
    'gh': "open -t https://github.com/koltea",
    'wh': "open -t https://alpha.wallhaven.cc/search?q=&categories=111&purity=100&topRange=1y&sorting=toplist&order=desc&colors=336600&page=1",
    'wt': "open -t https://www.webtoons.com/en/",
    'tag': "open -t http://www.tagged.com/home.html",
    'suck': "open -t http://suckless.org/",
}
