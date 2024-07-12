#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git | 
#========================================================================================================================================

from evo_framework.core import *
from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_type.entity.EvoMap import EvoMap
from evo_framework.core.evo_core_log.utility.IuLog import IuLog
from evo_framework.core.evo_core_api.entity.EApiConfig import EApiConfig
from evo_framework.core.evo_core_key.utility.IuKey import IuKey
from evo_framework.core.evo_core_crypto.utility.IuCryptEC import IuCryptEC
from evo_framework.core.evo_core_crypto.utility.IuCryptHash import IuCryptHash
from evo_framework.core.evo_core_log.utility.IuLog import IuLog
from evo_framework.core.evo_core_system.utility.IuSystem import IuSystem
from evo_framework.core.evo_core_convert.utility.IuConvert import IuConvert
from evo_framework.core.evo_core_setting.control.CSetting import CSetting
from evo_framework.core.evo_core_log.utility.IuLog import IuLog
from evo_framework.core.evo_core_api.entity.EActionTask import EActionTask
from evo_framework.core.evo_core_api.entity.ERequestInfo import ERequestInfo
from evo_framework.core.evo_core_api.entity.EApi import EApi
from evo_framework.core.evo_core_api.entity.EAction import EAction
from evo_framework.core.evo_core_api.entity.EnumApiAction import EnumApiAction
from evo_framework.core.evo_core_api.entity.EnumApiCrypto import EnumApiCrypto
from evo_framework.core.evo_core_api.entity.EnumApiCompress import EnumApiCompress
from evo_framework.core.evo_core_api.entity.EnumApiType import EnumApiType
from evo_framework.core.evo_core_api.entity.EnumApiVisibility import EnumApiVisibility
from evo_framework.core.evo_core_setting.utility.IuSettings import IuSettings
from evo_framework.core.evo_core_totp.utility.IuTotp import IuTotp
from evo_framework.core.evo_core_api.utility.IuApi import IuApi
from evo_framework.core.evo_core_file.utility.IuFile import IuFile
from evo_framework.core.evo_core_api.utility.IuApiRequest import IuApiRequest

import requests


#<

#>
# ---------------------------------------------------------------------------------------------------------------------------------------
# UApiClient
# ---------------------------------------------------------------------------------------------------------------------------------------
"""UApiClient
"""
class UApiClient():
    __instance = None
# ---------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):   
        if UApiClient.__instance != None:
            raise Exception("ERROR:SINGLETON")
        else:
            super().__init__()
            UApiClient.__instance = self
            self.currentPath = os.path.dirname(os.path.abspath(__file__))
            self.__url_server = "https://cyborgai-api.fly.dev"
            self.__pk_server = "1de18b4372c9aff7e0b893ded10baea4a20d4352612e6883d1623a0b105d8bb5591ceab0818838fd82752dca9454df963cc37407e173a258ee700f3e4bcde2ff"  # pinning
            self.__api_set = "admin_add_node"
            self.__api_get = "admin_get_node"
            #self.__url_cyborgai = f"{ self.__url_server}/v2/set_node/"
            
# ---------------------------------------------------------------------------------------------------------------------------------------
    """getInstance Singleton

    Raises:
        Exception:  api exception

    Returns:
        _type_: UApiClient instance
    """
    @staticmethod
    def getInstance():
        if UApiClient.__instance is None:
            uObject = UApiClient()  
            uObject.doInit()  
        return UApiClient.__instance
# ---------------------------------------------------------------------------------------------------------------------------------------
    """doInit

    Raises:
        Exception: api exception

    Returns:

    """   
    def doInit(self):   
        try:
#<
            #INIT ...
            pass
#>   
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doSetPeer(self, eApiConfig:EApiConfig)  :
        try:
            if eApiConfig is None:
                raise Exception("ERROR_REQUIRED|eApiConfig|")

#<        
          
            
            
            #yield eChatMessage
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------

#<
#OTHER METHODS ...
#>
# ---------------------------------------------------------------------------------------------------------------------------------------
