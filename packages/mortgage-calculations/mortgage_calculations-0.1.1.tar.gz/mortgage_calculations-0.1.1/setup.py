from setuptools import setup, find_packages

setup(
    name='mortgage_calculations',
    version='0.1.1',
    packages=find_packages(),
    description='A mortgage calculator for repayment periods and initial deposit calculations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Viktor Naumenkov',
    author_email='viktornaumenkov6@gmail.com',
    url='https://github.com/hornetexxon/mortgage_calculations',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
