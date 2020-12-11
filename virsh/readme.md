# kvm 相关操作

## 安装kvm资料

    https://github.com/jaywcjlove/handbook/blob/master/CentOS/CentOS7%E5%AE%89%E8%A3%85KVM%E8%99%9A%E6%8B%9F%E6%9C%BA%E8%AF%A6%E8%A7%A3.md#bridge%E6%A8%A1%E5%BC%8F%E9%85%8D%E7%BD%AE

## 添加磁盘

    virsh attach-disk centos74 /var/linux/images/centos74-add.qcow2 vdb --live --cache=none --subdriver=qcow2

## 使用图形界面安装（vnc）

    virt-install \
        --virt-type=kvm \
        --name=tarsee2 \
        --vcpus=16 \
        --memory=16384 \
        --location=/linux_images/CentOS-7-x86_64-DVD-1908.iso \
        --disk path=/home/vms/tarsee2.qcow2,size=850,format=qcow2 \
        --network bridge=br0 \
        --graphics vnc,port=5910 \
        --force

## 使用命令行安装

    --graphics none \
    --extra-args='console=ttyS0' \

## socat给vnc打洞（vnc监听在localhost 所以要打洞）

    socat TCP-LISTEN:5912,reuseaddr,fork TCP:localhost:5910

## 使用这个脚本帮助生成命令

    python construct_cmds.py <name> <port>
