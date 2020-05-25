#!/bin/bash
echo Button name?
read Bname
mkdir $Bname/
mkdir $Bname/Transparent/
python config-file-creation.py
mv -fv *ini *png $Bname
mv -fv $Bname/*ini $Bname/Transparent/
cp -rfv $Bname ~/Documents/Rainmeter/Skins/unFold/
mv -fv $Bname More-Icons-unFold-Rainmeter/
mv -fv More-Icons-unFold-Rainmeter/$Bname/*png More-Icons-unFold-Rainmeter/Buttons/Transparent
cd ~/Documents/Rainmeter/Skins/unFold/
mv $Bname/*png @Resources/Buttons/Transparent/