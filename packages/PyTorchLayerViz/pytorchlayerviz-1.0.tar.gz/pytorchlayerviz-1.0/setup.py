from setuptools import setup, find_packages

VERSION = '1.0'
DESCRIPTION = "PyTorchLayerViz is a Python library that allows you to visualize the weights and feature maps of a PyTorch model."
LONG_DESCRIPTION = """\
PyTorchLayerViz is a Python library designed to assist developers and researchers in visualizing 
the weights and feature maps of PyTorch models. This tool provides easy-to-use functions to help 
understand and interpret deep learning models, making it an essential utility for anyone working 
with PyTorch.
"""

setup(
    name="PyTorchLayerViz",
    version=VERSION,
    author="Simone Panico",
    author_email="simone.panico@icloud.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['torch', 'torchvision', 'pillow', 'matplotlib'],
    keywords=['python', 'pytorch', 'deep learning', 'model'],
)