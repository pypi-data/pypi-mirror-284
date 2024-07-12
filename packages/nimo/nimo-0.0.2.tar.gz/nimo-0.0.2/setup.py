from setuptools import setup, find_packages

setup(
    name="nimo",
    version="0.0.2",
    author="NIMO developers",
    license="MIT",
    description='NIMO package',
    #packages=find_packages(where='nimsos'),
    #package_dir={'': 'nimsos'},
    packages=["nimo", "nimo.ai_tools", "nimo.input_tools", "nimo.output_tools", "nimo.visualization"],
    install_requires=[
        "Cython",
        "matplotlib",
        "numpy",
        "physbo>=2.0.0",
        "scikit-learn",
        "scipy"
    ]
)
