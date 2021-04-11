# Arch UEFI EFISTUB Install
**DISCLAIMER**
---
_I am not responsible for any damages, loss of data, system corruption, or any mishap you may somehow cause by following this guide._
_Use at your own risk or use [Arch Wiki](https://wiki.archlinux.org/index.php/installation_guide) as your guide._

#### Before booting from usb stick check your hardware settings
- Disable Secure Boot
- Disable Launch CSM or Legacy Support
- Set Boot Mode to UEFI

#### Burn ISO with CLI using dd
```
  - $ dd bs=4M if=path/to/archlinux.iso of=/dev/sdx status=progress oflag=sync
```

#### Verify the boot mode
  - If the command shows the directory without error, then the system is **UEFI**
```
  - $ efivar -l
```

#### Test internet connection
```
- $ ping -c 3 archlinux.org
```

#### Update system clock
```
  - $ timedatectl set-ntp true
  - $ timedatectl status
```
---
#### Prepare disk
**Mount point** | **Partition** | **Partition type** | **Suggested size**
| :---: | :---: | :---: | :---: |
/mnt/boot | /dev/nvme0n1p1 | EFI system partition | 512 MiB
/mnt | /dev/nvme0n1p2 | Linux Filesystem | Remainder of the device
- **Partition drive**
```
  - $ lsblk -f                # check which drive you want to use
  - $ fdisk /dev/nvme0n1
  - Create GPT disklabel
  - Use the chart above
```
- **Format drive**
```
  - $ mkfs.fat -n BOOT -F 32 /dev/nvme0n1p1
  - $ mkfs.ext4 -L SYSTEM /dev/nvme0n1p2
```
- **Mount disk**
```
  - $ mount /dev/nvme0n1p2 /mnt
  - $ mkdir /mnt/boot
  - $ mount /dev/nvme0n1p1 /mnt/boot
```
---
#### Pacstrap
- **Change dns** if mirrors failed for some reason in _/etc/resolv.conf_
```
  - $ nvim /etc/resolv.conf             # if mirrors failed for some reason
  - nameserver 1.1.1.1
  - $ nvim /etc/pacman.d/mirrorlist     # edit mirrors
```
- **Pacstrap packages**
```
  - $ pacstrap /mnt base base-devel linux linux-firmware
```
---
#### System Configuration
- **Fstab**
```
  - $ genfstab -U /mnt >> /mnt/etc/fstab
```
- **Chroot** into the new system
```
  - $ arch-chroot /mnt
```
- **Set timezone**
```
  - $ ln -sf /usr/share/zoneinfo/Asia/Manila /etc/localtime
  - $ hwclock --systohc --utc
```
- **Localization**
```
  - $ pacman -S neovim
  - $ nvim /etc/locale.gen      # uncomment prefer language
  - $ locale-gen
  - $ echo LANG=en_PH.UTF-8 > /etc/locale.conf
```
- **Network configuration**
```
  - $ echo art > /etc/hostname
  - $ nvim /etc/hosts     # add matching entries to host, with the configuration below
```
```javascript
127.0.0.1    localhost
::1          localhost
127.0.1.1    art.localdomain art
```
- **Install your preferred network management software**
  - **Systemd-networkd**
```
    - $ ip addr                                         # find the name of your network adapter
    - $ systemctl enable systemd-networkd.service
    - $ nvim /etc/systemd/network/20-wired.network      # configure adapter, with the configuration below
```
  - **Networkmanager**
```
    - $ pacman -S networkmanager
    - $ systemctl enable NetworkManager
```
```javascript
[Match]
Name=enp0s31f6

[Network]
DHCP=yes
DNS=1.1.1.1
```
- **Root password**
```
  - $ passwd
```
- **Boot loader**
```
  - $ lsblk -f                          # Get root UUID
  - $ pacman -S efibootmgr intel-ucode
  - $ efibootmgr -b <bootnum> -B        # Delete old boot entry
```
  - create boot entry: Where _/dev/nvme0nX_ and _Y_ are the drive and partition number where the ESP is located.
  ```javascript
  - $ efibootmgr -d /dev/nvme0n1 -p Y -c -L "Arch" -l /vmlinuz-linux -u 'root=UUID=XXX-XXX rw quiet loglevel=3 vga=current nvidia-drm.modeset=1 rd.systemd.show_status=false rd.udev.log_level=3 initrd=\intel-ucode.img initrd=\initramfs-linux.img' --verbose
  ```
- **Exit the chroot environment**
```
  - exit
  - umount -R /mnt
  - reboot
```
  - login as root
```
  - $ pacman -Syu
```
- **Enable multilib**
  - uncomment in _/etc/pacman.conf_
```javascript
[multilib]
include = /etc/pacman.d/mirrorlist
```
  - **Update repository**
```
  - $ pacman -Syu
```
- **Add user**
```
  - $ pacman -S zsh
  - $ useradd -m -G users,wheel,video,audio,storage,disk -s /bin/zsh hoaxdream
  - $ passwd hoaxdream
```
- **Add sudoers**
```
  - $ EDITOR=nvim visudo
```
  - uncomment wheel group
```javascript
%wheel ALL=(ALL) ALL
```
  - logout root
  - login with created username and password
```
  - $ sudo pacman -Syu
```
---
#### Install automatically with script
- **Bootstrap script**
```
  - $ sudo pacman -S git
  - $ git clone https://github.com/hoaxdream/bootstrap
  - $ cd bootstrap
  - $ ./pkgsinstall
  - $ reboot
  - $ ./dotsetup
  - $ sudo ./postinstall
  - $ reboot
  - $ startx
  - $ sudo -E systemctl edit --full systemd-fsck-root.service
  - $ sudo -E systemctl edit --full systemd-fsck@.service
  - $ reboot
```
#### Installation of packages manually
- **Arch AUR helper**
```
  - $ curl -LO https://aur.archlinux.org/cgit/aur.git/snapshot/yay.tar.gz
  - $ tar xvzf yay.tar.gz
  - $ cd yay
  - $ makepkg -sci
```
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
- **Reboot system**
```
- systemctl reboot
```
---
### Window manager
- **Dwm**
```
  - $ git clone https://git.suckless.org/dwm ~/.config/dwm
  - $ git clone https://git.suckless.org/st ~/.config/st
  - $ git clone https://git.suckless.org/dmenu ~/.config/dmenu
  - $ make && sudo make install`-`in each directory and install
```
- **Xmonad**
```
  - $ sudo pacman -S xmonad xmonad-contrib xmobar
```
- **Bspwm**
```
  - $ sudo pacman -S bspwm sxhkd
```
---
### Install dotfiles
```
  - $ alias dot='git --git-dir=$HOME/.config/dots/ --work-tree=$HOME'` - `add to current shell scope
  - $ echo "dots" >> .gitignore
  - $ git clone --bare https://github.com/hoaxdream/dots.git $HOME/.config/dots
  - Remove stock configuration in $HOME, else error will occur.
  - $ dot checkout
  - $ dot config --local status.showUntrackedFiles no
  - $ dot push -u origin master
```
### File manager
- **nnn**
```
  - $ git clone https://github.com/jarun/nnn
  - $ cd nnn
  - $ make O_NERD=1 && sudo make install        # enable icons
  - install advcp nad advmv
  - $ wget http://ftp.gnu.org/gnu/coreutils/coreutils-8.32.tar.xz
  - $ tar xvJf coreutils-8.32.tar.xz
  - $ cd coreutils-8.32/
  - $ wget https://raw.githubusercontent.com/jarun/advcpmv/master/advcpmv-0.8-8.32.patch
  - $ patch -p1 -i advcpmv-0.8-8.32.patch
  - $ ./configure
  - $ make
  - install binaries and use cpg -g and mvg -g instead of cp and mv (prefered)
  - $ sudo mv ./src/cp /usr/local/bin/cpg
  - $ sudo mv ./src/mv /usr/local/bin/mvg
  - $ or install the binaries and create aliases
  - $ sudo mv ./src/cp /usr/local/bin/advcp
  - $ sudo mv ./src/mv /usr/local/bin/advmv
  - $ echo alias cp '/usr/local/bin/advcp -g' >> ~/.config/zsh/aliasrc
  - $ echo alias mv '/usr/local/bin/advmv -g' >> ~/.config/zsh/aliasrc
```
### Start session
```
  - $ startx
```
