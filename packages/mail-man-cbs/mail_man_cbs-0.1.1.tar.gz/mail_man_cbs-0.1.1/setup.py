from setuptools import find_packages, setup

def read_requirements():
    requirements = []
    with open('requirements.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                requirements.append(line)
    return requirements

setup(
    name="mail_man_cbs",
    packages=find_packages(include=["mail"]),
    version="0.1.1",
    description="First mailman example",
    author="Cabysis",
    install_requires=read_requirements(),
    setup_requires=["setuptools","pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)
