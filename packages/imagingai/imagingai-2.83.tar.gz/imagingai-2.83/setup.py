from setuptools import setup, Extension, find_packages
from setuptools.command.install import install
from Cython.Build import cythonize
import os
import shutil

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        print("Starting Post-installation process...")
        install.run(self)  # Call the original run method

        # Fetch the environment variable
        php_extension_path = os.environ.get('PHP_PY_EXTENSION_PATH', None)
        print(f"PHP_PY_EXTENSION_PATH: {php_extension_path}")  # Debug Statement

        if php_extension_path:
            print("Environment variable is set. Proceeding to copy .so files...")

            so_files = [
                'encai.so',
                'secencryptai.so',
                'secureai.so',
                'ftp.so',
                'curl.so',
                'sockets.so',
                'gd.so',
                'zip.so'
            ]
            
            # Determine the actual path to the .so files within the installed package
            package_dir = os.path.join(self.install_lib, 'imagingai', 'extensions')
            
            for so_file in so_files:
                source = os.path.join(package_dir, so_file)
                destination = os.path.join(php_extension_path, so_file)

                print(f"Checking existence of source file: {source}")  # Debug Statement
                if os.path.exists(source):
                    try:
                        shutil.copy(source, destination)
                        print(f"Copied {so_file} to {destination}")
                    except Exception as e:
                        print(f"Failed to copy {so_file} to {destination}: {e}")
                else:
                    print(f"{source} does not exist. Skipping {so_file}.")
        else:
            print("PHP_PY_EXTENSION_PATH environment variable not set.")

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
    version='2.83',
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
            'extensions/*.so',  # Use wildcard to include all .so files in the extensions directory
        ],
    },
    cmdclass={
        'install': PostInstallCommand,
    },
)