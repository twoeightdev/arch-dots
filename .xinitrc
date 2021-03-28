#!/bin/sh
#while type dwm >/dev/null ; do dwm && continue || break ; done
xset s off -dpms &
xrdb ${XDG_CONFIG_HOME:-$HOME/.config}/xorg/Xresources &
remaps &
xsetroot -cursor_name left_ptr &
mpdnotify &
picom -b &
setbg &
dunst &
dwmbar &

exec dwm
