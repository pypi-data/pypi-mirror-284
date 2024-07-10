"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from PyDefold.ddf import ddf_extensions_pb2 as ddf_dot_ddf__extensions__pb2
from PyDefold.ddf import ddf_math_pb2 as ddf_dot_ddf__math__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x15gamesys/gui_ddf.proto\x12\x08dmGuiDDF\x1a\x18ddf/ddf_extensions.proto\x1a\x12ddf/ddf_math.proto"\xcf\x15\n\x08NodeDesc\x12!\n\x08position\x18\x01 \x01(\x0b2\x0f.dmMath.Vector4\x12!\n\x08rotation\x18\x02 \x01(\x0b2\x0f.dmMath.Vector4\x12\x1e\n\x05scale\x18\x03 \x01(\x0b2\x0f.dmMath.Vector4\x12\x1d\n\x04size\x18\x04 \x01(\x0b2\x0f.dmMath.Vector4\x12\x1e\n\x05color\x18\x05 \x01(\x0b2\x0f.dmMath.Vector4\x12%\n\x04type\x18\x06 \x01(\x0e2\x17.dmGuiDDF.NodeDesc.Type\x12B\n\nblend_mode\x18\x07 \x01(\x0e2\x1c.dmGuiDDF.NodeDesc.BlendMode:\x10BLEND_MODE_ALPHA\x12\x0c\n\x04text\x18\x08 \x01(\t\x12\x0f\n\x07texture\x18\t \x01(\t\x12\x0c\n\x04font\x18\n \x01(\t\x12\n\n\x02id\x18\x0b \x01(\t\x129\n\x07xanchor\x18\x0c \x01(\x0e2\x1a.dmGuiDDF.NodeDesc.XAnchor:\x0cXANCHOR_NONE\x129\n\x07yanchor\x18\r \x01(\x0e2\x1a.dmGuiDDF.NodeDesc.YAnchor:\x0cYANCHOR_NONE\x125\n\x05pivot\x18\x0e \x01(\x0e2\x18.dmGuiDDF.NodeDesc.Pivot:\x0cPIVOT_CENTER\x12 \n\x07outline\x18\x0f \x01(\x0b2\x0f.dmMath.Vector4\x12\x1f\n\x06shadow\x18\x10 \x01(\x0b2\x0f.dmMath.Vector4\x12C\n\x0badjust_mode\x18\x11 \x01(\x0e2\x1d.dmGuiDDF.NodeDesc.AdjustMode:\x0fADJUST_MODE_FIT\x12\x19\n\nline_break\x18\x12 \x01(\x08:\x05false\x12\x0e\n\x06parent\x18\x13 \x01(\t\x12\r\n\x05layer\x18\x14 \x01(\t\x12\x1c\n\rinherit_alpha\x18\x15 \x01(\x08:\x05false\x12\x1f\n\x06slice9\x18\x16 \x01(\x0b2\x0f.dmMath.Vector4\x12D\n\x0bouterBounds\x18\x17 \x01(\x0e2\x1c.dmGuiDDF.NodeDesc.PieBounds:\x11PIEBOUNDS_ELLIPSE\x12\x16\n\x0binnerRadius\x18\x18 \x01(\x02:\x010\x12\x1d\n\x11perimeterVertices\x18\x19 \x01(\x05:\x0232\x12\x19\n\x0cpieFillAngle\x18\x1a \x01(\x02:\x03360\x12J\n\rclipping_mode\x18\x1b \x01(\x0e2\x1f.dmGuiDDF.NodeDesc.ClippingMode:\x12CLIPPING_MODE_NONE\x12\x1e\n\x10clipping_visible\x18\x1c \x01(\x08:\x04true\x12 \n\x11clipping_inverted\x18\x1d \x01(\x08:\x05false\x12\x10\n\x05alpha\x18\x1e \x01(\x02:\x011\x12\x18\n\routline_alpha\x18\x1f \x01(\x02:\x011\x12\x17\n\x0cshadow_alpha\x18  \x01(\x02:\x011\x12\x19\n\x11overridden_fields\x18! \x03(\r\x12\x16\n\x08template\x18" \x01(\tB\x04\xa0\xbb\x18\x01\x12\x1b\n\x13template_node_child\x18# \x01(\x08\x12\x17\n\x0ctext_leading\x18$ \x01(\x02:\x011\x12\x18\n\rtext_tracking\x18% \x01(\x02:\x010\x12@\n\tsize_mode\x18& \x01(\x0e2\x1b.dmGuiDDF.NodeDesc.SizeMode:\x10SIZE_MODE_MANUAL\x12\x13\n\x0bspine_scene\x18\' \x01(\t\x12\x1f\n\x17spine_default_animation\x18( \x01(\t\x12\x12\n\nspine_skin\x18) \x01(\t\x12\x1f\n\x10spine_node_child\x18* \x01(\x08:\x05false\x12\x12\n\nparticlefx\x18+ \x01(\t\x12\x16\n\x0bcustom_type\x18, \x01(\r:\x010\x12\x15\n\x07enabled\x18- \x01(\x08:\x04true\x12\x15\n\x07visible\x18. \x01(\x08:\x04true\x12\x10\n\x08material\x18/ \x01(\t"\xcb\x01\n\x04Type\x12\x15\n\x08TYPE_BOX\x10\x00\x1a\x07\xc2\xc1\x18\x03Box\x12\x17\n\tTYPE_TEXT\x10\x01\x1a\x08\xc2\xc1\x18\x04Text\x12\x15\n\x08TYPE_PIE\x10\x02\x1a\x07\xc2\xc1\x18\x03Pie\x12\x1f\n\rTYPE_TEMPLATE\x10\x03\x1a\x0c\xc2\xc1\x18\x08Template\x12\x19\n\nTYPE_SPINE\x10\x04\x1a\t\xc2\xc1\x18\x05Spine\x12#\n\x0fTYPE_PARTICLEFX\x10\x05\x1a\x0e\xc2\xc1\x18\nParticleFX\x12\x1b\n\x0bTYPE_CUSTOM\x10\x06\x1a\n\xc2\xc1\x18\x06Custom"\xc5\x01\n\tBlendMode\x12\x1f\n\x10BLEND_MODE_ALPHA\x10\x00\x1a\t\xc2\xc1\x18\x05Alpha\x12\x1b\n\x0eBLEND_MODE_ADD\x10\x01\x1a\x07\xc2\xc1\x18\x03Add\x124\n\x14BLEND_MODE_ADD_ALPHA\x10\x02\x1a\x1a\xc2\xc1\x18\x16Add Alpha (Deprecated)\x12!\n\x0fBLEND_MODE_MULT\x10\x03\x1a\x0c\xc2\xc1\x18\x08Multiply\x12!\n\x11BLEND_MODE_SCREEN\x10\x04\x1a\n\xc2\xc1\x18\x06Screen"X\n\x0cClippingMode\x12 \n\x12CLIPPING_MODE_NONE\x10\x00\x1a\x08\xc2\xc1\x18\x04None\x12&\n\x15CLIPPING_MODE_STENCIL\x10\x02\x1a\x0b\xc2\xc1\x18\x07Stencil"_\n\x07XAnchor\x12\x1a\n\x0cXANCHOR_NONE\x10\x00\x1a\x08\xc2\xc1\x18\x04None\x12\x1a\n\x0cXANCHOR_LEFT\x10\x01\x1a\x08\xc2\xc1\x18\x04Left\x12\x1c\n\rXANCHOR_RIGHT\x10\x02\x1a\t\xc2\xc1\x18\x05Right"_\n\x07YAnchor\x12\x1a\n\x0cYANCHOR_NONE\x10\x00\x1a\x08\xc2\xc1\x18\x04None\x12\x18\n\x0bYANCHOR_TOP\x10\x01\x1a\x07\xc2\xc1\x18\x03Top\x12\x1e\n\x0eYANCHOR_BOTTOM\x10\x02\x1a\n\xc2\xc1\x18\x06Bottom"\xfb\x01\n\x05Pivot\x12\x1c\n\x0cPIVOT_CENTER\x10\x00\x1a\n\xc2\xc1\x18\x06Center\x12\x16\n\x07PIVOT_N\x10\x01\x1a\t\xc2\xc1\x18\x05North\x12\x1c\n\x08PIVOT_NE\x10\x02\x1a\x0e\xc2\xc1\x18\nNorth East\x12\x15\n\x07PIVOT_E\x10\x03\x1a\x08\xc2\xc1\x18\x04East\x12\x1c\n\x08PIVOT_SE\x10\x04\x1a\x0e\xc2\xc1\x18\nSouth East\x12\x16\n\x07PIVOT_S\x10\x05\x1a\t\xc2\xc1\x18\x05South\x12\x1c\n\x08PIVOT_SW\x10\x06\x1a\x0e\xc2\xc1\x18\nSouth West\x12\x15\n\x07PIVOT_W\x10\x07\x1a\x08\xc2\xc1\x18\x04West\x12\x1c\n\x08PIVOT_NW\x10\x08\x1a\x0e\xc2\xc1\x18\nNorth West"p\n\nAdjustMode\x12\x1c\n\x0fADJUST_MODE_FIT\x10\x00\x1a\x07\xc2\xc1\x18\x03Fit\x12\x1e\n\x10ADJUST_MODE_ZOOM\x10\x01\x1a\x08\xc2\xc1\x18\x04Zoom\x12$\n\x13ADJUST_MODE_STRETCH\x10\x02\x1a\x0b\xc2\xc1\x18\x07Stretch"J\n\x08SizeMode\x12 \n\x10SIZE_MODE_MANUAL\x10\x00\x1a\n\xc2\xc1\x18\x06Manual\x12\x1c\n\x0eSIZE_MODE_AUTO\x10\x01\x1a\x08\xc2\xc1\x18\x04Auto"W\n\tPieBounds\x12&\n\x13PIEBOUNDS_RECTANGLE\x10\x00\x1a\r\xc2\xc1\x18\tRectangle\x12"\n\x11PIEBOUNDS_ELLIPSE\x10\x01\x1a\x0b\xc2\xc1\x18\x07Ellipse"\xef\t\n\tSceneDesc\x12\x14\n\x06script\x18\x01 \x02(\tB\x04\xa0\xbb\x18\x01\x12+\n\x05fonts\x18\x02 \x03(\x0b2\x1c.dmGuiDDF.SceneDesc.FontDesc\x121\n\x08textures\x18\x03 \x03(\x0b2\x1f.dmGuiDDF.SceneDesc.TextureDesc\x12)\n\x10background_color\x18\x04 \x01(\x0b2\x0f.dmMath.Vector4\x12!\n\x05nodes\x18\x06 \x03(\x0b2\x12.dmGuiDDF.NodeDesc\x12-\n\x06layers\x18\x07 \x03(\x0b2\x1d.dmGuiDDF.SceneDesc.LayerDesc\x128\n\x08material\x18\x08 \x01(\t: /builtins/materials/gui.materialB\x04\xa0\xbb\x18\x01\x12/\n\x07layouts\x18\t \x03(\x0b2\x1e.dmGuiDDF.SceneDesc.LayoutDesc\x12V\n\x10adjust_reference\x18\n \x01(\x0e2#.dmGuiDDF.SceneDesc.AdjustReference:\x17ADJUST_REFERENCE_LEGACY\x12\x16\n\tmax_nodes\x18\x0b \x01(\r:\x03512\x128\n\x0cspine_scenes\x18\x0c \x03(\x0b2".dmGuiDDF.SceneDesc.SpineSceneDesc\x127\n\x0bparticlefxs\x18\r \x03(\x0b2".dmGuiDDF.SceneDesc.ParticleFXDesc\x123\n\tresources\x18\x0e \x03(\x0b2 .dmGuiDDF.SceneDesc.ResourceDesc\x123\n\tmaterials\x18\x0f \x03(\x0b2 .dmGuiDDF.SceneDesc.MaterialDesc\x1a,\n\x08FontDesc\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x12\n\x04font\x18\x02 \x02(\tB\x04\xa0\xbb\x18\x01\x1a2\n\x0bTextureDesc\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x15\n\x07texture\x18\x02 \x02(\tB\x04\xa0\xbb\x18\x01\x1a\x19\n\tLayerDesc\x12\x0c\n\x04name\x18\x01 \x02(\t\x1a=\n\nLayoutDesc\x12\x0c\n\x04name\x18\x01 \x02(\t\x12!\n\x05nodes\x18\x02 \x03(\x0b2\x12.dmGuiDDF.NodeDesc\x1a4\n\x0cMaterialDesc\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x16\n\x08material\x18\x02 \x02(\tB\x04\xa0\xbb\x18\x01\x1a9\n\x0eSpineSceneDesc\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x19\n\x0bspine_scene\x18\x02 \x02(\tB\x04\xa0\xbb\x18\x01\x1a0\n\x0cResourceDesc\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x12\n\x04path\x18\x02 \x02(\tB\x04\xa0\xbb\x18\x01\x1a8\n\x0eParticleFXDesc\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x18\n\nparticlefx\x18\x02 \x02(\tB\x04\xa0\xbb\x18\x01"\x9d\x01\n\x0fAdjustReference\x122\n\x17ADJUST_REFERENCE_LEGACY\x10\x00\x1a\x15\xc2\xc1\x18\x11Root (Deprecated)\x12)\n\x17ADJUST_REFERENCE_PARENT\x10\x01\x1a\x0c\xc2\xc1\x18\x08Per Node\x12+\n\x19ADJUST_REFERENCE_DISABLED\x10\x02\x1a\x0c\xc2\xc1\x18\x08Disabled"0\n\rLayoutChanged\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x13\n\x0bprevious_id\x18\x02 \x02(\x04B\x1f\n\x18com.dynamo.gamesys.protoB\x03Gui'
    )
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gamesys.gui_ddf_pb2',
    globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x18com.dynamo.gamesys.protoB\x03Gui'
    _NODEDESC_TYPE.values_by_name['TYPE_BOX']._options = None
    _NODEDESC_TYPE.values_by_name['TYPE_BOX'
        ]._serialized_options = b'\xc2\xc1\x18\x03Box'
    _NODEDESC_TYPE.values_by_name['TYPE_TEXT']._options = None
    _NODEDESC_TYPE.values_by_name['TYPE_TEXT'
        ]._serialized_options = b'\xc2\xc1\x18\x04Text'
    _NODEDESC_TYPE.values_by_name['TYPE_PIE']._options = None
    _NODEDESC_TYPE.values_by_name['TYPE_PIE'
        ]._serialized_options = b'\xc2\xc1\x18\x03Pie'
    _NODEDESC_TYPE.values_by_name['TYPE_TEMPLATE']._options = None
    _NODEDESC_TYPE.values_by_name['TYPE_TEMPLATE'
        ]._serialized_options = b'\xc2\xc1\x18\x08Template'
    _NODEDESC_TYPE.values_by_name['TYPE_SPINE']._options = None
    _NODEDESC_TYPE.values_by_name['TYPE_SPINE'
        ]._serialized_options = b'\xc2\xc1\x18\x05Spine'
    _NODEDESC_TYPE.values_by_name['TYPE_PARTICLEFX']._options = None
    _NODEDESC_TYPE.values_by_name['TYPE_PARTICLEFX'
        ]._serialized_options = b'\xc2\xc1\x18\nParticleFX'
    _NODEDESC_TYPE.values_by_name['TYPE_CUSTOM']._options = None
    _NODEDESC_TYPE.values_by_name['TYPE_CUSTOM'
        ]._serialized_options = b'\xc2\xc1\x18\x06Custom'
    _NODEDESC_BLENDMODE.values_by_name['BLEND_MODE_ALPHA']._options = None
    _NODEDESC_BLENDMODE.values_by_name['BLEND_MODE_ALPHA'
        ]._serialized_options = b'\xc2\xc1\x18\x05Alpha'
    _NODEDESC_BLENDMODE.values_by_name['BLEND_MODE_ADD']._options = None
    _NODEDESC_BLENDMODE.values_by_name['BLEND_MODE_ADD'
        ]._serialized_options = b'\xc2\xc1\x18\x03Add'
    _NODEDESC_BLENDMODE.values_by_name['BLEND_MODE_ADD_ALPHA']._options = None
    _NODEDESC_BLENDMODE.values_by_name['BLEND_MODE_ADD_ALPHA'
        ]._serialized_options = b'\xc2\xc1\x18\x16Add Alpha (Deprecated)'
    _NODEDESC_BLENDMODE.values_by_name['BLEND_MODE_MULT']._options = None
    _NODEDESC_BLENDMODE.values_by_name['BLEND_MODE_MULT'
        ]._serialized_options = b'\xc2\xc1\x18\x08Multiply'
    _NODEDESC_BLENDMODE.values_by_name['BLEND_MODE_SCREEN']._options = None
    _NODEDESC_BLENDMODE.values_by_name['BLEND_MODE_SCREEN'
        ]._serialized_options = b'\xc2\xc1\x18\x06Screen'
    _NODEDESC_CLIPPINGMODE.values_by_name['CLIPPING_MODE_NONE']._options = None
    _NODEDESC_CLIPPINGMODE.values_by_name['CLIPPING_MODE_NONE'
        ]._serialized_options = b'\xc2\xc1\x18\x04None'
    _NODEDESC_CLIPPINGMODE.values_by_name['CLIPPING_MODE_STENCIL'
        ]._options = None
    _NODEDESC_CLIPPINGMODE.values_by_name['CLIPPING_MODE_STENCIL'
        ]._serialized_options = b'\xc2\xc1\x18\x07Stencil'
    _NODEDESC_XANCHOR.values_by_name['XANCHOR_NONE']._options = None
    _NODEDESC_XANCHOR.values_by_name['XANCHOR_NONE'
        ]._serialized_options = b'\xc2\xc1\x18\x04None'
    _NODEDESC_XANCHOR.values_by_name['XANCHOR_LEFT']._options = None
    _NODEDESC_XANCHOR.values_by_name['XANCHOR_LEFT'
        ]._serialized_options = b'\xc2\xc1\x18\x04Left'
    _NODEDESC_XANCHOR.values_by_name['XANCHOR_RIGHT']._options = None
    _NODEDESC_XANCHOR.values_by_name['XANCHOR_RIGHT'
        ]._serialized_options = b'\xc2\xc1\x18\x05Right'
    _NODEDESC_YANCHOR.values_by_name['YANCHOR_NONE']._options = None
    _NODEDESC_YANCHOR.values_by_name['YANCHOR_NONE'
        ]._serialized_options = b'\xc2\xc1\x18\x04None'
    _NODEDESC_YANCHOR.values_by_name['YANCHOR_TOP']._options = None
    _NODEDESC_YANCHOR.values_by_name['YANCHOR_TOP'
        ]._serialized_options = b'\xc2\xc1\x18\x03Top'
    _NODEDESC_YANCHOR.values_by_name['YANCHOR_BOTTOM']._options = None
    _NODEDESC_YANCHOR.values_by_name['YANCHOR_BOTTOM'
        ]._serialized_options = b'\xc2\xc1\x18\x06Bottom'
    _NODEDESC_PIVOT.values_by_name['PIVOT_CENTER']._options = None
    _NODEDESC_PIVOT.values_by_name['PIVOT_CENTER'
        ]._serialized_options = b'\xc2\xc1\x18\x06Center'
    _NODEDESC_PIVOT.values_by_name['PIVOT_N']._options = None
    _NODEDESC_PIVOT.values_by_name['PIVOT_N'
        ]._serialized_options = b'\xc2\xc1\x18\x05North'
    _NODEDESC_PIVOT.values_by_name['PIVOT_NE']._options = None
    _NODEDESC_PIVOT.values_by_name['PIVOT_NE'
        ]._serialized_options = b'\xc2\xc1\x18\nNorth East'
    _NODEDESC_PIVOT.values_by_name['PIVOT_E']._options = None
    _NODEDESC_PIVOT.values_by_name['PIVOT_E'
        ]._serialized_options = b'\xc2\xc1\x18\x04East'
    _NODEDESC_PIVOT.values_by_name['PIVOT_SE']._options = None
    _NODEDESC_PIVOT.values_by_name['PIVOT_SE'
        ]._serialized_options = b'\xc2\xc1\x18\nSouth East'
    _NODEDESC_PIVOT.values_by_name['PIVOT_S']._options = None
    _NODEDESC_PIVOT.values_by_name['PIVOT_S'
        ]._serialized_options = b'\xc2\xc1\x18\x05South'
    _NODEDESC_PIVOT.values_by_name['PIVOT_SW']._options = None
    _NODEDESC_PIVOT.values_by_name['PIVOT_SW'
        ]._serialized_options = b'\xc2\xc1\x18\nSouth West'
    _NODEDESC_PIVOT.values_by_name['PIVOT_W']._options = None
    _NODEDESC_PIVOT.values_by_name['PIVOT_W'
        ]._serialized_options = b'\xc2\xc1\x18\x04West'
    _NODEDESC_PIVOT.values_by_name['PIVOT_NW']._options = None
    _NODEDESC_PIVOT.values_by_name['PIVOT_NW'
        ]._serialized_options = b'\xc2\xc1\x18\nNorth West'
    _NODEDESC_ADJUSTMODE.values_by_name['ADJUST_MODE_FIT']._options = None
    _NODEDESC_ADJUSTMODE.values_by_name['ADJUST_MODE_FIT'
        ]._serialized_options = b'\xc2\xc1\x18\x03Fit'
    _NODEDESC_ADJUSTMODE.values_by_name['ADJUST_MODE_ZOOM']._options = None
    _NODEDESC_ADJUSTMODE.values_by_name['ADJUST_MODE_ZOOM'
        ]._serialized_options = b'\xc2\xc1\x18\x04Zoom'
    _NODEDESC_ADJUSTMODE.values_by_name['ADJUST_MODE_STRETCH']._options = None
    _NODEDESC_ADJUSTMODE.values_by_name['ADJUST_MODE_STRETCH'
        ]._serialized_options = b'\xc2\xc1\x18\x07Stretch'
    _NODEDESC_SIZEMODE.values_by_name['SIZE_MODE_MANUAL']._options = None
    _NODEDESC_SIZEMODE.values_by_name['SIZE_MODE_MANUAL'
        ]._serialized_options = b'\xc2\xc1\x18\x06Manual'
    _NODEDESC_SIZEMODE.values_by_name['SIZE_MODE_AUTO']._options = None
    _NODEDESC_SIZEMODE.values_by_name['SIZE_MODE_AUTO'
        ]._serialized_options = b'\xc2\xc1\x18\x04Auto'
    _NODEDESC_PIEBOUNDS.values_by_name['PIEBOUNDS_RECTANGLE']._options = None
    _NODEDESC_PIEBOUNDS.values_by_name['PIEBOUNDS_RECTANGLE'
        ]._serialized_options = b'\xc2\xc1\x18\tRectangle'
    _NODEDESC_PIEBOUNDS.values_by_name['PIEBOUNDS_ELLIPSE']._options = None
    _NODEDESC_PIEBOUNDS.values_by_name['PIEBOUNDS_ELLIPSE'
        ]._serialized_options = b'\xc2\xc1\x18\x07Ellipse'
    _NODEDESC.fields_by_name['template']._options = None
    _NODEDESC.fields_by_name['template'
        ]._serialized_options = b'\xa0\xbb\x18\x01'
    _SCENEDESC_FONTDESC.fields_by_name['font']._options = None
    _SCENEDESC_FONTDESC.fields_by_name['font'
        ]._serialized_options = b'\xa0\xbb\x18\x01'
    _SCENEDESC_TEXTUREDESC.fields_by_name['texture']._options = None
    _SCENEDESC_TEXTUREDESC.fields_by_name['texture'
        ]._serialized_options = b'\xa0\xbb\x18\x01'
    _SCENEDESC_MATERIALDESC.fields_by_name['material']._options = None
    _SCENEDESC_MATERIALDESC.fields_by_name['material'
        ]._serialized_options = b'\xa0\xbb\x18\x01'
    _SCENEDESC_SPINESCENEDESC.fields_by_name['spine_scene']._options = None
    _SCENEDESC_SPINESCENEDESC.fields_by_name['spine_scene'
        ]._serialized_options = b'\xa0\xbb\x18\x01'
    _SCENEDESC_RESOURCEDESC.fields_by_name['path']._options = None
    _SCENEDESC_RESOURCEDESC.fields_by_name['path'
        ]._serialized_options = b'\xa0\xbb\x18\x01'
    _SCENEDESC_PARTICLEFXDESC.fields_by_name['particlefx']._options = None
    _SCENEDESC_PARTICLEFXDESC.fields_by_name['particlefx'
        ]._serialized_options = b'\xa0\xbb\x18\x01'
    _SCENEDESC_ADJUSTREFERENCE.values_by_name['ADJUST_REFERENCE_LEGACY'
        ]._options = None
    _SCENEDESC_ADJUSTREFERENCE.values_by_name['ADJUST_REFERENCE_LEGACY'
        ]._serialized_options = b'\xc2\xc1\x18\x11Root (Deprecated)'
    _SCENEDESC_ADJUSTREFERENCE.values_by_name['ADJUST_REFERENCE_PARENT'
        ]._options = None
    _SCENEDESC_ADJUSTREFERENCE.values_by_name['ADJUST_REFERENCE_PARENT'
        ]._serialized_options = b'\xc2\xc1\x18\x08Per Node'
    _SCENEDESC_ADJUSTREFERENCE.values_by_name['ADJUST_REFERENCE_DISABLED'
        ]._options = None
    _SCENEDESC_ADJUSTREFERENCE.values_by_name['ADJUST_REFERENCE_DISABLED'
        ]._serialized_options = b'\xc2\xc1\x18\x08Disabled'
    _SCENEDESC.fields_by_name['script']._options = None
    _SCENEDESC.fields_by_name['script'
        ]._serialized_options = b'\xa0\xbb\x18\x01'
    _SCENEDESC.fields_by_name['material']._options = None
    _SCENEDESC.fields_by_name['material'
        ]._serialized_options = b'\xa0\xbb\x18\x01'
    _NODEDESC._serialized_start = 82
    _NODEDESC._serialized_end = 2849
    _NODEDESC_TYPE._serialized_start = 1629
    _NODEDESC_TYPE._serialized_end = 1832
    _NODEDESC_BLENDMODE._serialized_start = 1835
    _NODEDESC_BLENDMODE._serialized_end = 2032
    _NODEDESC_CLIPPINGMODE._serialized_start = 2034
    _NODEDESC_CLIPPINGMODE._serialized_end = 2122
    _NODEDESC_XANCHOR._serialized_start = 2124
    _NODEDESC_XANCHOR._serialized_end = 2219
    _NODEDESC_YANCHOR._serialized_start = 2221
    _NODEDESC_YANCHOR._serialized_end = 2316
    _NODEDESC_PIVOT._serialized_start = 2319
    _NODEDESC_PIVOT._serialized_end = 2570
    _NODEDESC_ADJUSTMODE._serialized_start = 2572
    _NODEDESC_ADJUSTMODE._serialized_end = 2684
    _NODEDESC_SIZEMODE._serialized_start = 2686
    _NODEDESC_SIZEMODE._serialized_end = 2760
    _NODEDESC_PIEBOUNDS._serialized_start = 2762
    _NODEDESC_PIEBOUNDS._serialized_end = 2849
    _SCENEDESC._serialized_start = 2852
    _SCENEDESC._serialized_end = 4115
    _SCENEDESC_FONTDESC._serialized_start = 3548
    _SCENEDESC_FONTDESC._serialized_end = 3592
    _SCENEDESC_TEXTUREDESC._serialized_start = 3594
    _SCENEDESC_TEXTUREDESC._serialized_end = 3644
    _SCENEDESC_LAYERDESC._serialized_start = 3646
    _SCENEDESC_LAYERDESC._serialized_end = 3671
    _SCENEDESC_LAYOUTDESC._serialized_start = 3673
    _SCENEDESC_LAYOUTDESC._serialized_end = 3734
    _SCENEDESC_MATERIALDESC._serialized_start = 3736
    _SCENEDESC_MATERIALDESC._serialized_end = 3788
    _SCENEDESC_SPINESCENEDESC._serialized_start = 3790
    _SCENEDESC_SPINESCENEDESC._serialized_end = 3847
    _SCENEDESC_RESOURCEDESC._serialized_start = 3849
    _SCENEDESC_RESOURCEDESC._serialized_end = 3897
    _SCENEDESC_PARTICLEFXDESC._serialized_start = 3899
    _SCENEDESC_PARTICLEFXDESC._serialized_end = 3955
    _SCENEDESC_ADJUSTREFERENCE._serialized_start = 3958
    _SCENEDESC_ADJUSTREFERENCE._serialized_end = 4115
    _LAYOUTCHANGED._serialized_start = 4117
    _LAYOUTCHANGED._serialized_end = 4165

