from setuptools import setup, find_packages

setup(
    name='solveur',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'math'
    ],
    entry_points={
        'console_scripts': [
            # Exemple de point d'entrée de script
            # 'my-command=my_package.module:main_function',
        ],
    },
    author='Bouquet Cédric',
    author_email='cedric-bouquet-7@outlook.fr',
    description="Solveur d'équations de second degré",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.0',
)
