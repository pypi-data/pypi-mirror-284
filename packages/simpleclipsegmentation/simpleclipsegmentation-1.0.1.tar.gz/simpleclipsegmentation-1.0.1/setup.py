from setuptools import setup, find_packages

VERSION = '1.0.1' 
DESCRIPTION = 'Semantic segmentation with CLIP'
LONG_DESCRIPTION = 'A lightweight package for semantic image segmentation with CLIP.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="simpleclipsegmentation", 
        version=VERSION,
        author="Sven Pfiffner",
        author_email="sven.pfiffner@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            'torch',
            'numpy',
            'Pillow',
            'opencv-python',
            'transformers',
        ], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'CLIP', 'semantic segmentation', 'segmentation', 'image segmentation', 'computer vision', 'deep learning', 'transformers'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent"
        ]
)