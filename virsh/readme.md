# kvm 相关操作

## 添加磁盘

    virsh attach-disk centos74 /var/linux/images/centos74-add.qcow2 vdb --live --cache=none --subdriver=qcow2