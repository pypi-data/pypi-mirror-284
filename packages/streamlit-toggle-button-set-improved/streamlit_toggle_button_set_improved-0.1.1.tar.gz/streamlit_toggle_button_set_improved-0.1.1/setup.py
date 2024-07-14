import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit-toggle-button-set-improved",
    version="0.1.1",  # 增加版本號
    author="BensonBS",
    author_email="benson.bs.sung@gmail.com",
    description="A Streamlit component for toggle button sets (Fork)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bensonbs/streamlit-toggle-button-set",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "streamlit >= 0.63",
    ],
)