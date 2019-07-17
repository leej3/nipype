# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import WarpPointsFromStd


def test_WarpPointsFromStd_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        coord_mm=dict(
            argstr='-mm',
            xor=['coord_vox'],
        ),
        coord_vox=dict(
            argstr='-vox',
            xor=['coord_mm'],
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        img_file=dict(
            argstr='-img %s',
            extensions=None,
            mandatory=True,
        ),
        in_coords=dict(
            argstr='%s',
            extensions=None,
            mandatory=True,
            position=-2,
        ),
        std_file=dict(
            argstr='-std %s',
            extensions=None,
            mandatory=True,
        ),
        warp_file=dict(
            argstr='-warp %s',
            extensions=None,
            xor=['xfm_file'],
        ),
        xfm_file=dict(
            argstr='-xfm %s',
            extensions=None,
            xor=['warp_file'],
        ),
    )
    inputs = WarpPointsFromStd.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_WarpPointsFromStd_outputs():
    output_map = dict(out_file=dict(extensions=None, ), )
    outputs = WarpPointsFromStd.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
