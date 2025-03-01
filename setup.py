from setuptools import setup, find_packages
import os

data_files = []

for root, dirs, files in os.walk('configuration'):
    data_files.append(
        (os.path.relpath(root, "configuration"),
         [os.path.join(root, f) for f in files])
    )
setup(
    name='ram_troubleshoot_ai',
    version='1.0',
    description='A brief description of your package',
    author='Ram Mittala',
    author_email='seetharamireddy540@gmail.com',
    packages=find_packages(where="src", exclude=("test")),
    package_dir={"": "src"},
    data_files=data_files,
    entry_points={
        'console_scripts': [
            'ram_troubleshoot_ai=ram_troubleshoot_ai.genai:main',
        ],
    },
    install_requires=[
        'fastapi',
        'uvicorn',
        'boto3',
        'click',
        'pydantic',
        'wheel'
    ]
)
