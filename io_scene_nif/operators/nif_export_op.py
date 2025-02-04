'''Blender Nif Plugin Main Export operators, function called through Export Menu'''

# ***** BEGIN LICENSE BLOCK *****
# 
# Copyright © 2005-2015, NIF File Format Library and Tools contributors.
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
# 
#    * Redistributions in binary form must reproduce the above
#      copyright notice, this list of conditions and the following
#      disclaimer in the documentation and/or other materials provided
#      with the distribution.
# 
#    * Neither the name of the NIF File Format Library and Tools
#      project nor the names of its contributors may be used to endorse
#      or promote products derived from this software without specific
#      prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# ***** END LICENSE BLOCK *****

import bpy
from bpy_extras.io_utils import ExportHelper

from pyffi.formats.nif import NifFormat

from io_scene_nif import nif_export

from .nif_common_op import NifOperatorCommon

def _game_to_enum(game):
    symbols = ":,'\" +-*!?;./="
    table = str.maketrans(symbols, "_" * len(symbols))
    enum = game.upper().translate(table).replace("__", "_")
    return enum

class NifExportOperator(bpy.types.Operator, ExportHelper, NifOperatorCommon):
    """Operator for saving a nif file."""

    #: Name of function for calling the nif export operators.
    bl_idname = "export_scene.nif"

    #: How the nif export operators is labelled in the user interface.
    bl_label = "Export NIF"

    #: Number of blender units per nif unit.
    scale_correction_export = bpy.props.FloatProperty(
        name="Scale Correction Export",
        description="Changes size of mesh from Blender default to nif default.",
        default=1.0,
        min=0.01, max=100.0, precision=2)

    #: For which game to export.
    game = bpy.props.EnumProperty(
        items=[
            (_game_to_enum(game), game, "Export for " + game)
            # implementation note: reversed makes it show alphabetically
            # (at least with the current blender)
            for game in reversed(sorted(
                [x for x in NifFormat.games.keys() if x != '?']))
            ],
        name="Game",
        description="For which game to export.",
        default='SKYRIM')

    #: How to export animation.
    animation = bpy.props.EnumProperty(
        items=[
            ('ALL_NIF', "All (nif)", "Geometry and animation to a single nif."),
            ('ALL_NIF_XNIF_XKF', "All (nif, xnif, xkf)", "Geometry and animation to a nif, xnif, and xkf (for Morrowind)."),
            ('GEOM_NIF', "Geometry only (nif)", "Only geometry to a single nif."),
            ('ANIM_KF', "Animation only (kf)", "Only animation to a single kf."),
            ],
        name="Process",
        description="Selects which parts of the blender file to export.",
        default='ALL_NIF')

    #: Smoothen inter-object seams.
    smooth_object_seams = bpy.props.BoolProperty(
        name="Smooth Inter-Object Seams",
        description="Smooth normal data along inter-object seams.",
        default=True)

    #: Use BSAnimationNode (for Morrowind).
    bs_animation_node = bpy.props.BoolProperty(
        name="Use NiBSAnimationNode",
        description="Use NiBSAnimationNode (for Morrowind).",
        default=False)

    #: Stripify geometries. Deprecate? (Strips are slower than triangle shapes.)
    stripify = bpy.props.BoolProperty(
        name="Stripify Geometries",
        description="Stripify geometries.",
        default=False,
        options={'HIDDEN'})

    #: Stitch strips. Deprecate? (Strips are slower than triangle shapes.)
    stitch_strips = bpy.props.BoolProperty(
        name="Stitch Strips",
        description="Stitch strips.",
        default=True,
        options={'HIDDEN'})

    #: Flatten skin.
    flatten_skin = bpy.props.BoolProperty(
        name="Flatten Skin",
        description="Flatten skin.",
        default=False)

    #: Export skin partition.
    skin_partition = bpy.props.BoolProperty(
        name="Skin Partition",
        description="Export skin partition.",
        default=True)

    #: Pad and sort bones.
    pad_bones = bpy.props.BoolProperty(
        name="Pad & Sort Bones",
        description="Pad and sort bones.",
        default=False)

    #: Maximum number of bones per skin partition.
    max_bones_per_partition = bpy.props.IntProperty(
        name = "Max Partition Bones",
        description="Maximum number of bones per skin partition.",
        default=24, min=4, max=63)

    #: Maximum number of bones per vertex in skin partitions.
    max_bones_per_vertex = bpy.props.IntProperty(
        name = "Max Vertex Bones",
        description="Maximum number of bones per vertex in skin partitions.",
        default=4, min=1,
        )

    #: Pad and sort bones.
    force_dds = bpy.props.BoolProperty(
        name="Force DDS",
        description="Force texture .dds extension.",
        default=True)

    #: Map game enum to nif version.
    version = {
        _game_to_enum(game): versions[-1]
        for game, versions in NifFormat.games.items() if game != '?'
        }

    def execute(self, context):
        """Execute the export operators: first constructs a
        :class:`~io_scene_nif.nif_export.NifExport` instance and then
        calls its :meth:`~io_scene_nif.nif_export.NifExport.execute`
        method.
        """
        return nif_export.NifExport(self, context).execute()
    
