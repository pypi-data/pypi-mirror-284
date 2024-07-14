from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "claid_designer" / "README.md").read_text()

setup(
    name='claid_designer',
    version='0.0.5',    
    description='Designer for the CLAID framework.',
    url='https://claid.ch',
    author='Patrick Langer (C4DHI)',
    author_email='planger@ethz.ch',
    license='Apache 2',
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['claid',      
                      'matplotlib==3.5.3',      
                      'pyqt5==5.14.2; platform_system=="Linux"',
                      'pyqt5==5.15.10; platform_system=="Darwin"',
                      'opencv-python==4.8.0.76' 
                      ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',  
        'Operating System :: Android',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',        
        'Operating System :: Unix',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',


)
