# Open Brush Python Tools

A collection of Python scripts to allow you to interact with [Open Brush](https://openbrush.app/) files and data

This code was previously part of the Tilt Brush Toolkit and was originally written by Google.

## Setup

### Local clone / development
```bash
git clone ...
pip install -e .
```

### PyPI package

```bash
pip install openbrush
```

## Contents

### Command Line Tools

Python 3.9 code and scripts for advanced Open Brush data manipulation.

 * `bin` - command-line tools
   * `dump_tilt.py` - Sample code that uses the openbrush.tilt module to view raw Open Brush data.
   * `geometry_json_to_fbx.py` - Sample code that shows how to postprocess the raw per-stroke geometry in various ways that might be needed for more-sophisticated workflows involving DCC tools and raytracers. This variant packages the result as a .fbx file.
   * `geometry_json_to_obj.py` - Sample code that shows how to postprocess the raw per-stroke geometry in various ways that might be needed for more-sophisticated workflows involving DCC tools and raytracers. This variant packages the result as a .obj file.
   * `tilt_to_strokes_dae.py` - Converts .tilt files to a Collada .dae containing spline data.
   * `unpack_tilt.py` - Converts .tilt files from packed format (zip) to unpacked format (directory) and vice versa, optionally applying compression.
 * `Python` - Put this in your `PYTHONPATH`
   * `openbrush` - Python package for manipulating Open Brush data.
     * `export.py` - Parse the legacy .json export format. This format contains the raw per-stroke geometry in a form intended to be easy to postprocess.
     * `tilt.py` - Read and write .tilt files. This format contains no geometry, but does contain timestamps, pressure, controller position and orientation, metadata, and so on -- everything Open Brush needs to regenerate the geometry.
     * `unpack.py` - Convert .tilt files from packed format to unpacked format and vice versa.
