""" Vision System - Socket Function
 
 
@author:    kais, misil.
@created:   2024-07-03
"""

import socket
from typing import Optional
from . import common

# global variables
raddr : tuple
sock : Optional[socket.socket] = None

# ip_addr : str = "192.168.10.148"
# port : int = 2006

ip_addr : str = "192.168.100.102"
port : int = 2006


def get_ip_addr():
    return ip_addr
 
def set_ip_addr(addr: str):
   global ip_addr
   ip_addr = addr
 
def get_port():
   return port
 
def set_port(_port: int):
   global port
   port = _port
   

def is_open():
    return (sock is not None)


def open():
    global raddr, sock, ip_addr, port
    
    if sock is not None: 
        return False
    
    try:
        raddr = (ip_addr, port)
        sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        sock.connect(raddr)
        
    except socket.error as e:
        common.logd("[Failed][vision] open failed")
        return False
    
    common.logd("[vision] open")
    return True



def is_close():
    if sock is not None:
        close()


def close():
    global sock
    if sock is None: 
        return
    
    common.logd("[vision] close")
    sock.close()
    sock = None
 
 
def send_msg(msg):
    if sock is None: 
        return -1
    
    common.logd("[vision] send : " + msg)
    bts = bytes(msg.encode())
    return sock.send(bts) 
    # return sock.sendto(bts, raddr)

 
def recv_msg():
    if sock is None: 
        return ""

    try:
        recv_data = sock.recv(1024).decode()
        common.logd("[vision] recv : " + recv_data)
        return recv_data
    
    except Exception as e:
        common.logd("[Failed][vision] " + str(e))
        return ""


