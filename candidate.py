import os
import getpass
import docker
import requests
import time
from git import Repo

workspace_dir = os.getcwd()+'/workspace'

try:
    shutil.rmtree(workspace_dir)
    print(workspace_dir + ' has been cleaned' )
except OSError as e:
    print("There was no such directory: " + workspace_dir)

try: 
    os.makedirs(workspace_dir)
except OSError:
    print ("Creation of the directory %s failed" % workspace_dir)
else:
    print ("Successfully created the directory %s" % workspace_dir)

Repo.clone_from('git@github.com:guyyosan/python-cherry-container.git', workspace_dir)

client = docker.from_env()
try:
    container = client.containers.get('test_app')
    container.stop()
except:
    print('You are runing this app first time on this machine. Do not forget to turn it off')
client.images.build(path=workspace_dir, tag='application', dockerfile='Dockerfile', labels={'label': 'delete'})
client.containers.run(image='application', detach=True, name='test_app', remove=True, ports = {'8080/tcp': 8080})

attempts = 0
while attempts < 3:
    try:
        response = requests.get('http://127.0.0.1:8080/')
        print('Your app is up and running')
        break
    except requests.exceptions.ConnectionError:
        attempts += 1
        print('Waiting for app is up')
        time.sleep(1) 




