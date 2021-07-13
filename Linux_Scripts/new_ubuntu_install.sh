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
/ubuntu-files/vscode_installer.deb
/ubuntu-files/CyberRe_1.0.0.tar.gz
/ubuntu-files/Sweet-cursors.tar.xz
/ubuntu-files/Flat-Remix-GTK-Blue-Darkest-NoBorder.tar.
/ubuntu-files/Flatery-Dark.tar.gz
sudo apt-get install filezilla git make gcc vim thonny protonvpn gnome-tweaks gnome-tweak-tool spotify-client vim ./discord-0.0.13.deb ./vscode_installer.deb -y
for f in *.tar*; do
	tar xf "$f" &
done
wait
mkdir ~/git && cd ~/git
git clone https://github.com/kp300/BACKGROUND-LOGIN-SCREEN.git
curl -O https://raw.githubusercontent.com/bb010g/betterdiscordctl/master/betterdiscordctl
chmod +x betterdiscordctl
sudo mv betterdiscordctl /usr/local/bin
ssh-keygen -t rsa -b 4096