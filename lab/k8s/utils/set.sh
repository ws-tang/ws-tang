#!/bin/bash

##################################################
# set.sh
#
# This script is for the container to use.
#
# DO NOT use it on the server ubuntu24.
##################################################

hostname=$('hostname')

if [ "$hostname" == "ubuntu24" ]; then
    echo "Cannot run this script on ubuntu24. Exiting..."
    exit;
fi


# Copy the .bashrc and apply it
cp -p /tmp/kind/.bashrc /root/.bashrc
cd /root
source /root/.bashrc


# Make the folder for Kubernetes testing and change to it
mkdir kind
cd kind


# Install the required packages
apt-get update
apt-get --assume-yes install vim

