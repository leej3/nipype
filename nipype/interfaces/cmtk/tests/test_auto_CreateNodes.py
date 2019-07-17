# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..cmtk import CreateNodes


def test_CreateNodes_inputs():
    input_map = dict(
        out_filename=dict(
            extensions=None,
            usedefault=True,
        ),
        resolution_network_file=dict(
            extensions=None,
            mandatory=True,
        ),
        roi_file=dict(
            extensions=None,
            mandatory=True,
        ),
    )
    inputs = CreateNodes.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_CreateNodes_outputs():
    output_map = dict(node_network=dict(extensions=None, ), )
    outputs = CreateNodes.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
