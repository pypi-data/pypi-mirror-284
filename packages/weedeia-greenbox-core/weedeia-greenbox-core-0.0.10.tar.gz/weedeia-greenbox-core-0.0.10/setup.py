import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weedeia-greenbox-core",
    version="0.0.10",
    author="Paulo Porto",
    description="API for GPIO admnistration",
    packages=setuptools.find_packages(),
    include_package_data=True,
    py_modules=['src'],
    entry_points={
      "console_scripts": [
          "weedeia-greenbox-core=src.main:main",
      ],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[
        'wheel',
        'fastapi',
        'uvicorn',
        'rpi.gpio'
    ]
)