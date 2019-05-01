# Flask Example for Docker and Kubernetes with Debugging


## To build in kubernetes
```
## --- docker
## Clone repo
git clone git@github.com:maraisf/flask-kubernetes-example.git


## Build image
cd ~/projects/python/flask-kubernetes-example && docker build -t flask-kubernetes-example:0.0.1 .

## --- minikube
## Start minikube
> minikube start

## Set docker env
> eval $(minikube docker-env)
Important note: You have to run eval $(minikube docker-env) on each terminal you want to use, since it only sets the environment variables for the current shell session.

## Run in minikube
> kubectl run flask-kubernetes-example --image=flask-kubernetes-example:0.0.1 --image-pull-policy=Never --labels="app=flask-kubernetes-example"

## Check that it's running
> kubectl get pods

## Create the service
> kubectl create -f service.yaml

## Curl test
> curl http://<minikube ip>:<web cluster port>
Hello world!

## Curl debug start
> curl http://<minikube ip>:<web cluster port>/debug
now connect using nc
> nc <minikube ip> <debug cluster port>
```


## One liner, rebuild docker image, remove old kubernetes deploy, create new deploy
```
> cd ~/projects/python/flask-kubernetes-example && docker build -t flask-kubernetes-example:0.0.1 . && kb delete deploy flask-kubernetes-example && kubectl run flask-kubernetes-example --image=flask-kubernetes-example:0.0.1 --image-pull-policy=Never --labels="app=flask-kubernetes-example"
```


## Debugging and port setup from container to cluster
```
web (python flask): 
	docker container (Dockerfile): 5000
	node port (service.yaml ): 5001
	cluster port: 3xxxx
	connect: > curl http://<minikube ip>:<web cluster port>/debug

debug (rpdb):
	docker container (Dockerfile): 4444
	node port (service.yaml ): 4445
	cluster port: 3xxxx
	connect: nc <minikube ip> <debug cluster port>
```






