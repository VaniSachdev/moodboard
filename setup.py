from setuptools import setup, find_packages

requires = [
    'requests',
    'spotipy',
    'pathlib',
    'pandas',
    'time',
    'gspread',
    'os'
    'numpy'
    'seaborn'
    'matplotlib.pyplot'
]


setup(
    name='moodboard',
    version='2.0',
    author='vani sachdev',
    author_email='vsachdev@g.hmc.edu',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)