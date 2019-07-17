# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import ComputeMask


def test_ComputeMask_inputs():
    input_map = dict(
        M=dict(),
        cc=dict(),
        m=dict(),
        mean_volume=dict(
            extensions=None,
            mandatory=True,
        ),
        reference_volume=dict(extensions=None, ),
    )
    inputs = ComputeMask.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_ComputeMask_outputs():
    output_map = dict(brain_mask=dict(extensions=None, ), )
    outputs = ComputeMask.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
