# import asyncio
import os
# import json
# import shutil
# import inspect
# import aiohttp
# from server import PromptServer
# from tqdm import tqdm
import sys
import re
# import folder_paths
import importlib

import subprocess
config = None

# code(core): pyio_read_dirs_name - read dirs name in some location
def pyio_read_dirs_name(loc:str):
    """
    read dirs name in some location
    """

    files_file = [
        f for f in os.listdir(loc) if os.path.isdir(os.path.join(loc, f))
    ]
    return files_file

# code(core): pyio_read_file_name - read file name in some location
def pyio_read_file_name(loc:str):
    """
    read file name in some location
    """
    files_file = [
        f for f in os.listdir(loc) if os.path.isfile(os.path.join(loc, f))
    ]
    return files_file

# code(core): pyio_read_module_name - read python module name in some location
def pyio_read_module_name(loc:str,ignore_list:list[str]=["__pycache__"]):
    """
    read module name in some location
    """

    dirs_name = pyio_read_dirs_name(loc)
    # docs(core): ignore name in ignore_list
    dirs_name = [x for x in dirs_name if x not in ignore_list]

    return dirs_name

# code(core): list_ignore_them - list ignore them
def list_ignore_them(namelist:list,them:list=[]):
    """
    name list ignore some
    """

    dirs_name = [x for x in namelist if x not in them]
    return dirs_name

# code(core): get_sys_module - read python module in sys in name
def get_sys_module(name:str):
    """
    get_sys_module(__name__)
    """
    return sys.modules[name]

# code(core): get_classes_in_module - read class list in python module
def get_classes_in_module(module):
    """
    get_classes_in_module(sys.modules[__name__])

    for cls in all_classes:
    
        print(cls.__name__)
    """
    classes = []
    for name in dir(module):
        member = getattr(module, name)
        if isinstance(member, type):
            classes.append(member)
    return classes

# code(core): std_stro_name - std name in stro
def std_stro_name(name):
    """
    std_stro_name('YMC/MASK//  mask ') # 'YMC/MASK/ mask'
    """
    stded = re.sub(r'-+', "-",name)
    stded = re.sub(r' +', " ",stded)
    stded = re.sub(r'/+', "/",stded)
    stded = stded.strip()
    return stded

# code(core): std_module_name - std name for module
def std_module_name(name):
    """
    std_module_name('YMC/MASK//  mask ') # 'YMC/MASK//_mask_'

    std_module_name('YMC/MASK//  mask ') # 'YMC_MASK_mask' # tpdo
    """
    stded = re.sub(r'-+', "_",name)
    stded = re.sub(r' +', "_",stded)
    stded = re.sub(r'_+', "_",stded)
    stded = stded.strip()
    return stded

# code(core): import_custom_node_module - import custom node in some location

def import_custom_node_module(root_path:str,root_name:str,sub_name="modules"):
    """
    import_custom_node_module(os.path.dirname(__file__),__name__,"modules")
    """
    # root_path=os.path.dirname(__file__)
    dirs_name = pyio_read_module_name(os.path.join(root_path,sub_name),["__pycache__"])
    for node_name in dirs_name:
        # print(node_name)
        rel_name=".".join(['',sub_name,node_name])
        # print(rel_name)
        importlib.import_module(rel_name, package=root_name)

# code(core): read_module_class_name - read class name in some python package
def read_module_class_name(name:str):
    YMC_CLASSS_NAME=[]
    print(f"[info] read name in sys.modules if name including {name} (loaded)")
    
    for key,value in sys.modules.items():
        # print(key)
        if name in key :
            # """do nothing"""
            # print(key)
            YMC_CLASSS_NAME.append(key)
    return YMC_CLASSS_NAME

