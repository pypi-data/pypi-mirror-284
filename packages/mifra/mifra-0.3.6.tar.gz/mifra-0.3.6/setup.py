#rm -rf mifra.egg-info && rm -rf dist && python3 setup.py sdist
#python -m twine upload --repository pypi dist/*

import setuptools

#Si tienes un readme
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='mifra',  #nombre del paquete
    version='0.3.6', #versión
    license='MIT',
    packages=setuptools.find_packages(where='src'),  # Asegúrate de que el argumento 'where' esté correcto según tu estructura
    package_dir={'': 'src'},  # Esto dice que el código fuente está en el directorio 'src'
    scripts=['src/exodo.py', 'src/log.py', 'src/raw.py', 'src/master.py'],  # Ajusta las rutas si es necesario
    author="Felipe Leiva", #autor
    author_email="anexatec@gmail.com", #email
    description="Un package hacer migraciones", #Breve descripción
    long_description=long_description,
    long_description_content_type="text/markdown", #Incluir el README.md si lo has creado
    url="https://github.com/felipeals256/mifra", #url donde se encuentra tu paquete en Github
 )