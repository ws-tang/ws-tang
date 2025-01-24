# Kubernetets Lab Utilties

## Scripts

- **kind.bashrc**: used along with **set.sh** and **start1.sh** to set up
- **goplane.sh**: the script for shell access the kind controlplane node
  the shell environment for shell access of the kind controlplane node
- **set.sh**: the script to set up the Kubernetes environment, including convenience aliases and the related packages
- **setenv.sh**: set the environment variable on the Linux server that runs kind environment
- **start1.sh**: start a one-node kind cluster (controlplane node only)

<br/>

## Configuration

- **kind-cluster2Nodes.yaml**: the sample kind config yaml file for a 2-node cluster (the controlplane node and one worker node)
- **kind-ctrlplanes.yaml**: the sample kind config yaml file for a 1-node cluster (controlplane node only)
