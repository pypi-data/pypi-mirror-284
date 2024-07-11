from setuptools import find_packages, setup
import os

# Función para leer el archivo requirements.txt
def read_requirements():
    requirements = []
    with open('requirements.txt', 'r') as f:
        for line in f:
            # Elimina espacios y comentarios
            line = line.strip()
            if line and not line.startswith('#'):
                requirements.append(line)
    return requirements

setup(
    name="mail_man_cbs_0.1",
    packages=find_packages(include=["mail"]),
    version="0.1.0",
    description="First mailman example",
    author="Cabysis",
    install_requires=[
        "requests==2.32.3",
    ],
    setup_requires=["setuptools","pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)
