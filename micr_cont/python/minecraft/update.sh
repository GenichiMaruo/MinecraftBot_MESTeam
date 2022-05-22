#!/bin/bash

wget -O /tmp/python.zip https://room404.is.oit.ac.jp/minecraft/python.zip
unzip -o /tmp/python.zip -d ./micr_cont/
rm /tmp/python.zip

wget -O /tmp/control.c https://room404.is.oit.ac.jp/minecraft/micr_cont/control.c
mv /tmp/control.c ./micr_cont/
wget -O /tmp/control.h https://room404.is.oit.ac.jp/minecraft/micr_cont/control.h
mv /tmp/control.h ./micr_cont/