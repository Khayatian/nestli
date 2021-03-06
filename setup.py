from setuptools import setup

setup(name='dtpy',
      description='Digital Twin in python',
      packages=['dtpy'],
      package_dir={'':'src'},
      version="0.1.0",
      install_requires=[
        'mosaik==3.0.1',
        'pandas==1.4.2',
        'fmpy==0.3.7',
        'pytest==7.1.2',
        'pyyaml==6.0',
        'tables==3.7.0',
        'h5py==3.6.0',
        'requests==2.22.0',
        'requests_ntlm==1.1.0'   
      ]
     )