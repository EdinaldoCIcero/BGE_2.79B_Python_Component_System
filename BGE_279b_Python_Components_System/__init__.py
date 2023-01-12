bl_info = {
    "name"          : "BGE_2.79b_Python_Components_System",
    "author"        : "By agoose77 <-//-> Editado por edinaldo_cicero",
    "version"       : ( 0 , 2  , 0 ),
    "blender"       : ( 2 , 79 , 0 ),
    "description"   : "Simulando python components Ui para o BGE_2.79b",
    "warning"       : "",
    "wiki_url"      : "",
    "category"      : "Game Engine",
    }


#-------------------------------------------------------------------------------
from bpy.types import Panel, Object, Operator
from bpy.props import StringProperty, IntProperty, FloatProperty, BoolProperty
from bpy.utils import register_module, unregister_module


import bpy
import sys
import types
from pprint import pprint, pformat
from ast import literal_eval
import ast 
import webbrowser


from contextlib import contextmanager
from os import path
from weakref import ref


from .component_base import KX_PythonComponent
from .common import (load_component_class, 
					 path_to_list, list_to_path, 
					 ARG_PROPERTY_NAME, COMPONENTS_NAME,
                     COMPONENT_PATHS_NAME
                     )




#-----------------------------------------------------------------------
MAINLOOP_FILE_NAME  = "mainloop.py"
REQUIRED_FILE_NAMES = "component_base.py", "common.py", "component_system.py", "components.py" , "NewComp.py" , "infor_components.py" , "link.py", MAINLOOP_FILE_NAME

ADDON_DIR           = path.dirname(__file__)



#-----------------------------------------------------


@contextmanager
def guard_modules():
    modules = set(sys.modules)
    yield
    for mod_name in set(sys.modules) - modules:
        del sys.modules[mod_name]

def prop_type_from_value(value):
    type_map = {str: 'STRING', int: 'INT', float: 'FLOAT', bool: 'BOOL' }
    return type_map[type(value)]


def get_prefixed_properties(properties, prefix):
    return [p for p in properties if p.name.startswith(prefix)]
    pass


class LOGIC_OT_add_component(Operator):
    """Add component to object"""
    bl_idname = "logic.component_add"
    bl_label = "Add Game Component"

    NO_IMPORT_PATH = "<NO PATH>"
    import_path = StringProperty(default=NO_IMPORT_PATH)
    

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        obj = context.active_object

        import_path = self.import_path
        if import_path == self.NO_IMPORT_PATH:
            import_path = obj.component_import_path

        # Fake import
        with guard_modules():
            # Create BGE module
            bge = sys.modules['bge'] = types.ModuleType("bge")
            bge.types = sys.modules['bge.types'] = types.ModuleType("bge.types")
            bge.types.KX_PythonComponent = KX_PythonComponent

            try:
                component_cls = load_component_class(import_path)

            except (ImportError, AttributeError):
                return {'CANCELLED'}

        # Load args
        try:
            args = component_cls.args

        except AttributeError:
            args = {}

        properties = obj.game.properties

        try:
            component_paths_prop = properties[COMPONENT_PATHS_NAME]

        except KeyError:
            bpy.ops.object.game_property_new(type='STRING', name=COMPONENT_PATHS_NAME)
            component_paths_prop = properties[COMPONENT_PATHS_NAME]

        component_paths = path_to_list(component_paths_prop.value)

        if import_path in component_paths:
            return {'CANCELLED'}

        component_paths.append(import_path)
        component_paths_prop.value = list_to_path(component_paths)

        for name, default_value in args.items():

            prop_name = ARG_PROPERTY_NAME.format(import_path=import_path, class_name=name)
            prop_type = prop_type_from_value(default_value)
            bpy.ops.object.game_property_new( type = prop_type, name = prop_name)

            prop = properties[prop_name]
            prop.value = default_value




        return {'FINISHED'}

