from setuptools import setup, find_packages

setup(
    name='openbrush',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_packages(),
    scripts=[
        'bin/analyze_tilt.py',
        'bin/concatenate_tilt.py',
        'bin/dump_tilt.py',
        'bin/geometry_json_to_fbx.py',
        'bin/geometry_json_to_obj.py',
        'bin/normalize_sketch.py',
        'bin/tilt_to_strokes_dae.py',
        'bin/unpack_tilt.py'
    ],
    install_requires=[
        # Add your package dependencies here
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
