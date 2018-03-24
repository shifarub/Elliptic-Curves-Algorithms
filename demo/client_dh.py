#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

os.chdir(os.path.dirname(os.path.realpath(__file__)))  # Set working directory to the script location
sys.path.append('..')  # Add parent directory to the path in order to import modules

from socket import *
from algorithms.diffiehellman import DiffieHellman
import pickle

BUFFER_SIZE = 4096

if __name__ == "__main__":

    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("localhost", 1337))

    dh = DiffieHellman()
    dh.askCurveToUse()

    # Attention au pickle.loads() qui peut entrainer une vulnérabilité, utilisé ici tel quel pour l'exemple
    s.send(pickle.dumps(dh.getParameterToSend()))

    dh_parameter = pickle.loads(s.recv(BUFFER_SIZE))
    print("Received parameter: ", dh_parameter)
    dh.completeDiffieHellmanExchange(dh_parameter)

    s.close()