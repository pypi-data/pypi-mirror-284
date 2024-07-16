from setuptools import dist, setup, Extension
import glob

sfc_module = Extension(
    name="GIMMESolver",
    include_dirs=['solverModules/GIMME_solver_modules'],
    sources=glob.glob('solverModules/GIMME_solver_modules/*.cpp'),
    language='c++',
)

with open('README.md', 'r') as file:
    readmeFile = file.read()

setup(
    name="GIMMECore",
    version="2.0.0",
    license="CC BY 4.0",
    python_requires='>=3.12',
    author="Samuel Gomes",
    author_email="samuel.gomes@tecnico.ulisboa.pt",
    description="A research package that "
                "applies preference-driven group management (division of a collective in work groups and attribution "
                "of tasks) so that collective ability improves.",
    long_description=readmeFile,
    long_description_content_type="text/markdown",
    url='https://github.com/SamGomes/GIMME',
    packages=['GIMMECore', 'GIMMECore.ModelBridge', 'GIMMECore.AlgDefStructs'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    install_requires=[
        'python-decouple>=3.0',
        'deap>=1.3.3',
        'pandas>=1.3.5',
        'scikit-learn>=1.0.2',
        'matplotlib>=3.5.3',
        'pymongo>=4.3.3'
    ],
    ext_modules=[sfc_module]
)
