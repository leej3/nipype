# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import FitMSParams


def test_FitMSParams_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        flip_list=dict(),
        in_files=dict(
            argstr='%s',
            mandatory=True,
            position=-2,
        ),
        out_dir=dict(
            argstr='%s',
            genfile=True,
            position=-1,
        ),
        subjects_dir=dict(),
        te_list=dict(),
        tr_list=dict(),
        xfm_list=dict(),
    )
    inputs = FitMSParams.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_FitMSParams_outputs():
    output_map = dict(
        pd_image=dict(extensions=None, ),
        t1_image=dict(extensions=None, ),
        t2star_image=dict(extensions=None, ),
    )
    outputs = FitMSParams.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
