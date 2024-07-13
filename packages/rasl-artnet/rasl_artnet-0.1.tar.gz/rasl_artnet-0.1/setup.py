from setuptools import setup

setup(name='rasl-artnet',
      version='0.1',
      description='ARTNet server and gui',
      url='http://github.com/VU-RASL/ARTNet',
      author='Alexandra Watkins',
      author_email='alexandra.watkins@vanderbilt.edu',
      license='MIT',
      packages=['artnet'],
      install_requires=[
        'pyzmq',
        'protobuf',
        'python-dotenv',
        'pyaudio'
      ],
    entry_points = {
        'console_scripts': ['artnet-gui=artnet.command_line:artnetGui'],
    },
      zip_safe=False)