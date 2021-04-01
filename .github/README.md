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
Package name | Description
:--- | :---
[xmonad](https://github.com/xmonad/xmonad) | tiling window manager configured in Haskell
[dwm](http://suckless.org/) | dynamic window manager for X
[bspwm](https://github.com/baskerville/bspwm) | tiling window manager based on binary space partitioning
[st](http://st.suckless.org/) | simple terminal implementation for X
[dmenu](http://tools.suckless.org/dmenu/) | dynamic menu for X
[Noto Sans Mono](https://archlinux.org/packages/extra/any/noto-fonts/) | main font used
[libxft-bgra](https://aur.archlinux.org/packages/libxft-bgra/) | provides colorful emoji for dwm and dmenu
[nnn](https://github.com/jarun/nnn) | fastest terminal file manager
xorg-server | X graphical server
xorg-xwininfo | print information about windows on an X server
xorg-xprop | property disaplyer for X
xorg-xdpyinfo | display information utility for X
xorg-xset | user preference utility for X
xorg-xsetroot | utility to set your root window background to a given pattern or color
xorg-xinit | X initialisation program
xterm | X Terminal Emulator
xcape | key modifier to act as other keys
xclip | command line interface to the X11 clipboard
xdo | utility for performing actions on windows in X
xdotool | command-line X11 automation tool
nvidia | NVIDIA drivers for linux
nvidia-utils | NVIDIA drivers utilities
lib32-nvidia-utils | NVIDIA drivers utilities (32-bit)
nvidia-settings | tool for configuring the NVIDIA graphics driver
vulkan-icd-loader | vulkan Installable Client Driver (ICD) Loader
lib32-vulkan-icd-loader | vulkan Installable Client Driver (ICD) Loader (32-bit)
mlocate | updatedb implementation
man-db | utility for reading man pages
git | fast distributed version control system
wget | network utility to retrieve files from the web
highlight | fast and flexible source code highlighter (CLI version)
gnome-keyring | stores passwords and encryption keys
python-pynvim | python client for neovim
python-adblock | brave adblock for qutebrowser
zip | compressor/archiver for creating and modifying zipfiles
unzip | for extracting and viewing files in .zip archives
unrar | RAR uncompression program
dosfstools | DOS filesystem utilities
ntfs-3g | NTFS filesystem driver and utilities
xdg-user-dirs | manage user directories
mediainfo | show tag information about a video/audio file (CLI interface)
transmission-cli | cli BitTorrent client
bc | arbitrary precision calculator language
tree | directory listing program displaying a depth indented list of files
pulseaudio-alsa | ALSA Configuration for PulseAudio
pulsemixer | CLI and curses mixer for pulseaudio
pamixer | Pulseaudio command-line mixer like amixer
ttf-joypixels ttf-nerd-fonts-symbols noto-fonts-emoji | emoji/symbol font
ttf-dejavu ttf-liberation | fonts used in my dotfiles
youtube-dl | command-line to download videos from youTube and a few more sites
ffmpeg | recording utility for video and audio on the command line
maim | utility to take a screenshot
sxiv | simple X image viewer
xwallpaper | wallpaper setting utility for X
imagemagick | image viewing/manipulation program
newsboat | rss feed reader for text terminals
picom | X compositor
unclutter | hides an inactive mouse
mpd | lightweight music daemon
mpc | terminal interface for mpd
mpv | media player
ncmpcpp | ncurses interface for music
zathura | pdf viewer
zathura-pdf-mupdf | allows mupdf pdf compatibility in zathura
poppler | manipulates .pdfs and gives .pdf previews
dunst | lightweight notification-daemon
libnotify | library for sending desktop notifications
gucharmap | gnome unicode charmap
qutebrowser | vim-like browser based on PyQt5
steam | valve's digital software delivery system
signal-desktop | private messenger
tremc | curses interface for transmission
