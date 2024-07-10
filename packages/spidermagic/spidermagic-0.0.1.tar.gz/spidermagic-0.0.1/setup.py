from setuptools import setup, find_packages

setup(
    name='spidermagic',
    version='0.0.1',
    description="爬虫需要用到的操作,后续或进行完善",
    long_description=open('README.md', encoding='utf-8').read(),
    include_package_data=True,
    author='jocre',

    author_email='2323769863@qq.com',
    maintainer='jocre',
    maintainer_email='2323769863@qq.com',
    license='MIT License',
    url='',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.9',
    install_requires=[],


)