from setuptools import setup

setup(
    name='day_date',
    version='0.1.0',
    entry_points={
        'console_scripts': [
            # Exemple de point d'entrée de script
            # 'my-command=my_package.module:main_function',
        ],
    },
    author='Bouquet Cédric',
    author_email='cedric-bouquet-7@outlook.fr',
    description="Calcule le jour de la semaine d'une date donnée",
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.0',
)
