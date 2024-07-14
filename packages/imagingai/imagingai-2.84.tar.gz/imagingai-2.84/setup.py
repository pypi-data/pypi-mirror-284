from setuptools import setup, Extension
from Cython.Build import cythonize
import os
import site

extensions = [
    Extension(
        "imagingai.ImagingAI",  # Update the module name
        ["imagingai/ImagingAI.pyx"],  # Update the filename
    )
]

cythonize_options = {
    'compiler_directives': {
        'language_level': 3,          # Use Python 3 syntax
        'emit_code_comments': False,  # Don't include comments in the generated C file
    }
}

# Define the directory where the .so files are located
so_files_dir = os.path.join('.', 'extensions')
# List all .so files in the specified directory
so_files = [os.path.join(so_files_dir, f) for f in os.listdir(so_files_dir) if f.endswith('.so')]

# Determine the site-packages directory of the current environment
site_packages_dir = site.getsitepackages()[0]

setup(
    name='imagingai',
    version='2.84',
    description='EKY Imaging AI Package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='ImagingAI',
    author_email='license@mit.edu',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
        'cryptography',
    ],
    ext_modules=cythonize(extensions, **cythonize_options),
    packages=['imagingai'],    
    include_package_data=True,
    package_data={
        'imagingai': [
            'extensions/*.so',  # Use wildcard to include all .so files in the extensions directory
        ],
    },
    data_files=[
        (site_packages_dir, so_files),  # Copy .so files to the site-packages directory
    ],
)

