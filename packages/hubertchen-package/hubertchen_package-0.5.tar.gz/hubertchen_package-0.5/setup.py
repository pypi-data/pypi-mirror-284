from setuptools import setup, find_packages

setup(
    name='hubertchen_package',
    version='0.5',
    packages=find_packages(),
    install_requires=[],  # Add any dependencies here
    url='https://github.com/hubertchen200/mypy-package',
    license='MIT',
    author='Hubert Chen',
    author_email='hubertchen200@gmail.com',
    description='Hubert Chen''s Python package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)