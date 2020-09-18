import setuptools


def get_requirements():
    with open("requirements.txt", "r") as f:
        return list(f)


def get_description():
    with open("README.md", 'r') as f:
        return f.read()


setuptools.setup(
    name="pytest-nice-parametrize",
    version="1.0.0",
    author="Yam Tirosh",
    author_email="yam.tirosh@gmail.com",
    description="A small snippet for nicer PyTest's Parametrize",
    long_description=get_description(),
    py_modules=["nice_parametrize"],
    install_requires=get_requirements(),
    keywords="pytest parametrize ids",
    classifiers=["Operating System :: OS Independent"],
)
