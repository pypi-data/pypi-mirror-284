from setuptools import setup, find_packages

setup(
    name='Streamlit_socialmedia',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4>=4.10.0',
        'requests>=2.26.0',
        'streamlit>=1.0.0'
    ],
    entry_points={
        'console_scripts': [
            'streamlit_socialmedia=streamlit_socialmedia.__main__:main'
        ]
    },
    author='Sumit Kumar Singh',
    author_email='sumitsingh9441@gmail.com',
    description='A package for generating social media icons with customizable colors and sizes.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RAJPUTRoCkStAr/Streamlit-socialmedia.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
