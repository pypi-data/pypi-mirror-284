#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation	https://github.com/cyborg-ai-git # 
#========================================================================================================================================

from evo_framework.entity.EObject import EObject
import struct
#========================================================================================================================================
"""EHeader

    EHeader represents the structure for making requests within the EVO framework for bridge communication.
    
"""
class EHeader(EObject):
    _struct_format = '<32sqiiii'
    _header_size = struct.calcsize(_struct_format)
    
    def __init__(self):
        super().__init__()
        #self.id: bytes = b'\x00' * 32
        #self.time: int = 0
        self.offsetStart: int = 0
        self.offsetEnd: int = 0
        self.data: bytes = None
        self.length: int = 0

    def toBytes(self) -> bytes:
       
        data = self.data if self.data else b''
       
        
      
        data_length = len(data) if data else -1
       

       
        header_data = struct.pack(self._struct_format, 
                                  self.id, 
                                  self.time, 
                                  self.offsetStart, 
                                  self.offsetEnd, 
                                  data_length,
                                  self.length
                                  )
        return header_data + data 

    def fromBytes(self, packed_data: bytes):
        header = packed_data[:self._header_size]
        (self.id, 
         self.time,
         self.offsetStart, 
         self.offsetEnd,
         data_length,
        self.length) = struct.unpack(self._struct_format, header)
        
        offset = self._header_size

        if data_length > 0:
            self.data = packed_data[offset:offset + data_length]
            
    def __str__(self) -> str:
        strReturn = "\n".join([
                super().__str__(),      
                f"\toffsetStart: {self.offsetStart}",
                f"\toffsetEnd: {self.offsetEnd}",
                f"\tdata length :{len(self.data) if self.data else 'None'}",
                f"\tlength :{self.length}",
                    ]) 
        return strReturn