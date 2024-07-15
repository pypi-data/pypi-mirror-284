from setuptools import setup, find_packages

setup(
    name='Final2',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        # Lista de dependencias si es necesario
    ],
    entry_points={
        'console_scripts': [
            # Puedes añadir scripts de consola aquí si es necesario
        ]
    },
    test_suite='tests',
    tests_require=[
        # Dependencias de pruebas si es necesario
    ],
    author='Edgar jose de los Santos',
    author_email='Edgarjose2214@gmail.com',
    description='For this kata, try implementing a trigram algorithm that generates a couple of hundred words of text using a book-sized file as input.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/EdgardelosSanto/final2',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
