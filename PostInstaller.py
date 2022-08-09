import os


# What it will do is upgrade your system automatically
# The app are going to be install is mpv lutris wine  
# Flakpak is going to be install
# This for Pop os 

os.system('sudo su')
os.system('apt-get update && apt-get full-upgrade')
os.system('apt install wine mpv')
os.system('exit')
os.system('sudo add-apt-repository ppa:lutris-team/lutris')
os.system('sudo su')
os.system('apt update')
os.system('apt install lutris')
os.system('apt install flatpak')
os.system('flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo')
os.system('reboot')

#Done