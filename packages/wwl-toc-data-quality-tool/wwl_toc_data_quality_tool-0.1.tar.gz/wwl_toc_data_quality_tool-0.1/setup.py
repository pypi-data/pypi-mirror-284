from setuptools import setup, find_packages

setup(
    name='data_quality_tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'quality_check=data_quality_tool.__main__:main',
        ],
    },
    author='Xifan.Z',
    author_email='xifanzou42@gmail.com',
    description='A tool to check data quality against predefined standards.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xifanzou/data_quality_check',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
