#!/bin/bash

# This is a utility script to set up the test environment
# for Kubernetes with kind (Kubernetes in Docker)
export KINDHOME=/opt/kind
export KUBECONFIG=$KINDHOME/k8sconfig.yaml

