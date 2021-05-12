import os

print("Upgrading pip")
os.system("pip install --upgrade pip")

file = open("dependencies.txt", "r")
for dependency in file:
    os.system("pip install " + dependency)
    print("Installed " + dependency)
print("\nFinished")
