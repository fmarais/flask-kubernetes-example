# Flask Example for Docker and Kubernetes


## To Build in kubernetes
```
## Clone repo
git clone git@github.com:maraisf/flask-kubernetes-example.git

## Go to project root
cd flask-kubernetes-example

## Build image
docker build -t flask-kubernetes-example:0.0.1 .

---

## Start minikube
minikube start

## Set docker env
eval $(minikube docker-env)

## Run in minikube
kubectl run flask-kubernetes-example --image=flask-kubernetes-example:0.0.1 --image-pull-policy=Never

## Check that it's running
kubectl get pods

## Create service for port 5000

Important note: You have to run eval $(minikube docker-env) on each terminal you want to use, since it only sets the environment variables for the current shell session.

```