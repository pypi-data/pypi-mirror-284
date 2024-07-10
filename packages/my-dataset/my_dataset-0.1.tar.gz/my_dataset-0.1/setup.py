from setuptools import setup, find_packages

setup(
    name='my_dataset',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='A dataset package for multi-class image classification',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_dataset',  # 修改为你的项目地址
    author='Your Name',
    author_email='your.email@example.com',
    install_requires=[
        'tensorflow',
        'numpy',
    ],
    package_data={
        'my_dataset': ['data/*/*'],
    },
)
