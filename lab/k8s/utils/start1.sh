#!/bin/bash

############################################################
# start1.sh
#
# This script is to start a Docker container with only the
# Kubernetes controlplane using kind.
#
# DO NOT use it on the server ubuntu24.
############################################################


# Delete the kind default cluster first, if existing
kind delete cluster


# Start the kind default cluster with only one Docker container
# for the Kubernetes controlplane
kind create cluster --config=kind-ctrlplane.yaml


# Invoke the script to go to the controlplane shell
cd /opt/kind
./goplane.sh

