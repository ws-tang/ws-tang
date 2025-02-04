# Set up a lab Kubernetes environment

Refer to **Setup the Lab Environment with a Linux Server** for the base lab Linux environment.

The information herein is aggregated and edited. The credits goes to the corresponding documentation and people who kindly share their experience. More details is available at the related links throughtout.

## Kubernetes

Install the Kubernetes packages (run as root or use sudo).

```
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.31/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

ls -l /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.31/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list

apt-get update

apt-get install -y kubelet kubeadm kubectl

apt-mark hold kubelet kubeadm kubectl
```

## Docker

Install Docker related packages (run as root or use sudo).

```
install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

chmod a+r /etc/apt/keyrings/docker.asc

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" |   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

apt-get update

. /etc/os-release && echo "$VERSION_CODENAME"

for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

docker --version

docker run hello-world

```

### Docker Container Setup

The Docker container(s) for the Kubernetes node(s) may need some update without using any customized image that includes the required packages like vim.

([Source](https://stackoverflow.com/questions/37695036/cannot-use-vim-vi-nano-yum-inside-docker-container))

```
docker exec -it containerName|containerId /bin/bash

apt-get update

apt-get install packageName

[Example]
apt-get install packageName

```

## kind

### Install

([Source](https://kind.sigs.k8s.io/docs/user/quick-start/#installing-from-release-binaries))

```
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.26.0/kind-linux-amd64

chmod +x ./kind

mv ./kind /usr/local/bin/kind
```

### Quick kind Commands

```
### Create a kind cluster
# Default cluster context name is "kind".
kind create cluster

OR

kind create cluster --name clusterName

### List kind Clusters
kind get clusters

### Interact with a specific cluster
# The clusterName must be prefixed with "kind-".
kubectl cluster-info --context kind-clusterName

[Example]
kubectl cluster-info --context kind-kind

### Delete a kind Cluster
kind delete cluster --name clusterName

```

### Set Up a Kubernetes Cluster

###

# References

1. [Kubernetes documentation](https://kubernetes.io/docs/home/)

2. [Docker reference documentation](https://docs.docker.com/reference/)

3. kind:

   - [Home]()
   - [Releases](https://github.com/kubernetes-sigs/kind/releases)
   - Installation Configuration: [Node](https://kind.sigs.k8s.io/docs/user/configuration/#nodes) and [Per-Node Options/Kubernetes Version](https://kind.sigs.k8s.io/docs/user/configuration/#kubernetes-version)

4. [A local Kubernetes cluster in seconds with Kind](https://dev.to/jdxlabs/a-local-kubernetes-cluster-in-seconds-with-kind-31lc) by Jérôme Dx.
