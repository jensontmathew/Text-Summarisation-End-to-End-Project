import setuptools

with open('README.md', 'r',encoding='utf-8') as f:
    long_description = f.read()


__version__ = '0.0.0'

REPO_NAME = 'Text-Summarisation-End-to-End-Project'
AUTHOR_NAME = 'jensontmathew'
SRC_REPO = 'textSummarizer'  #source repository name
AUTHOR_EMAIL = 'jensontmathew3@gmail.com'


setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description='A Python package for text summarization',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jensontmathew/Text-Summarization-End-to-End-Project',
    project_urls={
        'Bug Tracker': 'https://github.com/jensontmathew/Text-Summarization-End-to-End-Project/issues',
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)