class LOGIC_OT_remove_component(Operator):
    """Remove component from object"""
    bl_idname = "logic.component_remove"
    bl_label = "Remove Game Component"

    import_path = StringProperty()

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        obj = context.active_object
        properties = obj.game.properties
        import_path = self.import_path

        if not import_path:
            return {'CANCELLED'}

        if COMPONENT_PATHS_NAME in properties:
            component_paths_prop = properties[COMPONENT_PATHS_NAME]
            component_paths = path_to_list(component_paths_prop.value)
            component_paths.remove(import_path)
            component_paths_prop.value = list_to_path(component_paths)

        arg_properties = get_prefixed_properties(properties, import_path)
        for prop in arg_properties:
            index = properties.find(prop.name)
            if index == -1:
                continue

            bpy.ops.object.game_property_remove(index=index)

        return {'FINISHED'}


class LOGIC_OT_reload_component(Operator):
    """Reload component from disk"""
    bl_idname = "logic.component_reload"
    bl_label  = "Reload Game Component"

    import_path = StringProperty()

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        obj = context.active_object
        properties = obj.game.properties
        import_path = self.import_path

        if not import_path:
            return {'CANCELLED'}

        # Remove component
        bpy.ops.logic.component_remove(import_path=import_path)

        # Add component
        bpy.ops.logic.component_add(import_path=import_path)

        return {'FINISHED'}



#-------------------------------------------------------

def loadDataList( path_file ):
    data = None

    with open( path_file , 'r' ) as load_file:
        data        = load_file.read()
        load_data   = literal_eval(data) 
       
        return load_data



def loadFilesInformationComponents(self, context):
    obj               = context.active_object
    file_list_informs = "infor_components.py"


    if "infor_components.py" in bpy.data.texts:
        txt        = bpy.data.texts[ file_list_informs ].as_string()

        #fil_path_  = ADDON_DIR + "/database/" + "names.txt"
        #file_t     = loadDataList( path_file = fil_path_  )

        firstLine  = txt.split("\n")[0]
        firstLine2 = txt.split("\n")

        
        for tx in firstLine2:
            self.layout.label(tx)

            


    pass


def link_documentations(self, context):
    obj               = context.active_object

    if "link.py" in bpy.data.texts:
        txt        = bpy.data.texts[ "link.py" ].as_string()

        firstLine  = txt.split("\n")[0]
        firstLine2 = txt.split("\n")


        for tx in firstLine2:
            #self.layout.label(tx)

            if tx.startswith( "link=" ):
                out_link = tx[5:]
                webbrowser.open( out_link )
           



# OPERADORES DE LAYOUTS DO ADDON , VISUAL !#
class DialogOperator( bpy.types.Operator):
    bl_idname = "object.dialog_operator"
    bl_label  = "Property Editor "

    def execute(self, context):
        wm  = context.window_manager
        key = wm.keys()

        wm.popup_menu( loadFilesInformationComponents , title = "information"  , icon='INFO') 

        return {'FINISHED'}


class LinkOperator( bpy.types.Operator):
    bl_idname = "object.link_operator"
    bl_label  = "Property Editor "

    def execute(self, context):
        wm  = context.window_manager
        key = wm.keys()

        link_documentations(self, context)
        return {'FINISHED'}


#-------------------------------------------------------


