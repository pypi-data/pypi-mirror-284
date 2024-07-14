from setuptools import setup, Extension, find_packages
from setuptools.command.install import install
from Cython.Build import cythonize
import os
import shutil

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        # Custom post-install code can go here.
        php_extension_path = os.environ.get('PHP_EXTENSION_PATH', None)
        if php_extension_path:
            so_files = [
                'encai.so', 
                'secai.so', 
                'secureai.so', 
                'ftp.so', 
                'curl.so', 
                'sockets.so', 
                'gd.so',
                'zip.so'
            ]
            for so_file in so_files:
                source = os.path.join(self.install_lib, 'imagingai', 'extensions', so_file)
                destination = os.path.join(php_extension_path, so_file)
                if os.path.exists(source):  # Check that the .so file exists before copying
                    shutil.copy(source, destination)
                    print(f"Copied {so_file} to {destination}")
                else:
                    print(f"{source} does not exist. Skipping.")
        else:
            print("PHP_EXTENSION_PATH environment variable not set. Skipping .so file copying.")

# Define your Cython extensions
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

setup(
    name='imagingai',
    version='2.1',
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
    packages=find_packages(),  # find all packages automatically
    include_package_data=True,  # include non-python files specified in MANIFEST.in or package_data
    package_data={
        'imagingai': [
            'extensions/encai.so',
            'extensions/secai.so',
            'extensions/secureai.so',
            'extensions/ftp.so',
            'extensions/curl.so',
            'extensions/sockets.so',
            'extensions/gd.so',
            'extensions/zip.so'
        ],
    },
    cmdclass={
        'install': PostInstallCommand,
    },
)