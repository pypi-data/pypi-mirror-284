from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        subprocess.check_call(['chmod', '+x', 'install_dependencies.sh'])
        subprocess.check_call(['./install_dependencies.sh'])

setup(
    name='Heb',
    version='5.5.0',
    packages=find_packages(),
    install_requires=['pyperclip'],
    description="Clean your Directory with just one command",
    cmdclass={
        'install': PostInstallCommand,
    },
)
