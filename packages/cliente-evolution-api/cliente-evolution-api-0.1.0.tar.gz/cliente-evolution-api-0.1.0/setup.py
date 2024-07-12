from setuptools import setup, find_packages

NAME = "Evolution API Client"
REPO_ID = "evolution-api-client"
VERSION = "0.1.0"
PYTHON_REQUIRES = ">=3.9"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name='cliente-evolution-api',
    version=VERSION,    
    packages=find_packages(exclude=["test", "tests"]),
    install_requires=REQUIRES,
    python_requires=PYTHON_REQUIRES,    
    author='Flávio Coutinho',
    author_email='coutinho.fg@gmail.com',
    description='Biblioteca Python para cliente da EvolutionAPI',
    url='https://github.com/FlavioCoutinhoGO/evolution-api-client',
    keywords=["Evolution API", NAME, REPO_ID],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    package_data={"evolution_api_client": ["py.typed"]},
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 3 - Alpha',        
        'Intended Audience :: Developers',
    ],    
)