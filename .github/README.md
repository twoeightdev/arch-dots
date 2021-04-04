## Overview

* Arch linux dotfiles for [bspwm](https://github.com/baskerville/bspwm) [dwm](http://suckless.org/) & [xmonad](https://github.com/xmonad/xmonad)
* EFISTUB Arch Linux Installation [Guide](https://github.com/hoaxdream/dots/blob/main/.github/INSTALL.md)
* [Dependencies](https://github.com/hoaxdream/dots#dependencies)

## Xmonad
![Rice screen preview0000](https://i.imgur.com/hxUN5V0.png)
![Rice screen preview0001](https://i.imgur.com/exIs3Ot.png)
![Rice screen preview0002](https://i.imgur.com/O8RrjFG.png)

## Dwm
![Rice screen preview0003](https://i.imgur.com/caDawRq.png)
![Rice screen preview0004](https://i.imgur.com/5dFAWk4.png)

## Dotfiles installation
*Dwm is the default wm, just change xinitrc if you want to use bspwm or xmonad.*
*Read the commented lines in bootstrap scripts and change accordingly for your system*
```javascript
- $ alias dot='git --git-dir=$HOME/.config/dots/ --work-tree=$HOME'` - `add to current shell scope
- $ echo "dots" >> .gitignore
- $ git clone --bare https://github.com/hoaxdream/dots.git $HOME/.config/dots
- Remove stock configuration in $HOME, else error will occur.
- $ dot checkout
- $ dot config --local status.showUntrackedFiles no
- $ dot push -u origin master
```
 ---
## Dependencies
**Tag** | **Package** | **Description**
| :---: | :---: | :---: |
M | [xmonad](https://github.com/xmonad/xmonad) | tiling window manager configured in Haskell
G | [dwm](http://suckless.org/) | dynamic window manager for X
M | [bspwm](https://github.com/baskerville/bspwm) | tiling window manager based on binary space partitioning
G | [st](http://st.suckless.org/) | simple terminal implementation for X
G | [dmenu](http://tools.suckless.org/dmenu/) | dynamic menu for X
A | [libxft-bgra](https://aur.archlinux.org/packages/libxft-bgra/) | provides colorful emoji for dwm and dmenu
G | [nnn](https://github.com/jarun/nnn) | fastest terminal file manager
M | xorg-server | graphical server
M | xorg-xwininfo | print information about windows on an X server
M | xorg-xprop | property disaplyer for X
M | xorg-xdpyinfo | display information utility for X
M | xorg-xset | user preference utility for X
M | xorg-xsetroot | utility to set your root window background to a given pattern or color
M | xorg-xinit | X initialisation program
M | xterm | X Terminal Emulator
M | xcape | key modifier to act as other keys
M | xclip | command line interface to the X11 clipboard
M | xdo | utility for performing actions on windows in X
M | xdotool | command-line X11 automation tool
M | nvidia | NVIDIA drivers for linux
M | nvidia-utils | NVIDIA drivers utilities
M | lib32-nvidia-utils | NVIDIA drivers utilities (32-bit)
M | nvidia-settings | tool for configuring the NVIDIA graphics driver
M | vulkan-icd-loader | vulkan Installable Client Driver (ICD) Loader
M | lib32-vulkan-icd-loader | vulkan Installable Client Driver (ICD) Loader (32-bit)
M | mlocate | updatedb implementation
M | man-db | utility for reading man pages
M | git | fast distributed version control system
M | wget | network utility to retrieve files from the web
M | highlight | fast and flexible source code highlighter (CLI version)
M | gnome-keyring | stores passwords and encryption keys
M | python-pynvim | python client for neovim
M | python-adblock | brave adblock for qutebrowser
M | zip | compressor/archiver for creating and modifying zipfiles
M | unzip | for extracting and viewing files in .zip archives
M | unrar | RAR uncompression program
M | dosfstools | DOS filesystem utilities
M | ntfs-3g | NTFS filesystem driver and utilities
M | xdg-user-dirs | manage user directories
M | mediainfo | show tag information about a video/audio file (CLI interface)
M | transmission-cli | cli BitTorrent client
M | bc | arbitrary precision calculator language
M | tree | directory listing program displaying a depth indented list of files
M | pulseaudio-alsa | ALSA Configuration for PulseAudio
M | pulsemixer | CLI and curses mixer for pulseaudio
M | pamixer | Pulseaudio command-line mixer like amixer
M | ttf-joypixels ttf-nerd-fonts-symbols noto-fonts-emoji | emoji/symbol font
M | ttf-dejavu ttf-liberation noto-fonts ttf-roboto-mono ttf-ibm-plex | fonts used in my dotfiles
M | youtube-dl | command-line to download videos from youTube and a few more sites
M | youtube-viewer | command line utility for viewing youTube videos
M | ffmpeg | recording utility for video and audio on the command line
M | maim | utility to take a screenshot
M | sxiv | simple X image viewer
M | xwallpaper | wallpaper setting utility for X
M | imagemagick | image viewing/manipulation program
M | vifm | file manager with curses interface
M | newsboat | rss feed reader for text terminals
M | picom | X compositor
M | calcurse | text-based personal organizer
M | unclutter | hides an inactive mouse
M | mpd | lightweight music daemon
M | mpc | terminal interface for mpd
M | mpv | media player
M | ncmpcpp | ncurses interface for music
M | zathura | pdf viewer
M | zathura-pdf-mupdf | allows mupdf pdf compatibility in zathura
M | poppler | manipulates .pdfs and gives .pdf previews
M | dunst | lightweight notification-daemon
M | libnotify | library for sending desktop notifications
M | gucharmap | gnome unicode charmap
M | qutebrowser | vim-like browser based on PyQt5
M | steam | valve's digital software delivery system
M | signal-desktop | private messenger
A | libxft-bgra | fix crashing when viewing color emojis
A | tremc | curses interface for transmission
