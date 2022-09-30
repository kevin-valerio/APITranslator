from setuptools import find_packages, setup
setup(
    name='ApiTranslatorLib',
    packages=find_packages(include=['APITranslator']),
    version='0.1.0',
    description='A library to translate text from different modules.',
    author='Thomas SOUTIF',
    license='public',
    install_requires=["deepl","python-dotenv"],
    test_suites='tests'
)