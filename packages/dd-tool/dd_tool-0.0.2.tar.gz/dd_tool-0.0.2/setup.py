from setuptools import setup, find_packages

# 读取README.md文件内容
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dd-tool',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
        'tqdm',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'dd-tool = dd_tool.downloader:download_google_images',
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
