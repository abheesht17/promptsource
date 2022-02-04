from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().split('\n')

setup(
    name='promptsource',
    version='0.2.0',
    url='https://github.com/bigscience-workshop/promptsource.git',
    author='Multiple Authors',
    author_email='xxx',
    python_requires='>=3.7, <3.8',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    description='An Integrated Development Environment and Repository for Natural Language Prompts.',
    packages=find_packages(),
    license="Apache Software License 2.0",
    long_description=readme,
    package_data={"": [
        "templates/*/*.yaml",
        "templates/*/*/*.yaml",
    ]}
)
