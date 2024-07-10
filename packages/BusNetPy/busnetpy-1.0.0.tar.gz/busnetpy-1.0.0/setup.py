from setuptools import setup, find_packages

setup(
    name='BusNetPy',
    version='1.0.0',
    packages=find_packages(),  # 自动寻找项目中的所有包
    author='jinyangLi',
    author_email='1045186183@qq.com',
    description='busplanner',
    license='MIT',
    package_data={'': ['*.pyc']},
    exclude_package_data={'': ['*.py']},
    install_requires=[
        'pandas>=2.0.3',  # 指定依赖的包及其版本要求
        'geopandas>=0.13.2',
        'shapely>=2.0.2',
        'requests>=2.31.0',
        'contextily>=1.5.2',
        'matplotlib>=3.7.4',
        'osmnx>=1.9.1',
        'urllib3>=1.26.18',
        'xlwt>=1.3.0',
        'tqdm>=4.66.1',
        'fuzzywuzzy>=0.18.0',
        'bs4>=0.0.2',
        'pypinyin>=0.49.0',
        'networkx>=3.1'

    ],

)
