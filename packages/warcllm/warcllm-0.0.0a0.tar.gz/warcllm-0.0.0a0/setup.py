import os

from setuptools import setup

from warcllm import __version__


def get_long_description():
    with open(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
            encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="warcllm",
    description=__version__.__description__,
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Florents Tselai",
    url="https://github.com/Florents-Tselai/warcllm",
    entry_points="""
        [console_scripts]
        warcllm=warcllm.cli:cli
    """,
    project_urls={
        "Issues": "https://github.com/Florents-Tselai/warcllm/issues",
        "CI": "https://github.com/Florents-Tselai/warcllm/actions",
        "Changelog": "https://github.com/Florents-Tselai/warcllm/releases",
    },
    license="BSD License",
    version=__version__.__version__,
    packages=["warcllm"],
    install_requires=["llm", "click", "setuptools", "pip", "warcdb"],
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
            "black",
            "ruff",
        ]
    },
    python_requires=">=3.11",
)
