#!/bin/sh
xset s off -dpms &
remaps &
xsetroot -cursor_name left_ptr &
mpdnotify &
picom -b &
setbg &
dwmstatus &
#signal-daemon &
theme

initdwm
