from setuptools import setup, find_packages

setup(
    name='InlineGPT',
    version='0.1.0',
    author='Rahul Parihar',
    author_email='rahulaauji71@gmail.com',
    description='A Python package designed to provide direct inline support for developers. It integrates GPT ('
                'Generative Pre-trained Transformer) functionality directly into Python applications, '
                'enabling developers to handle errors effectively by suggesting appropriate changes.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rahulaauji-30/InlineGPT.git',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'google-generativeai>=0.7.2',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/rahulaauji-30/InlineGPT/issues',
        'Source': 'https://github.com/rahulaauji-30/InlineGPT',
    },
)
