import requests
import json
from createProject import testBedProject, gns3Creds


baseUrl = "http://localhost:3080/v2/"
username = gns3Creds['username']
password = gns3Creds['password']
projectId = testBedProject['project_id']

rtr01Details = {
    "compute_id": "vm",
    "name": "RTR01",
    "symbol": ":/symbols/affinity/circle/blue/router_cloud.svg",
    "node_type": "qemu",
        "properties": {
        "adapter_type": "vmxnet3",
        "hda_disk_image": "csr1000v-universalk9.16.12.03-serial.qcow2",
        "hda_disk_image_md5sum": "2aba82d78091b4603224a13710399447",
        "qemu_path": "/usr/bin/qemu-system-x86_64",
        "ram": 3072,
        "adapters": 4,
        },
    "label": {
        "rotation": 0,
        "style": "font-family: TypeWriter;font-size: 10.0;font-weight: bold;fill: #000000;fill-opacity: 1.0;",
        "text": "RTR01",
        "x": -2,
        "y": -25
    },
    }

rtr02Details = {
    "compute_id": "vm",
    "name": "RTR02",
    "symbol": ":/symbols/affinity/circle/blue/router_cloud.svg",
    "node_type": "qemu",
        "properties": {
        "adapter_type": "vmxnet3",
        "hda_disk_image": "csr1000v-universalk9.16.12.03-serial.qcow2",
        "hda_disk_image_md5sum": "2aba82d78091b4603224a13710399447",
        "qemu_path": "/usr/bin/qemu-system-x86_64",
        "ram": 3072,
        "adapters": 4,
        },
    "label": {
        "rotation": 0,
        "style": "font-family: TypeWriter;font-size: 10.0;font-weight: bold;fill: #000000;fill-opacity: 1.0;",
        "text": "RTR02",
        "x": -2,
        "y": -25
    },
        "x": 200
    }

mgts01Details = {
    "compute_id": "vm",
    "name": "MGTSW01",
    "symbol": ":/symbols/affinity/circle/blue/switch_multilayer.svg",
    "node_type": "iou",
        "properties": {
        "path": "i86bi-linux-l2-adventerprisek9-15.6.0.9S.bin",
        "use_default_iou_values": True
        },
    "y": 175
    }

cloudDetails = {
    "compute_id": "local",
    "name": "cloud",
    "node_type": "cloud",
    "x":  -180,
    "symbol": ":/symbols/affinity/circle/blue/cloud.svg"
}
def createNodes():
    requests.post (url=baseUrl+'projects/'+projectId+'/nodes', data=json.dumps(rtr01Details), auth=(username,password))
    requests.post (url=baseUrl+'projects/'+projectId+'/nodes', data=json.dumps(rtr02Details), auth=(username,password))
    requests.post (url=baseUrl+'projects/'+projectId+'/nodes', data=json.dumps(mgts01Details), auth=(username,password))
    requests.post (url=baseUrl+'projects/'+projectId+'/nodes', data=json.dumps(cloudDetails), auth=(username,password))