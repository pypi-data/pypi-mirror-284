from setuptools import setup, find_packages

setup(
    name='pypercorn',
    version='1.3.2',
    author='Ratabart666',
    author_email='hypercorncordoba@gmail.com',
    description='This is a wrapper for HyperCornAPI, developed by HyperCorn. It serves as a foundational API designed for seamless integration with HyperCorn, an advanced application specializing in crop classification.',
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    packages=["pypercorn",
              "pypercorn.algorithms", "pypercorn.algorithms.images"],
    keywords=['IMAGES', 'SPECTRUMS', 'CROPS', 'SENTINEL'],
    exclude=['tests'],
    install_requires=[
        'requests',
        'numpy',
        'msgpack_numpy'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
