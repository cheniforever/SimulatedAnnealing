from setuptools import setup, find_packages

setup(
    name = "simulated_annealing",
    packages = find_packages(),
    version = "0.1.8",
    author='Skyler Grammer, Andrew Nystrom',
    author_email="skylergrammer@gmail.com, awnystrom@gmail.com",
    description = "A Simulated Annealing implimentation with a scikit-learn style API backed by joblib for speed.",
    url = "https://github.com/cheniforever/SimulatedAnnealing",
    keywords = ["simulated", "annealing", "parameter", "hyperparameter", "optimization", "optimisation", "model", "selection"],
    license = "Apache 2.0",
    install_requires = ['scikit-learn>=0.16.0', 'numpy>=1.9.0'],
    dependency_links=['https://github.com/cheniforever/SimulatedAnnealing.git'],
    classifiers = ["Programming Language :: Python",
    			   "Programming Language :: Python :: 2.7",
    			   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.4",
    			   "License :: OSI Approved :: Apache Software License",
    			   "Operating System :: OS Independent",
    			   "Development Status :: 4 - Beta",
    			   "Intended Audience :: Developers"
    			   ]
	)