# code(core): read_module_valid_node_class - read class name in some python package and do valid filter
def read_module_valid_node_class(name):
    # print(f"[info] read class name if key in sys.modules including {__name__}")
    # docs(core): print class name if key in sys.modules including this module name
    ValidNodeClassList=[]
    ALL_CLASS_NAMES=[]
    for key,value in sys.modules.items():
        if name in key :
            # print(key)
            # docs(core): get all classes in name module
            module = sys.modules[key]
            all_classes = get_classes_in_module(module)
            for cls in all_classes:
                # dup class name
                if cls.__name__ not in ALL_CLASS_NAMES:
                    ALL_CLASS_NAMES.append(cls.__name__)
                    # print(cls.__name__)
                    if hasattr(cls,"NODE_DESC"):
                        ValidNodeClassList.append(cls)
                # print name of them
                # print(cls.__name__)

                # collect class that match ymc style - has attr NODE_DESC in class
                # if hasattr(cls,"NODE_DESC"):
                #     if cls not in ValidNodeClassList:
                #         ValidNodeClassList.append(cls)
    return ValidNodeClassList,ALL_CLASS_NAMES

# code(core): make_module_valid_node_class_map - make node class map for valid node module
def make_module_valid_node_class_map(NodeClassList:list,infoname:bool=False):
    """
    NODE_CLASS_MAPPINGS,NODE_DISPLAY_NAME_MAPPINGS,NODE_MENU_NAMES  = make_module_valid_node_class_map(all_classes,False)
    """
    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {}
    NODE_MENU_NAMES=[]     
    for cls in NodeClassList:
        # print name of them
        # print(cls.__name__)

        # docs(core): only register node when NODE_DESC in class
        if hasattr(cls,"NODE_DESC"):
            # docs(core): stdify CATEGORY in class and CATEGORY in class
            CURRENT_PREFIX = std_stro_name(cls.CATEGORY)
            CURRENT_TOPIC = std_stro_name(cls.NODE_DESC)
            # docs(core): make menu name with NODE_DESC,CATEGORY
            menu_name = f'{CURRENT_PREFIX}/{CURRENT_TOPIC}'

            # docs(core): plan to use node_name in 2.0.0
            node_name =  std_stro_name(cls.NODE_NAME) if hasattr(cls,"NODE_NAME") else ""
            if node_name is not None | node_name not in [""]:
                menu_name =  f'{CURRENT_PREFIX}/{node_name}'
            # docs(core): print repeated node name
           
            if  NODE_DISPLAY_NAME_MAPPINGS.get(menu_name,None) is not None:
                print(f'node name {menu_name} is repeat!')
            # docs(core): print menu name
            # if infoname ==True:
            if infoname:
                print(menu_name)
            NODE_MENU_NAMES.append(menu_name)
            NODE_CLASS_MAPPINGS[menu_name]=cls
            NODE_DISPLAY_NAME_MAPPINGS[menu_name]=CURRENT_TOPIC
    return NODE_CLASS_MAPPINGS,NODE_DISPLAY_NAME_MAPPINGS,NODE_MENU_NAMES

# code(core): import_py_file - import py file
def import_py_file(fileloc:str,rootname=None):
    """
    import_py_file(__file__,None)

    import_py_file(__file__,".")

    import_py_file(__file__,".YmcNodeArtComfyui")
    """
    root_path = os.path.dirname(fileloc)
    root_name= os.path.split(root_path)[-1]
    if rootname is not None:
        root_name=".".join([rootname,root_name])
    print(root_name)
    filename_list = pyio_read_file_name(root_path)
    # print(filename_list)
    filename_list = list_ignore_them(filename_list,["__init__.py"])
    # ignore when space in name
    filename_list = [x for x in filename_list if x.find(" ") == -1]
    # print(filename_list)
    for filename in filename_list:
        name = os.path.splitext(filename)[0]
        # rel_name=".".join(['',name])
        # importlib.import_module(rel_name, package=root_name)
        # importlib.import_module(rel_name)
        importlib.import_module(name)
    return filename_list

# code(core): read_py_file_name - read py file
def read_py_file_name(fileloc:str):
    """
    read_py_file_name(__file__)
    """
    root_path = os.path.dirname(fileloc)
    # root_name= os.path.split(root_path)[-1]
    filename_list = pyio_read_file_name(root_path)
    filename_list = list_ignore_them(filename_list,["__init__.py"])
    filename_list = [x for x in filename_list if x.find(" ") == -1]
    names=[]
    for filename in filename_list:
        name = os.path.splitext(filename)[0]
        names.append(name)
    return filename_list

