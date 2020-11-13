1. tke 选择virtual gpu
2. 给node打标签
    
    kubectl label node *.*.*.* nvidia-device-enable=enable

3. 加载nvidia设备文件
    
    nvidia-modprobe -u -c=0

    #执行之后会生成这个设备文件 /dev/nvidia-uvm

4. 测试gpu
    
    kubectl apply -f tf-pod.yaml

5. 进如pod
    
    kubectl exec tf-pod -it -- bash

6. NVIDIA Container Toolkit

    # 更多信息参见 https://github.com/NVIDIA/nvidia-docker
    distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
    curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.repo | sudo tee /etc/yum.repos.d/nvidia-docker.repo
    yum install -y nvidia-container-toolkit

7. 测试 NVIDIA Container Toolkit

    sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi

