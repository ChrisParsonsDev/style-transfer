# PyTorch Style Transfer

This repo contains a simple Python script for Style Transfer in PyTorch.

The reason I've gone for a script not Jupyter notebook is that it's much easier to use it in our Docker environment than to spend ages opening ports/dealing with network (thanks [kubectl](https://kubernetes.io/docs/tasks/debug-application-cluster/get-shell-running-container/))

Anyway - I hope you find this useful..

You'll need to change lines XX and XY to match your content/style images and the output will end up in:

`output/<loss>.png`