# code(core): make_all_import - make __all__ for comfyui node
# code(core): ignore __init__.py 
def make_all_import(location:str):
    """
    __all__= make_all_import(__file__)
    """
    all_py_file=[]
    root_path=os.path.dirname(location)
    for fileanme in os.listdir(root_path):
        if fileanme == '__init__.py' or fileanme[-3:] != '.py':
            continue
        goodname=fileanme[:-3]
        all_py_file.append(goodname)
        # importlib.import_module(goodname)
        # importlib.import_module(os.path.join(root_path,goodname))
        # importlib.import_module(os.path.join(root_path,fileanme))
    return all_py_file

# code(core): get_all_modulename_of_x_in_sys - get all name of x in sys
def get_all_modulename_of_x_in_sys(x):
    """
    get_all_modulename_of_x_in_sys(__name__)
    """
    all_names_of_x=[]
    for key,value in sys.modules.items():
        # if 'ymc' in key:
        #     print(key)
        if x in key and x != key:
            # print(key)
            all_names_of_x.append(key)
    return all_names_of_x

# code(core): get_all_module_of_x_in_sys - get all module of x in sys
def get_all_module_of_x_in_sys(x):
    """
    get_all_module_of_x_in_sys(__name__)
    """
    all_module_of_x=[]
    for key,value in sys.modules.items():
        # if 'ymc' in key:
        #     print(key)
        if x in key and x != key:
            # print(key)
            all_module_of_x.append(value)
    return all_module_of_x


NODE_LOADING_DEBUG=True
def debug_print(msg):
    # if NODE_LOADING_DEBUG == True:
    if NODE_LOADING_DEBUG:
        print(msg)
    return msg
    
# code(core): entry_prepare_import - make __all__ with name and file location

def entry_prepare_import(name:str,file:str,infoimport=None,):
    """
    __all__ = entry_prepare_import(__name__,__file__,infoimport)


    __all__ = entry_prepare_import(name,file,infoimport)
    """
    global NODE_LOADING_DEBUG
    NODE_LOADING_DEBUG=NODE_LOADING_DEBUG if infoimport is None else infoimport
    
    # debug_print(f'[init] {__file__} do:')
    debug_print(f'[init] {name} do:')

    debug_print(f'[info] this module file in {file}')

    debug_print('[info] import utils from parent file')

    debug_print('[info] define __all__ with utils.make_all_import')
    # docs(core): define what it need to import in __all__
    __all__= make_all_import(file)
    return __all__

# code(core): entry_prepare_import - prepare import for comfyui node
def entry_do_after_import(name:str,file:str,infoimport=None,):
    """
    NODE_CLASS_MAPPINGS,NODE_DISPLAY_NAME_MAPPINGS,NODE_MENU_NAMES  = entry_do_after_import(__name__,__file__,infoimport)


    NODE_CLASS_MAPPINGS,NODE_DISPLAY_NAME_MAPPINGS,NODE_MENU_NAMES  = entry_do_after_import(name,file,infoimport)
    """
    global NODE_LOADING_DEBUG
    NODE_LOADING_DEBUG=NODE_LOADING_DEBUG if infoimport is None else infoimport
    
    debug_print('[info] get all module name of this module in sys')
    this_module_all_name= get_all_modulename_of_x_in_sys(name)
    # debug_print(f'[info] get all module of this module in sys')
    # this_module_all= get_all_module_of_x_in_sys(__name__)

    debug_print('[info] get all classes of this module in this module')
    all_classes=[]
    # for x in __all__:
    #     cl = get_classes_in_module(sys.modules[".".join([__name__,x])])
    #     all_classes.extend(cl)

    for x in this_module_all_name:
        # debug_print(x)
        # cl = get_classes_in_module(sys.modules[x])
        cl = get_classes_in_module(get_sys_module(x))
        all_classes.extend(cl)

    debug_print('[info] make valid node class map of this module')
    NODE_CLASS_MAPPINGS,NODE_DISPLAY_NAME_MAPPINGS,NODE_MENU_NAMES  = make_module_valid_node_class_map(all_classes,False)
    # debug_print(f'[init] {__file__} done.')

    debug_print(f'[init] {name} done.')

    return NODE_CLASS_MAPPINGS,NODE_DISPLAY_NAME_MAPPINGS,NODE_MENU_NAMES

