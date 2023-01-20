# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 14:57:14 2023

@author: Ксения
"""

import subprocess
import chardet

def ping(args):
    ping_res = ''
    sub_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in sub_ping.stdout:
        ping_res = chardet.detect(line)
        line = line.decode(ping_res['encoding'])
        print(line)

args_yan = ['ping', 'yandex.ru']
args_you = ['ping', 'youtube.com']

ping(args_yan)
ping(args_you)
