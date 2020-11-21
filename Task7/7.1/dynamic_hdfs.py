import os
import subprocess as sp
from time import sleep

from printHead.printHead import header

header()

mount_point = ""

def start_datanode():
    ap.run("hadoop-daemon.sh start datanode", shell=True)

def stop_datanode():
    sp.run("hadoop-daemon.sh stop datanode", shell=True)

def create_physical_volume():
    deviceName = input("Enter the device name: ")
    sp.run("pvcreate {0}".format(deviceName), shell=True)

def display_physical_volume():
    deviceName = input("Enter the device name: ")
    sp.run("pvdisplay {0}".format(deviceName), shell=True)

def create_volume_group():
    vgName = input("Enter volume group name: ")
    deviceList = ["/dev/xvdf1", "/dev/xvdg1"]
    pvList = ""
    for i in deviceList:
        pvList = pvList + " " + i

    sp.run("vgcreate {0} {1}".format(vgName, pvList), shell=True)

def display_volume_group():
    vgName = input("Enter volume group name: ")
    sp.run("vgdisplay {0}".format(vgName), shell=True)

def create_logical_volume():
    size = int(input("Enter the size of the logical volume in GiB: "))
    lvName = input("Enter the logical volume name: ")
    vgName = input("Enter the volume group name: ")
    sp.run("lvcreate --size {0}G --name {1} {2}".format(size, lvName, vgName), shell=True)

def display_logical_volume():
    sp.run("lvdisplay", shell=True)

def format_logical_volume():
    lvName = input("Enter the logical volume name: ")
    sp.run("mkfs.ext4 {0}".format(lvName), shell=True)

def mount_logical_volume():
    lvName = input("Enter the logical volume name to mount: ")
    mountPoint = input("Enter the location where to mount the logical volume: ")
    mount_point = mountPoint
    sp.run("mount {0} {1}".format(lvName, mountPoint), shell=True)

def increase_logical_volume_size():
    size = input("Enter the size in GiB to increase the size of logical volume: ")
    lvName = input("Enter the name of logical volume: ")
    stop_datanode()
    sp.run("umount {0}".format(mount_point), shell=True)
    sp.run("lvextend --size +{0}G {1}".format(size, lvName), shell=True)
    sp.run("e2fsck -f {0}".format(lvName), shell=True)
    sp.run("resize2fs {0}".format(lvName), shell=True)
    sp.run("mount {0} {1}".format(lvName, mount_point), shell=True)
    start_datanode()

while True:
    header()
    os.system("tput setaf 4")
    print('''
            1. START HADOOP DATANODE
            2. STOP HADOOP DATANODE
            3. CREATE PHYSICAL VOLUME
            4. DISPLAY PHYSICAL VOLUME
            5. CREATE VOLUME GROUP
            6. DISPLAY VOLUME GROUP
            7. CREATE LOGICAL VOLUME
            8. DISPLAY LOGICAL VOLUME
            9. FORMAT LOGICAL VOLUME
            10. MOUNT LOGICAL VOLUME
            11. INCREASE LOGICAL VOLUME SIZE
            12. Exit
            ''')
    os.system("tput setaf 7")

    # Taking user choice to run the command
    choice = int(input("Enter your choice(number): "))

    # Output is displayed in green color
    if choice == 1:
        header()
        start_datanode()
    elif choice == 2:
        header()
        stop_datanode()
    elif choice == 3:
        header()
        create_physical_volume()
    elif choice == 4:
        header()
        display_physical_volume()
    elif choice == 5:
        header()
        create_volume_group()
    elif choice == 6:
        header()
        display_volume_group()
    elif choice == 7:
        header()
        create_logical_volume()
    elif choice == 8:
        header()
        display_logical_volume()
    elif choice == 9:
        header()
        format_logical_volume()
    elif choice == 10:
        header()
        mount_logical_volume()
    elif choice == 11:
        header()
        increase_logical_volume_size()
    elif choice == 12:
        exit()