# code(core): entry - make entry vars for comfyui node
def entry(name,file,infoimport=None,):
    """
    __all__,NODE_CLASS_MAPPINGS,NODE_DISPLAY_NAME_MAPPINGS,NODE_MENU_NAMES = entry(__name__,__file__)
    """
    global __all__

    global NODE_LOADING_DEBUG
    NODE_LOADING_DEBUG=NODE_LOADING_DEBUG if infoimport is None else infoimport
    
    __all__ = entry_prepare_import(name,file,infoimport)

    debug_print('[info] import __all__ with from . import * ')

    # docs(core): automatically import
    # from . import * 
    for x in __all__:
        importlib.import_module(".".join([name,x]))

    NODE_CLASS_MAPPINGS,NODE_DISPLAY_NAME_MAPPINGS,NODE_MENU_NAMES = entry_do_after_import(name,file,infoimport)

    return __all__,NODE_CLASS_MAPPINGS,NODE_DISPLAY_NAME_MAPPINGS,NODE_MENU_NAMES

# code(core): pyio_install_requirements - install requirements in file location
def pyio_install_requirements(file):
    """
    piio_install_requirements(Path(__file__).parent / "requirements.txt")

    piio_install_requirements(os.path.join(os.path.dirname(__file__),"requirements.txt"))
    """
    # code based on custom_nodes/ComfyUI-Frame-Interpolation/install.py
    s_param = '-s' if "python_embeded" in sys.executable else '' 
    if not os.path.isfile(file):
        # print('file does not exist.')
        """
        do nothing
        """
    else:
        with open(file, 'r') as f:

            for package in f.readlines():
                package = package.strip()
                if package != "":
                    print(f"installing {package}...")
                    os.system(f'"{sys.executable}" {s_param} -m pip install {package}')

# docs(core): you can install package in requirements.txt with utils.node_install_requirements

# code(core): node_install_requirements - install requirements in dir and file name
def node_install_requirements(location,name="requirements.txt"):
    """

    node_install_requirements(__file__,"requirements.txt"))
    """
    # code based on custom_nodes/ComfyUI-Frame-Interpolation/install.py
    file = os.path.join(os.path.dirname(location),name)
    # pyio_install_requirements(file)
    spio_install_requirements(file)


# code base on:
# custom_nodes\masquerade-nodes-comfyui\MaskNodes.py
package_list = None
# docs(core): support install package in your node if you need with utils.ensure_package
def update_package_list():
    
    global package_list
    package_list = [r.decode().split('==')[0] for r in subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).split()]

# code(core): ensure_package - install some python package  if not installed
def ensure_package(package_name, import_path=None):
    """
    ensure_package("qrcode")

    ensure_package("clipseg", "clipseg@git+https://github.com/timojl/clipseg.git@bbc86cfbb7e6a47fb6dae47ba01d3e1c2d6158b0")
    """
    global package_list
    if import_path is None:
        import_path = package_name
    if package_list is None:
        update_package_list()

    if package_name not in package_list:
        print("(First Run) Installing missing package %s" % package_name)
        subprocess.check_call([sys.executable, '-m', 'pip', '-q', 'install', import_path])
        # s_param = '-s' if "python_embeded" in sys.executable else '' 
        # os.system(f'"{sys.executable}" {s_param} -m pip install {import_path}')
        update_package_list()

# code(core): spio_install_requirements - install some python package in file location if not installed
def spio_install_requirements(file):
    """
    spio_install_requirements(Path(__file__).parent / "requirements.txt")

    spio_install_requirements(os.path.join(os.path.dirname(__file__),"requirements.txt"))
    """
    if not os.path.isfile(file):
        """
        do nothing
        """
    else:
        with open(file, 'r') as f:
            for package in f.readlines():
                package = package.strip()
                if package != "":
                    package_name = package.split('==')[0]
                    ensure_package(package_name)

