# Set up a lab Kubernetes environment

Refer to [**Setup the Lab Environment with a Linux Server**](../linuxBase.md) for the base lab Linux environment.

The information herein is aggregated from different sources with my edit. The credits goes to the corresponding documentation and people who kindly share their experience. More details is available at the related links below.

**Table of Contents**

- [Kubernetes](#k8s)
- [Docker](#docker)
- [Helm](#helm)
- [Go Programming Language](#golang)
- [References](#refs)

<br/>

## Kubernetes <a name="k8s"></>

### Installation

Install the Kubernetes packages (run as root or use sudo).

```
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.31/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

ls -l /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.31/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list

apt-get update

apt-get install -y kubelet kubeadm kubectl

apt-mark hold kubelet kubeadm kubectl
```

<br/>

### Helpful Kubernetes commands

[Kubernetes cheatsheet](https://kubernetes.io/docs/reference/kubectl/quick-reference/)

```
# Set the current context to a specific namespace other than default
kubectl config set-context --current --namespace=namespaceName

# Get the pod name
kubectl get pods -n nameSpaceName

# Access the pod shell (in the Docker container)
kubectl exec -it podName -c containerN -- /bin/sh
```

<br/>

## Docker <a name="docker"></>

Install Docker related packages (run as root or use sudo)

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

<br/>

### Docker Container Setup

#### Install packages in the Docker container

The Docker container(s) for the Kubernetes node(s) may need some update without using any customized image that includes the required packages like vim.

([Source](https://stackoverflow.com/questions/37695036/cannot-use-vim-vi-nano-yum-inside-docker-container))

```
docker exec -it containerName|containerId /bin/bash

apt-get update

apt-get install packageName

[Example]
apt-get install packageName

```

#### Copy files between a Docker container and the host

([Source](https://stackoverflow.com/questions/28302178/how-can-i-add-a-volume-to-an-existing-docker-container) and [Docker reference](https://docs.docker.com/reference/cli/docker/container/cp/))

```
docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH

docker cp [OPTIONS] SRC_PATH CONTAINER:DEST_PATH
```

### Tutorials and Documentation

- [Docker Docs](https://docs.docker.com/)
- [Play with Docker](https://training.play-with-docker.com) (hands-on tutorials)

<br/>

## Helm <a name="helm"></a>

Helm helps you manage Kubernetes applications — Helm Charts help you define, install, and upgrade even the most complex Kubernetes application. ([Source](https://helm.sh/))

<br/>

### Install Helm for Ubuntu

(Source: [](https://helm.sh/docs/intro/install/))

```
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```

<br/>

## Go Programming Language <a name="golang"></a>

([Source](https://go.dev/doc/install))

1. **Remove any previous Go installation** by deleting the /usr/local/go folder (if it exists), then extract the archive you just downloaded into /usr/local, creating a fresh Go tree in /usr/local/go:

```
rm -rf /usr/local/go && tar -C /usr/local -xzf go1.23.5.linux-amd64.tar.gz
```

(You may need to run the command as root or through sudo).

2.  **Do not** untar the archive into an existing /usr/local/go tree. This is known to produce broken Go installations.
    Add /usr/local/go/bin to the PATH environment variable.

3.  You can do this by adding the following line to your $HOME/.profile or /etc/profile (for a system-wide installation):

```
export PATH=$PATH:/usr/local/go/bin
```

**Note**: Changes made to a profile file may not apply until the next time you log into your computer. To apply the changes immediately, just run the shell commands directly or execute them from the profile using a command such as source $HOME/.profile.
Verify that you've installed Go by opening a command prompt and typing the following command:

```
go version
```

4. Confirm that the command prints the installed version of Go.

<br/>

## kind

### Install

([Source](https://kind.sigs.k8s.io/docs/user/quick-start/#installing-from-release-binaries))

```
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.26.0/kind-linux-amd64

chmod +x ./kind

mv ./kind /usr/local/bin/kind
```

<br/>

### Quick kind commands

```
### Create a kind cluster
# Default cluster context name is "kind".
kind create cluster

OR

kind create cluster --name clusterName

### Create a kind cluster with

### List kind clusters
kind get clusters

### Interact with a specific cluster
# The clusterName must be prefixed with "kind-".
kubectl cluster-info --context kind-clusterName

[Example]
kubectl cluster-info --context kind-kind

### Access the shell of the Docker container(s) of Kubernetes nodes
# Get the container name/Id
docker ps -a

docker exec -it containerName|containerId /bin/bash

### Delete a kind Cluster
kind delete cluster --name clusterName

```

<br/>

### Set up a Kubernetes cluster with kind

A sample kind configuration for a two-node cluster (one controlplane and one worker) is as follows.
([Reference 1](https://kind.sigs.k8s.io/docs/user/configuration/#per-node-options) and [Reference 2](https://kind.sigs.k8s.io/docs/user/quick-start/#configuring-your-kind-cluster))

```
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
#
# A cluster of the nodes:
#   - Controlplane Node: 1
#   - Worker node: 1
#
# While these will not add more real compute capacity and
# have limited isolation, this can be useful for testing
# rolling updates etc.
#
# The API-server and other control plane components will be
# on the control-plane node.
#
# You probably don't need this unless you are testing Kubernetes itself.
nodes:
- role: control-plane
  # Ensure to use the proper Kubernetes release
  image: kindest/node:v1.31.4@sha256:2cb39f7295fe7eafee0842b1052a599a4fb0f8bcf3f83d96c7f4864c357c6c30
  # Add a mount from /path/to/my/files on the host to /files on the node
  extraMounts:
  - hostPath: /tmp/kind
    containerPath: /tmp/kind
- role: worker
  image: kindest/node:v1.31.4@sha256:2cb39f7295fe7eafee0842b1052a599a4fb0f8bcf3f83d96c7f4864c357c6c30
  extraMounts:
  - hostPath: /tmp/kind
    containerPath: /tmp/kind
```

I have some [utilities scripts](utils/k8sutils.md) available for convenience.

<br/>

## References <a name="refs"></a>

1. [Kubernetes documentation](https://kubernetes.io/docs/home/)

2. [Docker reference documentation](https://docs.docker.com/reference/)

3. kind:

   - [Home]()
   - [Releases](https://github.com/kubernetes-sigs/kind/releases)
   - Installation Configuration: [Node](https://kind.sigs.k8s.io/docs/user/configuration/#nodes) and [Per-Node Options/Kubernetes Version](https://kind.sigs.k8s.io/docs/user/configuration/#kubernetes-version)

4. [A local Kubernetes cluster in seconds with Kind](https://dev.to/jdxlabs/a-local-kubernetes-cluster-in-seconds-with-kind-31lc) by Jérôme Dx.
