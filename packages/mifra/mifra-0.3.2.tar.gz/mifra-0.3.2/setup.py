"""
rm -rf dist && python3 setup.py sdist && python -m twine upload --repository pypi dist/*

"""
import setuptools



# Si tienes un README
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mifra',  # nombre del paquete
    version='0.3.2', # versión
    license='MIT',
    py_modules=['exodo', 'log', 'raw', 'master'],  # módulos individuales en lugar de scripts
    author="Felipe Leiva", # autor
    author_email="anexatec@gmail.com", # email
    description="Un package para hacer migraciones", # Breve descripción
    long_description=long_description,
    long_description_content_type="text/markdown", # Incluir el README.md si lo has creado
    url="https://github.com/felipeals256/mifra", # URL donde se encuentra tu paquete en Github
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "numpy>=1.23.4",
        "openpyxl>=3.0.1",
        "psycopg2-binary>=2.9.4",
        "pymssql>=2.2.5",
        "pandas>=1.5.1"
    ],
) # aquí añadimos información sobre el lenguaje usado, el tipo de licencia, etc.
