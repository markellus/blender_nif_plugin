'''Nif Properties, adds custom properties via Blender types''' 

# ***** BEGIN LICENSE BLOCK *****
# 
# Copyright © 2005-2013, NIF File Format Library and Tools contributors.
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
from bpy.props import (PointerProperty, 
                       FloatVectorProperty,
                       StringProperty,
                       IntProperty,
                       BoolProperty,
                       EnumProperty
                       )

from pyffi.formats.nif import NifFormat

def underscore_to_camelcase(s):
    """Take the underscore-separated string s and return a camelCase
    equivalent.  Initial and final underscores are preserved, and medial
    pairs of underscores are turned into a single underscore."""
    def camelcase_words(words):
        first_word_passed = False
        for word in words:
            
            if not word:
                yield "_"
                continue
            if first_word_passed:
                yield word.capitalize()
            else:
                yield word.lower()
            first_word_passed = True
    return ''.join(camelcase_words(s.split('_')))


class NiftoolsMaterialProps(bpy.types.PropertyGroup):
    '''Adds custom properties to material'''
    
    @classmethod
    def register(cls):
        bpy.types.Material.niftools = PointerProperty(
                        name='Niftools Materials',
                        description = 'Additional material properties used by the Nif File Format',
                        type=cls,
                        )
        
        cls.diffuse_color = FloatVectorProperty(
                name='Diffuse', subtype='COLOR', default=[1.0,1.0,1.0],min=0.0, max=1.0)
        
        cls.ambient_color = FloatVectorProperty(
                name='Ambient', subtype='COLOR', default=[1.0,1.0,1.0],min=0.0, max=1.0)
        
        cls.emissive_color = FloatVectorProperty(
                name='Emissive', subtype='COLOR', default=[0.0,0.0,0.0],min=0.0, max=1.0)
        
        cls.emissive_preview = BoolProperty(
                name='Preview', description='Allows a viewport preview of the emissive property', default=False)
    
    @classmethod
    def unregister(cls):
        del bpy.types.Material.niftools


