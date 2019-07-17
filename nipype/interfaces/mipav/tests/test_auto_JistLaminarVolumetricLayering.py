# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..developer import JistLaminarVolumetricLayering


def test_JistLaminarVolumetricLayering_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inInner=dict(
            argstr='--inInner %s',
            extensions=None,
        ),
        inLayering=dict(argstr='--inLayering %s', ),
        inLayering2=dict(argstr='--inLayering2 %s', ),
        inMax=dict(argstr='--inMax %d', ),
        inMin=dict(argstr='--inMin %f', ),
        inNumber=dict(argstr='--inNumber %d', ),
        inOuter=dict(
            argstr='--inOuter %s',
            extensions=None,
        ),
        inTopology=dict(argstr='--inTopology %s', ),
        incurvature=dict(argstr='--incurvature %d', ),
        inpresmooth=dict(argstr='--inpresmooth %s', ),
        inratio=dict(argstr='--inratio %f', ),
        null=dict(argstr='--null %s', ),
        outContinuous=dict(
            argstr='--outContinuous %s',
            hash_files=False,
        ),
        outDiscrete=dict(
            argstr='--outDiscrete %s',
            hash_files=False,
        ),
        outLayer=dict(
            argstr='--outLayer %s',
            hash_files=False,
        ),
        xDefaultMem=dict(argstr='-xDefaultMem %d', ),
        xMaxProcess=dict(
            argstr='-xMaxProcess %d',
            usedefault=True,
        ),
        xPrefExt=dict(argstr='--xPrefExt %s', ),
    )
    inputs = JistLaminarVolumetricLayering.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_JistLaminarVolumetricLayering_outputs():
    output_map = dict(
        outContinuous=dict(extensions=None, ),
        outDiscrete=dict(extensions=None, ),
        outLayer=dict(extensions=None, ),
    )
    outputs = JistLaminarVolumetricLayering.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
