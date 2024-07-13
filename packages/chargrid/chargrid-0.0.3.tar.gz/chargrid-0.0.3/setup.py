from setuptools import setup, find_packages

setup(
    name='chargrid',
    version='0.0.3',
    description='HackNet-style grid-based game engine framework.',
    author='James Evans',
    author_email='joesaysahoy@gmail.com',
    url='https://github.com/primal-coder/chargrid',
    packages=find_packages(),
    install_requires=['gridengine_framework', 'CharActor', 'CharMonster', 'CharObj', 'dicepy', 'entyty'],
    keywords='gridengine_framework CharActor grid character rpg game engine framework chargrid cell grid-based cell-based dnd d&d dungeons and dragons dungeon dragons'    
)