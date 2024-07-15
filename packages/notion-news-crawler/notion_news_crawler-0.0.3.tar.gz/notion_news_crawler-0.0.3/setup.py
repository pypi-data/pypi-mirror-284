from setuptools import setup, find_packages
import os

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()

setup(
    name='notion-news-crawler',
    version='0.0.3',
    url='https://github.com/kar7mp5/Notion-News-Crawler.git',
    author='MinSup Kim',
    author_email='tommy1005a@gmail.com',
    description='Notion news mecro',
    packages=find_packages(),
    long_description=read_file('README.md'),
    install_requires=['python-dotenv', 'tqdm', 'selenium', 'pytz', 'requests', 'retrying'],
)