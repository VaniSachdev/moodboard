from setuptools import setup, find_packages

requires = [
    'flask',
    'spotipy',
    'pathlib',
    'pandas'
]

setup(
    name='moodboard',
    author='vani sachdev',
    author_email='vsachdev@g.hmc.edu',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)