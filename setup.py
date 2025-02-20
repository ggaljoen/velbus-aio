from setuptools import setup

setup(
    name="velbus-aio",
    version="2021.7",
    url="https://github.com/ggaljoen/velbus-aio",
    license="MIT",
    author="Maikel Punie",
    install_requires=["asyncio", "pyserial-asyncio"],
    author_email="maikel.punie@gmail.com",
    packages=["velbusaio"],
    platforms="any",
)
