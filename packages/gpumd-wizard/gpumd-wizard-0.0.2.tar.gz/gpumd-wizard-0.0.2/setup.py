import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()
    
setuptools.setup(
    name = "gpumd-wizard",
    version = "0.0.2",
    author = "Jiahui Liu",
    author_email="jiahui.liu.willow@gmail.com",
    description="Material structure processing software ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jonsnow-willow/GPUMD-Wizard",                                         
    packages=setuptools.find_packages(),     
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=['ase',
                      'phonopy',
                      'calorine'],
    )

