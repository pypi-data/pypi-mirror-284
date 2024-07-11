from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='autoscheduler',
    version='0.1.5',
    packages=find_packages(),
    test_suite='tests',
    description='A library for quantum circuit composition',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Jorge Casco Seco',
    author_email='jorgecs@unex.es',
    url='https://github.com/Qcraft-UEx/QCRAFT-AutoSchedulQ',
    project_urls={
        'Changelog': 'https://github.com/Qcraft-UEx/QCRAFT-AutoSchedulQ/blob/main/CHANGELOG.md',
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    license='MIT',
    keywords='quantum, quantum computing, quantum circuit optimization, circuit cost reduction, qiskit, braket',
    install_requires=[
        'requests>=2.32.0,<3.0.0',
        'qiskit>=1.1.0,<2.0.0',
        'amazon-braket-sdk>=1.80.0,<2.0.0',
        'qiskit-ibm-runtime>=0.23.0,<1.0.0',
        'qiskit-aer>=0.14.2,<1.0.0',
        'antlr4-python3-runtime==4.9.2'
    ],
    extras_require={
        'dev': [
            'pytest'
        ]
    },
    python_requires='>=3.9'
)
