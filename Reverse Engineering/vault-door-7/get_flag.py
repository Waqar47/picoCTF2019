#let's do marjava

secret = [1096770097,1952395366,1600270708,1601398833,1716808014,1734305381,828716089,895562083]



def get_complete_blocks():
    temp = []
    
    for binary in secret:
        #binary = str(binary)[2:]
        binary = bin(binary)[2:]
        
        if len(binary) < 32:
            diff = 32 - len(binary)
            binary = ('0' * diff) + binary
            temp.append(binary)
        #print(binary + ' ' + str(len(str(binary)))) 
    return temp   
        
#IMPORTANT
get_complete_blocks()


def get_binary_char():
    temp = []
    
    for block in blocks8_per32bit:
        
        for div in range(0,len(block),8):
            #GET BINARY EQUIVALENT of each character
            temp.append(int(block[div:div+8],2))

    return temp
#def shift_bits():
    

def get_password():
    temp = []
    for block in blocks8_per32bit:
        
        for div in range(0,len(block),8):
            temp.append(chr(int(block[div:div+8],2)))
    
    return temp

    


#HINTS
#a = [0x41,0x5F,0x62,0x31,0x74,0x5F,0x30,0x66,0x5F,0x62,0x31,0x74,0x5F,0x73,0x68,0x31,0x66,0x54,0x69,0x4E,0x17,0x34,0x29,0x20,0x24,0x37,0x38,0x66,0x64,0x31,0x35,0x31,0x32]


blocks8_per32bit = get_complete_blocks()
password = get_password()
binary_per_char = get_binary_char()





print('picoCTF{%s}' % ''.join(password))




