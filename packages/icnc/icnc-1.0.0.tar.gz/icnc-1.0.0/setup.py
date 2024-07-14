from setuptools import setup, find_packages

setup(
    name='icnc',  # Replace with your package name
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'icnc = icnc.main:main'  # Replace with your entry point
        ]
    },
    install_requires=[
        'python-dotenv',
        'openai==0.12.6'  # Replace with your dependencies
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
