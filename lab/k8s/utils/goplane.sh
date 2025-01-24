#!/bin/bash 

########################################
# goplane.sh
# 
# This script copy the script .bashrc
# to the container mounted folder and
# start a shell to the container that
# runs Kubernetes controlplane.
#
# Created: 2025-02-05
########################################



CMD_CONTAINER_ID="docker container ls | cut -d ' ' -f 1"

containerId=''


# Execute the command and read its output line by line
while read -r line; do

  if [ "$line" != "CONTAINER" ]; then
    containerId=$line
  fi

done < <(eval "$CMD_CONTAINER_ID")


# Copy the scripts for the container use
cp -p /opt/kind/kind.bashrc /tmp/kind/.bashrc
cp -p /opt/kind/set.sh /tmp/kind/.
cp -p /opt/kind/sethelm.sh /tmp/kind/.


# Start a bash shell to the controlplane container
docker exec -it "$containerId" /bin/bash



