#!/bin/sh
# set env variables
export USER_NAME=$(whoami)
export USER_UID=$(id -u)
export USER_GID=$(id -g)
# Linuxを仮定する
export USER_UID=1000
export USER_GID=1000

# open Visual Studio Code
code .
