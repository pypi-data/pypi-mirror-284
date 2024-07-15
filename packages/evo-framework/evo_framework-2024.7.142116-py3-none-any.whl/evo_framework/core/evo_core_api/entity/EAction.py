
import struct
class EActionStruct:
    __struct_format = '<iqiiiiii'
    __sizeHeader = struct.calcsize(__struct_format)
   
    def __init__(self):
        #super().__init__()  
        self.id:bytes = b''
        self.time:int = 0
        self.seek:int = 0
        self.pk:bytes = b''
        self.sign:bytes = b''
        self.input:bytes = b''
        self.output:bytes = b''
        self.length:int = -1
    
    def to_bytes(self): 
        header_data = struct.pack(
            self.__struct_format,
            len(self.id),
            self.time,
            self.seek,
            len(self.pk),
            len(self.sign),
            len(self.input),
            len(self.output),
            self.length
        )
        
        return header_data + self.id + self.pk + self.sign + self.input + self.output

    def from_bytes(self, packed_data):  
        [ 
        idLength,
        self.time,
        self.seek,
        pkLength,
        signLength,
        inputLength,
        outputLength,
        self.length         
        ] = struct.unpack(self.__struct_format, packed_data[:self.__sizeHeader])
        
        offset = self.__sizeHeader
        
        if idLength > 0:
            self.id = packed_data[offset:offset + idLength] 
            offset += idLength 
        
        if pkLength > 0:
            self.pk = packed_data[offset:offset + pkLength] 
            offset += pkLength 

        if signLength > 0:
            self.sign = packed_data[offset:offset + signLength] 
            offset += signLength 

        if inputLength > 0:
            self.input = packed_data[offset:offset + inputLength] 
            offset += inputLength 
        
        if outputLength > 0:
            self.output = packed_data[offset:offset + outputLength] 
  
        return self

    def __str__(self):
        return (f"id: {self.id}\n"
                f"time: {self.time}\n"
                f"seek: {self.seek}\n"
                f"pkLength: {len(self.pk)}\n"
                f"signLength: {len(self.sign)}\n"
                f"inputLength: {len(self.input)}\n"
                f"outputLength: {len(self.output)}\n"
                f"inputLength: {len(self.input)}\n"
                f"outputLength: {len(self.output)}\n"
                f"length: {self.length}\n")