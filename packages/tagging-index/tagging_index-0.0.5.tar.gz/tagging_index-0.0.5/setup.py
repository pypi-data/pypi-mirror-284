import os
from setuptools import setup, find_namespace_packages

name = "tagging_index"
description = "content tagging and index generator with maxcompute"
url = "https://github.com/Digital-Transformation-Research-Center/tagging-index"  # 项目网址
# # 依赖包列表
install_requires = [
    "treelib>=1.7.0",
    "data2cloud>=0.0.2",
]

author = "t2wei"  # 作者名
author_email = "t2wei@me.com"  # 作者邮箱

# git action workflow yml文件中定义的版本号,来自于tag
version = os.getenv("PACKAGE_VERSION")
version = version if version else "0.0.1-dev"
# 自动发现所有包
packages = find_namespace_packages(".", include=[name + "*"], exclude=["*schemas*"])
print(f"packages:{packages}")
if not version:
    raise Exception("no version info found!")
print(f"version: {version};")
setup(
    name=name,  # 包的名称，应与项目目录名一致，且符合PyPI的要求
    version=version,  # 版本号
    author=author,
    author_email=author_email,
    description=description,
    long_description=open("README.md").read(),  # 详细描述，通常从README文件读取
    long_description_content_type="text/markdown",  # 如果README是Markdown格式
    url=url,
    packages=packages,
    include_package_data=True,
    classifiers=[  # 分类信息，帮助用户在PyPI上找到你的包
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    python_requires=">=3.7",  # 指定Python版本要求
)
