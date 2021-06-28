import subprocess
import os


subprocess.run('python3 -m venv venv/', shell=True)
subprocess.run('source venv/bin/activate && pip install -r requirements.txt', shell=True, executable='/bin/bash')

