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
cd More-Icons-unFold-Rainmeter/
mv -fv ./$Bname/*png ./Buttons/Transparent
cd ~/Documents/Rainmeter/Skins/unFold/
mv -fv ./$Bname/*png ./@Resources/Buttons/Transparent