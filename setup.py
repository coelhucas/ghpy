from setuptools import setup

setup(
    name='ghpy',
    version='0.1',
    description='Control GitHub from your terminal.',
    author='Lucas (lcrabbit) Coelho',
    author_email='lucascoelhodacosta@gmail.com',
    packages=['ghpy'],
    install_requires=['click', 'colorama', 'PyGithub']
)