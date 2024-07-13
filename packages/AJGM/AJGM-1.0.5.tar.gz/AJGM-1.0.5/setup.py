import setuptools
with open('README.md','r',encoding='utf-8') as fh:
    long_description=fh.read()

setuptools.setup(
    name='AJGM',
    version='1.0.5',
    author='stevenyang',
    author_email='yangsq@hnu.edu.cn',
    description='.',
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=['pandas','numpy','scipy','scikit-learn'],
    license='MIT'   
)