#!/bin/bash
echo Button name?
read Bname
mkdir $Bname/
mkdir $Bname/Transparent/
python config-file-creation.py
mv -fv *ini *png $Bname
mv -fv $Bname/*ini $Bname/Transparent/
cp -rv $Bname ~/Documents/Rainmeter/Skins/unFold/
cp -rv $Bname More-Icons-unFold-Rainmeter/
rm -dirf $Bname
mv -fv More-Icons-unFold-Rainmeter/$Bname/*png More-Icons-unFold-Rainmeter/Buttons/Transparent/
cd ~/Documents/Rainmeter/Skins/unFold/$Bname
mv -fv *png ~/Documents/Rainmeter/Skins/unFold/@Resources/Buttons/Transparent