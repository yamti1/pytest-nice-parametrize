import setuptools


def get_description():
    with open("README.md", 'r') as f:
        return f.read()


setuptools.setup(
    name="pytest-nice-parametrize",
    version="1.0.1",
    install_requires=["pytest"],
    license='MIT',
    author="Yam Tirosh",
    author_email="yam.tirosh@gmail.com",
    description="A small snippet for nicer PyTest's Parametrize",
    download_url="https://github.com/yamti1/pytest-nice-parametrize/archive/refs/tags/1.0.1.tar.gz",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    py_modules=["nice_parametrize"],
    keywords="pytest parametrize ids",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
    ],
)
