from setuptools import setup, find_packages
import os 
os.system('sudo apt-get install xclip')
os.system('sudo apt-get install xsel')
os.system('sudo apt-get install wl-clipboard')

setup(
    name='Heb',
    version='5.7.0',
    packages=find_packages(),
    install_requires=['pyperclip'
      
    ],description="Clean your Directory with just one command",
 
)
