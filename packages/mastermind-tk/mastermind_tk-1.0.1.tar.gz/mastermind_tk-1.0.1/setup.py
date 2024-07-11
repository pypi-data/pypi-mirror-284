from setuptools import setup

setup(
    name='mastermind_tk',
    version='1.0.1',
    requires=["tkinter", "PIL"],
    entry_points={
        'console_scripts': [
            'mastermind=mastermind_tk:main'
        ],
    },
    include_package_data=True,
    package_data={
        '': ['resources/*']
    },
    author='Bouquet Cédric',
    author_email='cedric-bouquet-7@outlook.fr',
    description="Jeu du mastermind en version graphique",
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    python_requires='>=3.0',
)
