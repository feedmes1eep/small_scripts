cd ~/Downloads
sudo apt-get install curl -y
curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | sudo apt-key add - 
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
wget -q -O - https://repo.protonvpn.com/debian/public_key.asc | sudo apt-key add - 
sudo add-apt-repository 'deb https://repo.protonvpn.com/debian unstable main'
sudo apt-get update
# add domain to the front of these, i don't want people using my own net bandwidth.
wget 
/ubuntu-files/discord-0.0.13.deb 
/ubuntu-files/vscode-installer.deb
/ubuntu-files/CyberRe_1.0.0.tar.gz
/ubuntu-files/Sweet-cursors.tar.xz
/ubuntu-files/Flat-Remix-GTK-Blue-Darkest-NoBorder.tar.
/ubuntu-files/Flatery-Dark.tar.gz
sudo apt-get install filezilla git make gcc libglib2.0-dev-bin libgtk-3-dev libpolkit-dobject-1-dev protonvpn gnome-tweaks gnome-tweak-tool spotify-client vim ./discord-0.0.13.deb ./vscode-installer.deb -y
for f in *.tar*; do
	tar xf "$f" &
done
wait
mkdir ~/.themes
mv -t ~/.themes Flat-Remix-GTK-Blue-Darkest-NoBorder
sudo mv -t /usr/share/icons/ Sweet-cursors
sudo mv -t /usr/share/icons/ Flatery-Dark
cd 'CyberRe 1.0.0'
./install.sh
git clone https://github.com/thiggy01/gdm-background.git
cd gdm-background
make
sudo make install
ssh-keygen -t rsa -b 4096 -f ~/.ssh/