from setuptools import setup, find_packages

setup(
    name='retail_insights',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'requests>=2.25.0',
        'numpy>=1.21.0'
    ],
    entry_points={
        'console_scripts': [
            'retail_insights=retail_insights.app:app',
        ],
    },
)