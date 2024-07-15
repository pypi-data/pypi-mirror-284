#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This is sample Python 2.7 code that uses the openbrush.tilt module
to view raw Tilt Brush data."""

import os
import pprint
import sys

try:
    sys.path.append(os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), 'Python'))
    from openbrush.tilt import Tilt
except ImportError:
    print("Please put the 'Python' directory in your PYTHONPATH", file=sys.stderr)
    sys.exit(1)


def dump_sketch(sketch):
    """Prints out some rough information about the strokes.
    Pass a openbrush.tilt.Sketch instance."""
    cooky, version, unused = sketch.header[0:3]
    print('Cooky:0x%08x  Version:%s  Unused:%s  Extra:(%d bytes)' % (
        cooky, version, unused, len(sketch.additional_header)))

    # Create dicts that are the union of all the stroke-extension and
    # control-point-extension # lookup tables.
    union_stroke_extension = {}
    union_cp_extension = {}
    for stroke in sketch.strokes:
        union_stroke_extension.update(stroke.stroke_ext_lookup)
        union_cp_extension.update(stroke.cp_ext_lookup)

    print("Stroke Ext: %s" % ', '.join(list(union_stroke_extension.keys())))
    print("CPoint Ext: %s" % ', '.join(list(union_cp_extension.keys())))

    for (i, stroke) in enumerate(sketch.strokes):
        print("%3d: " % i, end=' ')
        dump_stroke(stroke)


def dump_stroke(stroke):
    """Prints out some information about the stroke."""
    if len(stroke.controlpoints) and 'timestamp' in stroke.cp_ext_lookup:
        cp = stroke.controlpoints[0]
        timestamp = stroke.cp_ext_lookup['timestamp']
        start_ts = ' t:%6.1f' % (cp.extension[timestamp] * .001)
    else:
        start_ts = ''

    try:
        scale = stroke.extension[stroke.stroke_ext_lookup['scale']]
    except KeyError:
        scale = 1

    if 'group' in stroke.stroke_ext_lookup:
        group = stroke.extension[stroke.stroke_ext_lookup['group']]
    else:
        group = '--'

    if 'seed' in stroke.stroke_ext_lookup:
        seed = '%08x' % stroke.extension[stroke.stroke_ext_lookup['seed']]
    else:
        seed = '-none-'

    print("B:%2d  S:%.3f  C:#%02X%02X%02X g:%2s s:%8s %s  [%4d]" % (
        stroke.brush_idx, stroke.brush_size * scale,
        int(stroke.brush_color[0] * 255),
        int(stroke.brush_color[1] * 255),
        int(stroke.brush_color[2] * 255),
        # stroke.brush_color[3],
        group, seed,
        start_ts,
        len(stroke.controlpoints)))


def main():
    import argparse
    parser = argparse.ArgumentParser(description="View information about a .tilt")
    parser.add_argument('--strokes', action='store_true', help="Dump the sketch strokes")
    parser.add_argument('--metadata', action='store_true', help="Dump the metadata")
    parser.add_argument('files', type=str, nargs='+', help="Files to examine")

    args = parser.parse_args()
    if not (args.strokes or args.metadata):
        print("You should pass at least one of --strokes or --metadata")

    for filename in args.files:
        t = Tilt(filename)
        if args.strokes:
            dump_sketch(t.sketch)
        if args.metadata:
            pprint.pprint(t.metadata)


if __name__ == '__main__':
    main()
