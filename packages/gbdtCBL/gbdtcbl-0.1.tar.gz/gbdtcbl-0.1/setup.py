from setuptools import setup, find_packages

setup(
    name='gbdtCBL',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-learn',
    ],
    author='Jiaqi Luo, Yuan Yuan, Shixin Xu',
    author_email='jiaqi.luo.jqluo@outlook.com',
    description='A package containing class-balanced loss functions for gradient boosting decision tree',
    url='https://github.com/Luojiaqimath/ClassbalancedLoss4GBDT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9,<3.12',
)

