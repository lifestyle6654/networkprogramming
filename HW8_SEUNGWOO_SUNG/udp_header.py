import socket
import struct
import binascii

class Udphdr:
    def __init__(self, src_port, dst_port, len, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.len = len
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!HHHH', self.src_port, self.dst_port, self.len, self.checksum)
        return packed

def unpack_Udphdr(buffer): # 언팩하여 표현
    unpacked = struct.unpack('!HHHH', buffer[:8])
    return unpacked

def getSrcPort(unpacked_Udpheader): 
    return unpacked_Udpheader[0]

def getDstPort(unpacked_Udpheader): 
    return unpacked_Udpheader[1]

def getLength(unpacked_Udpheader): 
    return unpacked_Udpheader[2]

def getChecksum(unpacked_Udpheader):
    return unpacked_Udpheader[3]
    

udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_Udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_Udphdr))

unpacked_Udphdr = unpack_Udphdr(packed_Udphdr)
print(unpacked_Udphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'\
.format(getSrcPort(unpacked_Udphdr), getDstPort(unpacked_Udphdr), getLength(unpacked_Udphdr), getChecksum(unpacked_Udphdr)))