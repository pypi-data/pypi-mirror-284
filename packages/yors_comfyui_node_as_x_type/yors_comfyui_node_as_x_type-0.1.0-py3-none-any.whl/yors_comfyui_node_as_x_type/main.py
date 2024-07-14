# from ..ymcz_utils import any_type
# from .yors_comfyui_node_util import any_type

class AnyType(str):
  """A special class that is always equal in not equal comparisons. Credit to pythongosssss"""

  def __ne__(self, __value: object) -> bool:
    return False

any_type = AnyType("*")


CURRENT_CATEGORY="YMC/LINK"
CURRENT_FUNCTION="exec"

# feat(core): node to set it as any type
class NodeSetItAsAny:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {

            },
            "optional":{
                "a": (any_type),
            },
            # "hidden": {
            #     "unique_id": "UNIQUE_ID",
            #     "extra_pnginfo": "EXTRA_PNGINFO",
            # },
        }

    # INPUT_IS_LIST = True
    RETURN_TYPES = (any_type,)
    RETURN_NAMES = ("a",)
    
    FUNCTION = CURRENT_FUNCTION
    CATEGORY = CURRENT_CATEGORY
    NODE_NAME = "as any"
    NODE_DESC = "set it as any type"
    # OUTPUT_NODE = True
    # OUTPUT_IS_LIST = (True,)
    def exec(self, a=None):
        return (a,)
    
# feat(core): node to set it as image type
class NodeSetItAsImage:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {

            },
            "optional":{
                "a": (any_type),
            },
            # "hidden": {
            #     "unique_id": "UNIQUE_ID",
            #     "extra_pnginfo": "EXTRA_PNGINFO",
            # },
        }

    # INPUT_IS_LIST = True
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)

    FUNCTION = CURRENT_FUNCTION
    CATEGORY = CURRENT_CATEGORY
    NODE_NAME = "as image"
    NODE_DESC = "set it as image type"
    # OUTPUT_NODE = True
    # OUTPUT_IS_LIST = (True,)
    def exec(self, a=None):
        return (a,)

# feat(core): node to set it as model type    
class NodeSetItAsModel:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {

            },
            "optional":{
                "a": (any_type),
            },
            # "hidden": {
            #     "unique_id": "UNIQUE_ID",
            #     "extra_pnginfo": "EXTRA_PNGINFO",
            # },
        }

    # INPUT_IS_LIST = True
    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("model",)

    FUNCTION = CURRENT_FUNCTION
    CATEGORY = CURRENT_CATEGORY
    NODE_NAME = "as model"
    NODE_DESC = "set it as model type"
    # OUTPUT_NODE = True
    # OUTPUT_IS_LIST = (True,)
    def exec(self, a=None):
        return (a,)
      
# feat(core): node to set it as clip type
class NodeSetItAsClip(NodeSetItAsAny):
    RETURN_TYPES = ("CLIP",)
    RETURN_NAMES = ("clip",)

    FUNCTION = CURRENT_FUNCTION
    CATEGORY = CURRENT_CATEGORY
    NODE_NAME = "as clip"
    NODE_DESC = "set it as clip type"

# feat(core): node to set it as vae type
class NodeSetItAsVae(NodeSetItAsAny):
    RETURN_TYPES = ("VAE",)
    RETURN_NAMES = ("vae",)

    FUNCTION = CURRENT_FUNCTION
    CATEGORY = CURRENT_CATEGORY
    NODE_NAME = "as vae"
    NODE_DESC = "set it as vae type"

# feat(core): node to set it as conditioning type
class NodeSetItAsConditioning(NodeSetItAsAny):
    RETURN_TYPES = ("CONDITIONING",)
    RETURN_NAMES = ("Conditioning",)

    FUNCTION = CURRENT_FUNCTION
    CATEGORY = CURRENT_CATEGORY
    NODE_NAME = "as conditioning"
    NODE_DESC = "set it as conditioning type"

# feat(core): node to set it as latent type
class NodeSetItAsLatent(NodeSetItAsAny):
    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("Latent",)

    FUNCTION = CURRENT_FUNCTION
    CATEGORY = CURRENT_CATEGORY
    NODE_NAME = "as latent"
    NODE_DESC = "set it as latent type"

# feat(core): node to set it as string type
class NodeSetItAsString(NodeSetItAsAny):
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("String",)

    FUNCTION = CURRENT_FUNCTION
    CATEGORY = CURRENT_CATEGORY
    NODE_NAME = "as string"
    NODE_DESC = "set it as string type"

# feat(core): node to set it as int type
class NodeSetItAsInt(NodeSetItAsAny):
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("Int",)

    FUNCTION = CURRENT_FUNCTION
    CATEGORY = CURRENT_CATEGORY
    NODE_NAME = "as int"
    NODE_DESC = "set it as int type"

# feat(core): node to set it as float type
class NodeSetItAsFloat(NodeSetItAsAny):
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("Float",)

    FUNCTION = CURRENT_FUNCTION
    CATEGORY = CURRENT_CATEGORY
    NODE_NAME = "as float"
    NODE_DESC = "set it as float type"

# feat(core): node to set it as number type
class NodeSetItAsNumber(NodeSetItAsAny):
    RETURN_TYPES = ("NUMBER",)
    RETURN_NAMES = ("Number",)

    FUNCTION = CURRENT_FUNCTION
    CATEGORY = CURRENT_CATEGORY
    NODE_NAME = "as number"
    NODE_DESC = "set it as number type"


# def get_module(loc:str):
#   """
#   get_module(__name__)
#   """
#   import sys
#   return sys.modules[loc]

# # code(core): get_classes_in_module - read class list in python module
# def get_classes_in_module(module):
#     """
#     all_class_in_this_module = get_classes_in_module(sys.modules[__name__])
#     """
#     classes = []
#     for name in dir(module):
#         member = getattr(module, name)
#         if isinstance(member, type):
#             classes.append(member)
#     return classes

# def get_node_class(nc:list):
#     """
#     node_class_in_this_module=get_node_class(all_class_in_this_module)
#     """
#     ValidNodeClassList=[]
#     for cls in nc:
#         if hasattr(cls,"NODE_DESC"):
#             ValidNodeClassList.append(cls)
#     return ValidNodeClassList

# def set_node_class_category(nc:list,category:str):
#     """
#     set_node_class_category(node_class_in_this_module,"YMC/LINK")
#     """
#     for cls in nc:
#         if hasattr(cls,"CATEGORY"):
#             setattr(cls,"CATEGORY",category)

# def log_node_class(nc:list):
#     """
#     set_node_class_category(node_class_in_this_module,"YMC/LINK")
#     """
#     for cls in nc:
#         msg=''
#         if hasattr(cls,"CATEGORY"):
#             msg+=f'{cls.CATEGORY}/'
#         if hasattr(cls,"NODE_NAME"):
#             msg+=f'{cls.NODE_NAME}'
#         if hasattr(cls,"NODE_DESC"):
#             msg+=f' - {cls.NODE_DESC}'
#         print(msg)

# all_class_in_this_module = get_classes_in_module(get_module(__name__))
# # yors_comfyui_node_as_x_type
# # all_class_in_this_module = get_classes_in_module(nodes)
# node_class_in_this_module=get_node_class(all_class_in_this_module)
# log_node_class(node_class_in_this_module)
# set_node_class_category(node_class_in_this_module,"YMC/as_x_type")
# log_node_class(node_class_in_this_module)
# # print(__name__)
