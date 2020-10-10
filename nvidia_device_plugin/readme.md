1. tke 选择virtual gpu
2. 给node打标签
    
    kubectl label node *.*.*.* nvidia-device-enable=enable

3. 加载nvidia设备文件
    
    nvidia-modprobe -u -c=0

4. 测试gpu
    
    kubectl apply -f tf-pod.yaml

5. 进如pod
    
    kubectl exec tf-pod -it -- bash
