import toml
from setuptools import setup, find_packages

def get_dependencies_from_pipfile(pipfile_path='Pipfile'):
    pipfile = toml.load(pipfile_path)
    dependencies = pipfile.get('packages', {})
    formatted_dependencies = []

    for package, version in dependencies.items():
        if version == "*":
            formatted_dependencies.append(package)
        else:
            formatted_dependencies.append(f"{package}{version}")

    return formatted_dependencies

install_requires = get_dependencies_from_pipfile()

setup(
    name='pycoretoolkit',
    version='0.0.1',
    packages=find_packages(),
    install_requires=install_requires,
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'bandit',
            'safety',
            'ruff',
            'black',
        ],
    },
    entry_points={
        'console_scripts': [
            'pycoretoolkit=pycoretoolkit.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
