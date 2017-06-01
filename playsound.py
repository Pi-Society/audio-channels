#!/usr/bin/env python

import os
import subprocess
from time import sleep
from threading import Thread

while True:
	os.system('play audio.mp3 &')
	subprocess.check_output("play audio2.mp3 &", shell=True)
	
	sleep(20);