from setuptools import setup, find_packages
VERSION = '0.0.1'
setup(
    name="ParagMehta",
    version=VERSION,
    author="Parag Mehta",
    author_email="<mehtaparag45@gmail.com>",
    packages=find_packages(),
    keywords=['python', 'percentage','weight','grams','kg','marks'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
setup(
    # ... other metadata ...
    entry_points={
        'console_scripts': [
            'Prog = Prog:marks',
        ],
    },
)
    
   

