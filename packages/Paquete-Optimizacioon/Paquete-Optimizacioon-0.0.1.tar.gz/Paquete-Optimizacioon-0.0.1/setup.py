from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Proyecto Final: Paquete de optimizacion'
LONG_DESCRIPTION = 'Paquete que incluye todos los algoritmos vistos en la materia de optimizacion'

# Configurando
setup(
       # el nombre debe coincidir con el nombre de la carpeta 	  
       #'modulomuysimple'
        name="Paquete-Optimizacioon", 
        version=VERSION,
        author="Norma Jimenez",
        author_email="<ux21ii004@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # añade cualquier paquete adicional que debe ser
        #instalado junto con tu paquete. Ej: 'caer'
        
        keywords=['python', 'paquete optimizacion', 'proyecto final'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)