import sys
import re
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

PY_VER = sys.version_info
if PY_VER < (3, 6):
    raise RuntimeError("asynceth doesn't support Python version prior 3.6")

install_requires = [
    'regex',
    'ethereum',
    'eth_abi>=2.0.0-alpha.2'
]
dependency_links = [
    'git+https://github.com/tristan/eth-abi.git@93c521195424d764f22ccf00dcf4227fda4259a9#egg=eth_abi-2.0.0-alpha.2'
]

tests_require = [
    'pytest',
    'aiohttp',
    'pytest-aiohttp',
    'testing.parity'
]

def read_version():
    regexp = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")
    init_py = os.path.join(os.path.dirname(__file__),
                           'asynceth', '__init__.py')
    with open(init_py) as f:
        for line in f:
            match = regexp.match(line)
            if match is not None:
                return match.group(1)
        else:
            raise RuntimeError('Cannot find version in asynceth/__init__.py')

setup(
    name='asynceth',
    version=read_version(),
    description='Asyncio Ethereum Utilities',
    long_description=open('README.md').read(),
    author='Tristan King',
    author_email='mail@tristan.sh',
    url='https://github.com/tristan/asynceth',
    packages=['asynceth'],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=install_requires,
    include_package_data=True,
    tests_require=tests_require,
    setup_requires=['pytest-runner'],
    dependency_links=dependency_links,
)
