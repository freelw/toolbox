安装插件
    kubectl create -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/master/nvidia-device-plugin.yml

kubectl describe node <nodeip>

    Capacity:
    cpu:                20
    ephemeral-storage:  358225Mi
    hugepages-1Gi:      0
    hugepages-2Mi:      0
    memory:             263608108Ki
    nvidia.com/gpu:     2
    pods:               256
    Allocatable:
    cpu:                19800m
    ephemeral-storage:  338063523281
    hugepages-1Gi:      0
    hugepages-2Mi:      0
    memory:             262481708Ki
    nvidia.com/gpu:     2
    pods:               256

测试gpu
kubectl apply -f tf-pod.yaml

进如pod
kubectl exec tf-pod -it -- bash
