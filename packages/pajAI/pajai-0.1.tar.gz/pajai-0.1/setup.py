from setuptools import setup, find_packages

setup(
    name="pajAI",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "googleads",
    ],
    entry_points={
        'console_scripts': [
            'pajai=pajAI.ad_manager:main',
        ],
    },
    author="Pavle Bradic",
    author_email="your_email@example.com",
    description="A package for managing Google Ad Manager tasks.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/pajAI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
