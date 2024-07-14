from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import site
from setuptools.command.install import install
import os
import shutil

class CustomInstallCommand(install):
    """Customized setuptools install command - runs a post-install script."""
    def run(self):
        install.run(self)
        self.run_post_install()

    def run_post_install(self):
        # Run the post-install script
        os.system('python post_install.py')

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
site_packages_dir = os.path.join('.', 'extensions')

setup(
    name='imagingai',
    version='2.92',
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
    packages=find_packages(),    
    include_package_data=True,
    package_data={
        'imagingai': [
            'extensions/*.so',  # Use wildcard to include all .so files in the extensions directory
        ],
    },
    data_files=[
        (site_packages_dir, so_files),  # Copy .so files to the site-packages directory
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
)
