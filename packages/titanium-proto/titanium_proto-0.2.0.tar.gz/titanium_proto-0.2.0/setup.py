from setuptools import setup, find_packages

setup(
    name="titanium-proto",
    version="0.2.0",
    description="A Python library to generate C++ classes from JSON for working with structs.",
    author="Lucas D. Franchi",
    author_email="LucasD.Franchi@gmail.com",
    packages=find_packages(),  # Automatically find all packages under the current directory
    package_data={
        'titanium_proto': ['templates/*.jinja2'],  # Corrected path to include templates
    },
    include_package_data=True,  # Ensure package_data is included in the distribution
    python_requires=">=3.7",  # Specify the minimum Python version required
    entry_points={
        'console_scripts': [
            'titanium-proto = titanium_proto.titanium_proto:main',  # Command line entry point
        ],
    },
    extras_require={
        "dev": [  # Define development dependencies
            "pytest >= 6.2.4",
            "pytest-cov >= 2.12.1",
            "coverage >= 5.5",
        ]
    },
    classifiers=[  # Metadata about your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
