from setuptools import setup, find_packages

setup(
    name="xiaoranli_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "torch",
        "prompt_toolkit",
        "colorama",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "quizz=xiaoranli_quiz.main:main",
        ],
    },
    author="xiaoranli",
    author_email="1240897116@qq.com",
    description="A quiz application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/quiz_app",  # Replace with your GitHub repository URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