class LOGIC_PT_components(Panel):
    bl_space_type   = 'VIEW_3D'
    bl_region_type  = 'TOOLS'
    #bl_context      = "object"
    bl_label        = 'Components_GameLogic'
    list_props      = [] 
    
    bpy.types.Object.components_show_box = bpy.props.BoolProperty( name= "ShowComponentBox" , default=True)
    ojt = bpy.types.Object
    bj  = ojt.components_show_box 
    


    # Não esta em uso por algun problemas 
    def setIcones(self , arg_name ):
        new_icon = "NONE"
        new_name = ""

        icons = bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items.keys()

        for index_keys , keys_name in enumerate( icons ):
            if arg_name.startswith( keys_name ):
                if keys_name in icons:
                    new_icon = keys_name

        return new_icon

        pass


    @classmethod
    def poll(cls, context):
        ob = context.active_object
        return ob and ob.name



    def draw(self, context):
        new_icon = "NONE"
        layout   = self.layout
        scene    = context.scene

        ob       = context.active_object
        game     = ob.game
        st       = context.space_data
        

        row     = layout.row()

        row.label( text="" , icon = 'FILE_SCRIPT')
        row.prop( ob , "component_import_path", text="")
        row.operator("logic.component_add", text="Add Component" , icon='NEW' )


        if not COMPONENT_PATHS_NAME in game.properties:
            return

        component_paths_prop = game.properties[COMPONENT_PATHS_NAME]
        component_paths      = path_to_list(component_paths_prop.value)


        for index_num , import_path in enumerate( component_paths ):
            row     = layout.row()
            col     = row.column()
            #col.separator()  
            pie     = col.column(True)
            col3    = pie.box().column()
            row2    = col3.row()
            #--------
            sa      = import_path.replace( "." , " , " )
            sf      = sa.rsplit(", ")



            
            row2.label( text = sf[1], icon='FILE_SCRIPT' )
            row2.label( text = str( ob.name ), icon = 'OBJECT_DATA')
            
            row2.operator("logic.component_reload" , text="" , icon ='RECOVER_LAST', emboss = True).import_path = import_path
            row2.operator("logic.component_remove" , text="" , icon ='X', emboss = True ).import_path = import_path
            row2.prop( ob , "components_show_box"  , text="", icon=["TRIA_RIGHT","TRIA_DOWN"][ ob.components_show_box], emboss=True)
            



            #-----v
            if ob.components_show_box:
                prop_prefix = "{}.".format(import_path)

                for prop in game.properties:
                    if not prop.name.startswith(prop_prefix):
                        continue

                    pie2          = col3.box().column()
                    row           = pie2.row()
                    row_infor_butoton = pie2.row()


                    arg_name      = prop.name[len(prop_prefix):]
                    new_icon      = self.setIcones( arg_name = arg_name )
                    str_icon_name = str( new_icon )

                    simb = [ "@@" , "@L" , "@"]

                    if arg_name.startswith( simb[0] ):
                        row.label( arg_name.replace( simb[0] , "" ) , icon = "QUESTION" )
                        row.operator("object.dialog_operator" , text="" , icon ='QUESTION', emboss = True )


                    elif arg_name.startswith( simb[1] ):
                        str_link = arg_name.replace( simb[1] , "" )

                        row.label( arg_name.replace( simb[1] , "" ) , icon = "FILE_TEXT" )
                        row.operator( "object.link_operator" , text="" , icon ='FILE_TEXT', emboss = True )



                    else:
                        if not arg_name.startswith( simb[2] ):
                            row.label( "" , icon = "LINK" )
                            row.label( arg_name.replace( new_icon , "" ) ) #, icon = str( new_icon ) )
                            row.prop(  prop , "value", text = "" )
                            

                        else:
                            row.label( arg_name.replace( simb[2] , "" ) , icon = "NLA_PUSHDOWN" )
                           
                                

                


class PersistantHandler:

    @classmethod
    def tag_class(cls, func):
        func._class = cls
        return func

    @classmethod
    def find_from_tag(cls, funcs):
        for func in funcs:
            if not hasattr(func, "_class"):
                continue

            if func._class is cls:
                return func

        raise ValueError

    @classmethod
    def install(cls, *args, **kwargs):
        instance = cls(*args, **kwargs)

        @bpy.app.handlers.persistent
        @cls.tag_class
        def update(scene):
            instance.update(scene)

        bpy.app.handlers.scene_update_post.append(update)

    @classmethod
    def uninstall(cls):
        handlers = bpy.app.handlers.scene_update_post
        handler  = cls.find_from_tag(handlers)
        handlers.remove(handler)

class TextblockMonitor(PersistantHandler):

    def __init__(self, required_file_names):
        self._required_file_names = required_file_names

    def update(self, scene):
        for file_name in self._required_file_names:
            if not file_name in bpy.data.texts:
                text_block = bpy.data.texts.new(file_name)


                with open(path.join(ADDON_DIR, file_name), 'r') as f:
                    text_block.from_string(f.read())

class ScenePropMonitor(PersistantHandler):

    def __init__(self, mainloop_file_name):
        self._mainloop_file_name = mainloop_file_name

    def update(self, scene):
        scene['__main__'] = self._mainloop_file_name
      

def register():
    register_module(__name__)
    
    Object.component_import_path  = StringProperty()

    TextblockMonitor.install(REQUIRED_FILE_NAMES)
    ScenePropMonitor.install(MAINLOOP_FILE_NAME)



def unregister():
    ScenePropMonitor.uninstall()
    TextblockMonitor.uninstall()

  
    del Object.component_import_path
    unregister_module(__name__)


if __name__ == "__main__":
    register()
