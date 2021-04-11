#### Void Installation Guide
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
  - $ mkfs.fat -F 32 /dev/nvme0n1p1
  - $ mkfs.ext4 /dev/nvme0n1p2
```
- **Mount disk**
```
  - $ mount /dev/nvme0n1p2 /mnt
  - $ mkdir /mnt/boot
  - $ mount /dev/nvme0n1p1 /mnt/boot
```
---
#### Base Installation
```
  - $ REPO=https://alpha.de.repo.voidlinux.org/current
  - $ ARCH=x86_64
  - $ XBPS_ARCH=$ARCH xbps-install -S -r /mnt -R "$REPO" base-system
```

#### Configuration
- **Enter Chroot**
```
  - $ mount --rbind /sys /mnt/sys && mount --make-rslave /mnt/sys
  - $ mount --rbind /dev /mnt/dev && mount --make-rslave /mnt/dev
  - $ mount --rbind /proc /mnt/proc && mount --make-rslave /mnt/proc
  - $ for dir in dev proc sys run; do mount --rbind /$dir /mnt/$dir; mount --make-rslave /mnt/$dir; done  # alternative
  - $ cp /etc/resolv.conf /mnt/etc/
  - $ PS1='(chroot) # ' chroot /mnt/ /bin/bash
```
- **Installation Configuration**
```
  - $ vim /etc/hostname  # Specify hostname
  - Go through the options in /etc/rc.conf.
  - If installing a glibc distribution, edit /etc/default/libc-locales, uncommenting desired locales.
  - $ xbps-reconfigure -f glibc-locales  # generat locale files
  - $ passwd  # Set password
  - $ cp /proc/mounts /etc/fstab  # Generate fstab
  - Remove lines in /etc/fstab that refer to proc, sys, devtmpfs and pts.
  - Replace references to /dev/sdXX, /dev/nvmeXnYpZ, etc. with their respective UUID
```
- **Fstab**
```
  - Change the last zero of the entry for / to 1, and the last zero of every other
  - line to 2. These values configure the behaviour of fsck.
  - Example below
  /dev/sda1       /boot/EFI   vfat    rw,relatime,[...]       0 0
  /dev/sda2       /           ext4    rw,relatime             0 0

  UUID=6914[...]  /boot/EFI   vfat    rw,relatime,fmask=0022,dmask=0022,codepage=437,iocharset=ascii,shortname=mixed,utf8,errors=remount-ro  0 2
  UUID=dc1b[...]  /           ext4    rw,relatime             0 1
  - Add an entry to mount /tmp in RAM:
  tmpfs           /tmp        tmpfs   defaults,nosuid,nodev   0 0
```
-- **Dracut**
```
  - $ echo hostonly=yes >> /etc/dracut.conf
```
-- **Finishing install**
```
  - $ xbps-install -Su void-repo-nonfree intel-ucode
```
- **EFIBSTUB**
```
  - $ ROOT_UUID=$(blkid -s UUID -o value /dev/nvme0n1p2)
  - $ efibootmgr -d /dev/nvme0n1 -p Y -c -L "Arch" -l /vmlinuz-5.11.12_1 -u 'root=UUID=$ROOT_UUID rw quiet initrd=\initramfs-5.11.12_1.img' --verbose
```
- **GRUB**
```
  - $ xbps-install grub-x86_64-efi
  - $ grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id="Void"
```
- **Finalization**
```
  - $ xbps-reconfigure -fa linux<major>.<minor>
  - $ exit
  - $ umount -R /mnt
  - $ reboot
```
- **Post Install**
```
  - $ xbps-install -S zsh
  - $ useradd -m -G users,wheel,input,video,audio,storage,disk -s /bin/zsh hoaxdream
  - $ passwd hoaxdream
  - $ EDITOR=nvim visudo
```

#### Packages

- xorg-server
- xwininfo
- xprop
- xdpyinfo
- xset
- xsetroot
- xinit
- xterm
- xcape
- xclip
- xdo
- xdotool
- nvidia
- nvidia-libs
- nvidia-libs-32bit
- vulkan-loader
- vulkan-loader-32bit
- mlocate
- man-db
- git
- wget
- python3-adblock
- zip
- unzip
- unrar
- dosfstools
- ntfs-3g
- xdg-user-dirs
- mediainfo
- bc
- tree
- alsa-plugins-pulseaudio
- pulsemixer
- pamixer
- noto-fonts-emoji
- noto-fonts-ttf
- dejavu-fonts-ttf
- liberation-fonts-ttf
- fonts-roboto-ttf
- font-ibm-plex-ttf
- youtube-dl
- ffmpeg
- maim
- sxiv
- xwallpaper
- ImageMagick
- newsboat
- picom
- mpd
- mpc
- mpv
- ncmpcpp
- zathura
- zathura-pdf-mupdf
- poppler
- dunst
- libnotify
- gucharmap
- qutebrowser
- steam
- Signal-Desktop
- tremc

#### dwm
- base-devel libX11-devel libXft-devel libXinerama-devel
