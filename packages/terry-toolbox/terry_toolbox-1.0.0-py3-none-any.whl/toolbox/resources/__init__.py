# %%
from toolbox import get_directory
from pathlib import Path
from pprint import pprint
from enum import Enum
from typing import Dict

RESOURCE_PATH = get_directory(__file__)

ROBOT_PATH = RESOURCE_PATH / 'assets/robots'
MANAGERIE_PATH = RESOURCE_PATH / 'assets/mujoco_menagerie'


    
class ASSET_SRC(Enum):
    CUSTOM = 0
    MENAGERIE = 1

def get_asset_dict(TYPE=ASSET_SRC.CUSTOM, XML=True)->Dict[str, Path]:
    if TYPE is ASSET_SRC.CUSTOM:
        path = ROBOT_PATH
    elif TYPE is ASSET_SRC.MENAGERIE:
        path = MANAGERIE_PATH
    else:
        raise ValueError(f"Unknown asset type {TYPE}")
    
    if XML:
        xml_dict = {}
        for name in path.glob('**/*.xml'):
            if name.stem == 'scene':
                continue
            xml_dict[name.stem] = name
            
            xml_scene = name.parent / 'scene.xml'
            if xml_scene.is_file():
                xml_dict['scene_'+name.stem] = xml_scene
        
        
        pprint(xml_dict)
        return xml_dict
    else:
        urdf_dict = {}
        for name in path.glob('**/*.urdf'):
            urdf_dict[name.name] = name
        pprint(urdf_dict)
        return urdf_dict

    # asset_path = dict(xml=xml_dict, urdf=urdf_dict)
    # print(f"Available assets for {name}:")
    # pprint(asset_path)
    # return asset_path


# %%
if __name__ == '__main__':
    # get_asset_dict(ASSET_SRC.CUSTOM)
    get_asset_dict(ASSET_SRC.MENAGERIE)
    
    
# %%
