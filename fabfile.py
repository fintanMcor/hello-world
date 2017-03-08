
from fabric.api import *

import os


# the follwoing sets the enviroemtn variabels to connect to the remote lcoation in this case the bbb
# note i logged in as root with no passowrd and it seems to have worked

env.hosts = ['192.168.7.2']
env.user  = 'root'
env.password=''


# here will get the path, i am not sure if it ges the path from where the fab file is runnign from 
# i need to chekc this then substitue the env.repo_path for the path name
env.repo_path = os.path.dirname(os.path.realpath(__file__))

def hello(name="world"):
    print("Hello %s!"%name)
    
    
    
    



def remote_info():
    # note that the run (' some command") is the same as runnign the command on the remote console
    #run('uname -a')
    run('lsusb')

def local_info():
     # note that the local (' some command") is the same as runnign the command on the remote console
    #local('uname -a')
    local('ls -ail')
 
def upload(): 
    print env.repo_path
    
    #put( "/cygdrive/c/users/home pc/Desktop/Linux_BBB_Python_tutorials/tutorials_code_etc/test_file.txt", "/home/" )
    #put( "/cygdrive/c/git/hello-world/tutorials_code_etc/python_code/threadExample.py", "/home/" )
    put( "/cygdrive/j/ProjectX/galil/dev/tutorials_code_etc/python_code/threadExample.py", "/home/" )
    
   