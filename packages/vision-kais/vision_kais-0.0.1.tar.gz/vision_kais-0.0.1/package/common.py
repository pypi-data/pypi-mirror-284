""" Vision System interface - common.
 
 
@author:    kais, misil.
@created:   2024-07-03
"""

import xhost
# import requests
 

class com:
    idx: int = 8
    currnet : int = 0
    valueList: list = ['x', 'y', 'z', 'rx', 'ry', 'rz']
    delimiter: str = ','
    
class cmd:
    # VISOR Control
    TRR = "TRR"     # Trigger Robotics
    
    # VISOR Job settings
    SPP = "SPP"     # Set Parameter
    
    # VISOR calibration
    CCD = "CCD"     # Initialization
    CAI = "CAI"     # Add image
    CRP = "CRP"     # Robotics multi-image
    
    TRR_default: str = "TRR104Part0"
    CAI_default: str = "CAI120001020"
    CRP_default: str = "CRP1140"
    SPP_default: str = "SPP001030000013"
    SPP_default_res: str = "SPP001035000480"
    
    fail:str = "Fail"
    calibStart_return: str = "CalibReady"
    calibX_return: str = "Next"
    calibEnd_return: str = "Complete"
    
    
    @staticmethod
    def GetSPPT(key):
        # signed(정수), unsigned(음수)
        if key == "SI08":
            return "SignedInteger08"
        elif key == "UI08":
             return "UnsignedInteger08"
        elif key == "SI16":
            return "SignedInteger16"
        elif key == "UI16":
             return "UnsignedInteger16"
        elif key == "SI32":
            return "SignedInteger32"
        elif key == "UI32":
            return "UnsignedInteger32"
        elif key == "SI40":
            return "SignedInteger40"
        elif key == "UI40":
            return "UnsignedInteger40"
        elif key == "FLOT":
            return "Float"
        elif key == "DOBL":
            return "Double"
        elif key == "STRG":
            return "String"
        elif key == "BOOL":
            return "Boolean"
        elif key == "SP08":
            return "SpecialSigned8"
        elif key == "UDEF":
            return "Undefined"
        elif key == "IARR":
            return "IntegerArray"
        elif key == "ZERO":
            return "DefaultZeroParameter"
        



def res_api(path: str, query: dict):
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = path
    query_parameter = query
    response = {'nsync': 0, '_type': 'Pose', 'rx': 0.0, 'x': 1067.366, 'ry': 73.248, 'y': -12.859, 'rz': -0.69, 'z': 1609.909, 'mechinfo': 1, 'crd': 'base', 'j1': 0.0, 'j2': 0.0, 'j3': 0.0, 'j4': 0.0, 'j5': 0.0, 'j6': 0.0}
    # response = requests.get(url = base_url + path_parameter, params = query_parameter).json()
    return response

 
def logd(text: str):
    print(text)
    xhost.printh(text)