class NiftoolsBoneProps(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Bone.niftools = PointerProperty(
                        name='Niftools Bone Property',
                        description = 'Additional bone properties used by the Nif File Format',
                        type = cls,
                        )
        cls.flags = IntProperty(
                        name = 'Nif Flags'
                        )
        
    @classmethod
    def unregister(cls):
        del bpy.types.Bone.niftools


class NiftoolsBsShaderProps(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Object.niftools_bsshader = PointerProperty(
                        name='Niftools BsShader Property',
                        description = 'Properties used by the BsShader for the Nif File Format',
                        type = cls,
                        )
        cls.specular = BoolProperty(
                        name = 'Specular'
                        )
        
        cls.skin = BoolProperty(
                        name = 'Skinned'
                        )
        
        cls.lowdetail = BoolProperty(
                        name = 'Low Detail'
                        )
        
        cls.vertexalpha = BoolProperty(
                        name = 'Vertex Alpha'
                        )
        
        cls.unknown1 = BoolProperty(
                        name = 'Unknown 1'
                        )
        
        cls.singlepass = BoolProperty(
                        name = 'Single Pass'
                        )
        
        cls.empty = BoolProperty(
                        name = 'Empty'
                        )
        
        cls.environmentmapping = BoolProperty(
                        name = 'Environment Mapping'
                        )
        
        cls.alphatexture = BoolProperty(
                        name = 'Alpha Texture'
                        )
        
        cls.unknown2 = BoolProperty(
                        name = 'Unknown 2'
                        )
        
        cls.facegen = BoolProperty(
                        name = 'Face Gen'
                        )
        
        cls.parallaxshaderindex = BoolProperty(
                        name = 'Parallax Shader Index'
                        )
        
        cls.unknown3 = BoolProperty(
                        name = 'Unknown 3'
                        )
        
        cls.nonprojectiveshadows = BoolProperty(
                        name = 'Non-Projective Shadows'
                        )
        
        cls.unknown4 = BoolProperty(
                        name = 'Unknown 4'
                        )
        
        cls.refraction = BoolProperty(
                        name = 'Refraction'
                        )
        
        cls.firerefraction = BoolProperty(
                        name = 'Fire Refraction'
                        )
        
        cls.eyeenvronmentmapping = BoolProperty(
                        name = 'Eye Environment Mapping'
                        )
        
        cls.hair = BoolProperty(
                        name = 'Hair'
                        )
        
        cls.dynamicalpha = BoolProperty(
                        name = 'Dynamic Alpha'
                        )
        
        cls.localmaphidesecret = BoolProperty(
                        name = 'Local Map Hide Secret'
                        )
        
        cls.windowenvironmentmapping = BoolProperty(
                        name = 'Window Environment Mapping'
                        )
        
        cls.treebillboard = BoolProperty(
                        name = 'Tree Billboard'
                        )
        
        cls.shadowfrustum = BoolProperty(
                        name = 'Shadow Frustum'
                        )
        
        cls.multipletextures = BoolProperty(
                        name = 'Multiple Textures'
                        )
        
        cls.remappabletextures = BoolProperty(
                        name = 'Remappable Textures'
                        )
        
        cls.decalsinglepass = BoolProperty(
                        name = 'Decal Single Pass'
                        )
        
        cls.dynamicdecalsinglepass = BoolProperty(
                        name = 'Dynamic Decal Single Pass'
                        )
        
        cls.parallaxocclusion = BoolProperty(
                        name = 'Parallax Occlusion'
                        )
        
        cls.externalemittance = BoolProperty(
                        name = 'External Emittance'
                        )
        
        cls.shadowmap = BoolProperty(
                        name = 'Shadow Map'
                        )
        
        cls.zbuffertest = BoolProperty(
                        name = 'Z Buffer Test'
                        )
        
    @classmethod
    def unregister(cls):
        del bpy.types.Object.niftools_bsshader




class NiftoolsObjectProps(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Object.niftools = PointerProperty(
                        name='Niftools Object Property',
                        description = 'Additional object properties used by the Nif File Format',
                        type = cls,
                        )
        cls.longname = StringProperty(
                        name = 'Nif LongName'
                        )

        cls.objectflags = IntProperty(
                        name = 'Object Flag',
                        description = 'Controls animation and collision',
                        default = 2 # 2 = Bit 1, enable collision
                        )

        cls.bsxflags = IntProperty(
                        name = 'BSXFlags',
                        description = 'Controls animation and collision',
                        default = 2 # 2 = Bit 1, enable collision
                        )

        cls.upb = StringProperty(
                        name = 'UPB',
                        description = 'Commands for an optimizer?',
                        default = ''
                        )

        cls.LHMaxAngle = IntProperty(
                        name = 'LHMaxAngle',
                        description = 'Havok limited hinge max angle.',
                        )

        cls.LHMinAngle = IntProperty(
                        name = 'LHMinAngle',
                        description = 'Havok limited hinge min angle.',
                        )

        cls.LHMaxFriction = IntProperty(
                        name = 'LHMaxFriction',
                        description = 'Havok limited hinge max friction.',
                        )
        
        cls.shadowfrustrum = BoolProperty(
                        name = 'Shadow Frustrum',
                        description = 'Shader property to do stuff with things',
                        )
        
    @classmethod
    def unregister(cls):
        del bpy.types.Object.niftools   


class NiftoolsObjectCollisionProps(bpy.types.PropertyGroup):
    '''Group of Havok related properties, which gets attached to objects through a property pointer.'''
    @classmethod
    def register(cls):

        # physics
        bpy.types.Object.nifcollision = PointerProperty(
                        name='Niftools Collision Property',
                        description = 'Additional collision properties used by the Nif File Format',
                        type = cls,
                        )
        
        cls.motion_system = EnumProperty(
                        name='Motion System',
                        description = 'Havok Motion System settings for bhkRigidBody(t)',
                        items = [(item, item,"", i) for i, item in enumerate(NifFormat.MotionSystem._enumkeys)],
                        # default = 'MO_SYS_FIXED',
                        
                        )
           
        cls.oblivion_layer = EnumProperty(
                        name = 'Oblivion Layer',
                        description = 'Mesh color, used in Editor',
                        items = [(item, item,"", i) for i, item in enumerate(NifFormat.OblivionLayer._enumkeys)],
                        # default = 'OL_STATIC',
                        )
          
        cls.quality_type = EnumProperty(
                        name = 'Quality Type',
                        description = 'Determines quality of motion',
                        items = [(item, item,"", i) for i, item in enumerate(NifFormat.MotionQuality._enumkeys)],
                        # default = 'MO_QUAL_FIXED',
                        )
        
        cls.col_filter = IntProperty(
                        name = 'Col Filter',
                        description = 'Flags for bhkRigidBody(t)',
                        default = 0
                        )
        
        cls.havok_material = EnumProperty(
                        name = 'Havok Material',
                        description = 'The Shapes material',
                        items = [(item, item,"", i) for i, item in enumerate(NifFormat.HavokMaterial._enumkeys)],
                        # default = 'HAV_MAT_WOOD'
                        )
                        
        cls.export_bhklist = BoolProperty(
                        name = 'Export BHKList',
                        description = 'None',
                        default = False
                        )
        
        cls.use_blender_properties = BoolProperty(
                        name = 'Use Blender Properties',
                        description = 'Whether or not to export collision settings via blender properties',
                        default = False,
                        )
    @classmethod
    def unregister(cls):
        del bpy.types.Object.nifcollision
        
        
def register():
    bpy.utils.register_class(NiftoolsMaterialProps)
    bpy.utils.register_class(NiftoolsObjectProps)
    bpy.utils.register_class(NiftoolsObjectCollisionProps)


def unregister():
    bpy.utils.unregister_class(NiftoolsMaterialProps)
    bpy.utils.unregister_class(NiftoolsObjectProps)
    bpy.utils.unregister_class(NiftoolsObjectCollisionProps)