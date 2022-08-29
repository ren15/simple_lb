sudo kubectl create -f k8s/simple-lb.namespace.yaml
sudo kubectl apply -f k8s/simple-lb.deployment.client.yaml -n simple-lb