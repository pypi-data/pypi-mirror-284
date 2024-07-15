from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Proyecto Optimizacion: Paquete de optimizacion'
LONG_DESCRIPTION = 'Paquete de todos los algoritmos que hicimos a lo largo del semestre'
# Configurando
setup(
       # el nombre debe coincidir con el nombre de la carpeta 	  
       #'modulomuysimple'
        name="PaqueteOpt", 
        version=VERSION,
        author="Mario Zepeda",
        author_email="<ux21ii039@ux.edu.mx>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # añade cualquier paquete adicional que debe ser
        #instalado junto con tu paquete. Ej: 'caer'
        
        keywords=['python', 'primer paquete', 'PaqueteOptimizacion'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)