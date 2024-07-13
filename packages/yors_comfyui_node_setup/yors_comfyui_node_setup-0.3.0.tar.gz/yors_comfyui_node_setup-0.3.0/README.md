<div align="center">
  <h1>yors_comfyui_node_setup</h1>
  <p>
    <strong>🤖 A python library for setup comfyui custom nodes for developers in development.</strong>
  </p>
  
  ![PyPI - Version](https://img.shields.io/pypi/v/yors_comfyui_node_setup)
  ![PyPI - License](https://img.shields.io/pypi/l/yors_comfyui_node_setup)

</div>

to setup comfyui custom nodes for developers in development:

- install requriements automatically for nodes
- entry - export comfyui node vars automatically

## 1 - install python package

```bash
pip install yors_comfyui_node_setup
# yors_comfyui_node_util
```

## 2 - use it in your python code

- in some comfyui custom nodes project or module

- code in `__init__.py`

```py
#
# from ...utils import entry,node_install_requirements # local
from yors_comfyui_node_setup import entry,node_install_requirements # global

# install requirements
node_install_requirements(__file__)

# export comfyui node vars
__all__,NODE_CLASS_MAPPINGS,NODE_DISPLAY_NAME_MAPPINGS,NODE_MENU_NAMES = entry(__name__,__file__)

#
```

## 3 - code yours nodes

- dirs map of your node may be:

```
.
└─__init__.py
└─nodes.py
```

- in any py file (no test in `__init__.py`)
- code nodes.py

```py
class AnyType(str):
  """A special class that is always equal in not equal comparisons. Credit to pythongosssss"""

  def __ne__(self, __value: object) -> bool:
    return False

any_type = AnyType("*")


CURRENT_CATEGORY="YMC/LINK" # set the right mouse button menu (custom for your comfyui nodes)
CURRENT_FUNCTION="exec"

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
    # set NODE_NAME and NODE_DESC for yors_comfyui_node_setup
    NODE_NAME = "as image"
    NODE_DESC = "set it as image type"
    # OUTPUT_NODE = True
    # OUTPUT_IS_LIST = (True,)
    def exec(self, a=None):
        return (a,)
```

## Author

ymc-github <ymc.github@gmail.com>

## License

MIT
