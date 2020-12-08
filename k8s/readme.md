## k8s disk pressure导致evicted的临时解决方案

    在文件 /var/lib/kubelet/kubeadm-flags.env 中增加选项

    --eviction-hard=nodefs.available<1Gi

这样可以降低磁盘驱逐阈值

然后重启kubelet

    systemctl restart kubelet

删除被驱逐的pod

    kubectl get pods | grep Evicted | awk '{print $1}' | xargs kubectl delete pod

    

    