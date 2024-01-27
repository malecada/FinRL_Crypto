from setuptools import find_packages
from setuptools import setup

REQUIRES = []
try:
    with open("requirements.txt", "rb") as f:
        REQUIRES = [line.strip() for line in f.read().decode("utf-8").split("\n")]
        REQUIRES = [line for line in REQUIRES if "#" not in line]
except FileNotFoundError as myEx:
    raise Exception(myEx)

setup(
    name="finrl-crypto",
    version="0.0.1",
    author="Xiao-Yang Liu, Ming Zhu, Jingyang Rui, Hongyang Yang",
    author_email="hy2500@columbia.edu",
    url="https://github.com/malecada/FinRL_Crypto.git",
    license="MIT",
    install_requires=REQUIRES,
    description="FinRL­-Meta: A Universe of ­ Market En­vironments for Data­-Driven Financial Reinforcement Learning",
    packages=find_packages(),
    long_description="FinRL­-Meta: A Universe of Near Real­ Market En­vironments for Data­-Driven Financial Reinforcement Learning",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    keywords="Reinforcment Learning",
    platform=["any"],
    python_requires=">=3.6",
)