#!/bin/sh
#while type dwm >/dev/null ; do dwm && continue || break ; done
xset s off -dpms &
remaps &
xsetroot -cursor_name left_ptr &
mpdnotify &
picom -b &
setbg &
dwmstatus &
theme

initdwm
#exec awesome
