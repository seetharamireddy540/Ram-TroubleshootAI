import os
import platform
import sys

print(sys.version)
print(platform.system())
print(os.getcwd())

os.system("ls -la")
print(platform.python_implementation())
print(platform.uname().machine)
