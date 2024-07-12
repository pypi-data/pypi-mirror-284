#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git | 
#========================================================================================================================================

from evo_framework import *
from evo_package_root.entity import *

#<
from evo_package_firebase.utility.UFirebaseApi import UFirebaseApi
#>
# ---------------------------------------------------------------------------------------------------------------------------------------
# URootApi
# ---------------------------------------------------------------------------------------------------------------------------------------
"""URootApi
"""
class URootApi():
    __instance = None
# ---------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):   
        if URootApi.__instance != None:
            raise Exception("ERROR:SINGLETON")
        else:
            super().__init__()
            URootApi.__instance = self
            self.currentPath = os.path.dirname(os.path.abspath(__file__))
            self.mapEApiConfig:EvoMap = EvoMap()
            
# ---------------------------------------------------------------------------------------------------------------------------------------
    """getInstance Singleton

    Raises:
        Exception:  api exception

    Returns:
        _type_: URootApi instance
    """
    @staticmethod
    def getInstance():
        if URootApi.__instance is None:
            uObject = URootApi()  
            uObject.doInit()  
        return URootApi.__instance
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
    async def doOnSet(self, eApiConfig:EApiConfig) -> EApiText :
        try:
            if eApiConfig is None:
                raise Exception("ERROR_REQUIRED|eApiConfig|")

#<        
            IuLog.doDebug(__name__, f"eConfig:{eApiConfig}")

            idSha256 = IuCryptHash.toSha256Bytes(eApiConfig.publicKey)
            
            if idSha256 != eApiConfig.id:
                raise Exception("ERROR_NOT_VALID_ID")
            
            id = eApiConfig.id.hex() 
            
            eApiconfigID = f"cyborgai://{id}"
           
            data=eApiConfig.toBytes()
           
            await UFirebaseApi.getInstance().doSet(collection=EApiConfig.VERSION, iD=id, data=data, isEncrypt=False)
            self.mapEApiConfig.doSet(eApiConfig)
   
            eApiText = EApiText()
            eApiText.doGenerateID()
            eApiText.text=eApiconfigID
            
            yield eApiText
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnGet(self, eApiQuery:EApiQuery) -> EApiConfig :
        try:
            if eApiQuery is None:
                raise Exception("ERROR_REQUIRED|eApiQuery|")

#<        
            #Add other check
            
            if IuText.StringEmpty(eApiQuery.eObjectID) :
                raise Exception("ERROR_REQUIRED|eRootInput.eApiconfigID|")
            
            id = IuConvert.fromHex(eApiQuery.eObjectID)
            if id in self.mapEApiConfig.keys():
                eApiConfig:EApiConfig = self.mapEApiConfig.doGet(id)
            else:
                data = await UFirebaseApi.getInstance().doGet(collection=EApiConfig.VERSION, id=eApiQuery.eObjectID)
                eApiConfig = IuApi.toEObject(EApiConfig(), data)
                self.mapEApiConfig.doGet(eApiConfig)

            yield eApiConfig
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------

#<
#OTHER METHODS ...
#>
# ---------------------------------------------------------------------------------------------------------------------------------------
