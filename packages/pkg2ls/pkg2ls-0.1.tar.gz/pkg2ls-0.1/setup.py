from setuptools import setup, find_packages

setup(
    name='pkg2ls',
    version='0.1',
    packages=find_packages(),
    scripts=['pkg2ls.py'],
    install_requires=[
        # List your dependencies here if any
    ],
    author='Jianfengliu0413',
    author_email='Jianfeng.Liu0413@gmail.com',
    description='pkg managements',
    url='https://github.com/yourusername/pkg2ls',  # Link to your package's repository
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
