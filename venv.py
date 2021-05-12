import os

print("Upgrading pip")
os.system("pip install --upgrade pip")
print("Installing/Updating virtualenv dependency")
os.system("pip install virtualenv")
name = input("What would your like to name the virtual environment?: ")
os.system("virtualenv " + name)
print("virtual environment created.")