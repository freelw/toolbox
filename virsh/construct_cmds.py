
import sys

cmds = [
    """virt-install \\
    --virt-type=kvm \\
    --name=%(name)s \\
    --vcpus=16 \\
    --memory=16384 \\
    --location=/linux_images/CentOS-7-x86_64-DVD-1908.iso \\
    --disk path=/home/vms/%(name)s.qcow2,size=850,format=qcow2 \\
    --network bridge=br0 \\
    --graphics vnc,port=%(port)s \\
    --force""",
    """virsh attach-disk centos74 /home/vms/%(name)s.qcow2 vdb --live --cache=none --subdriver=qcow2""",
    """socat TCP-LISTEN:%(port1)s,reuseaddr,fork TCP:localhost:%(port)s"""
]
if '__main__' == __name__:
    name = sys.argv[1]
    port = sys.argv[2]
    port1 = int(port)+1
    dict = {
        'name': name,
        'port': port,
        'port1': port1
    }
    for cmd in cmds:
        print cmd % dict
