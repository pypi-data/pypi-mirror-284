from setuptools import setup, find_packages

setup(
    name='optimnat',
    version='0.1.1',
    packages=find_packages(),   
    install_requires=[],
    author='Natalia Jarquin',
    author_email='ux21ii179@ux.edu.mx',
    description='Paquete de métodos de optimización para funciones de una variable y multivariables',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/n4tJM/optimnat_project',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)

