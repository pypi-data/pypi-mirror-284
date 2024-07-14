from setuptools import setup, find_packages

# 读取README.md文件内容
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dd_tools',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'tqdm',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'dd_tools=dd_tools.downloader:download_google_images',  # 确保这个函数存在并且没有参数
        ],
    },
    author='豬嘎嘎',
    author_email='piggaga.company@gmail.com',
    description='Download images from Google search',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/piggaga/dd-tools',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
