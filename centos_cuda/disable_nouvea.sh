#!/bin/bash

echo "blacklist nouveau" >> /usr/lib/modprobe.d/dist-blacklist.conf
echo "options nouveau modeset=0" >> /usr/lib/modprobe.d/dist-blacklist.conf
mv /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r).img.bak
dracut /boot/initramfs-$(uname -r).img $(uname -r)
