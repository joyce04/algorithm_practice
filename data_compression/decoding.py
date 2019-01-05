import sys
import struct

def decoding(data):
    d_out = []
    for (n, c) in data:
        d_out.append(c if n == 0 else d_out[n-1] + c)
    return ''.join(d_out)


def decompress(compressed_file, decompressed_file):
        import struct 
        bin_file = open(compressed_file, 'rb')
        bin_type = {2: 'Bc', 3: 'Hc', 4: 'Ic', 5: 'Ic'}
        
        encoded_data = []
        seq = 0
        
        while True:
            # when sequence is less than 256 (2^8 = 1 byte)
            # 2 byte = 1 byte of idx and 1 byte of ascii code for char
            if seq <= 255:
                bin_size = 2
            # when sequence is less than 65536 ((2^8)^2 = 2 byte)
            # 3 byte = 2 byte of idx and 1 byte of ascii code for char
            elif seq <= 65535:
                bin_size = 3
            # when sequence is less than 16777216 (((2^8)^2)^2 = 2 byte)
            # 4 byte = 3 byte of idx and 1 byte of ascii code for char
            elif seq <= 16777215:
                bin_size = 4
            # when sequence is greater than 16777216 (((2^8)^2)^2 = 2 byte)
            # 5 byte = 4 byte of idx and 1 byte of ascii code for char
            else:
                bin_size = 5
            
            # read by bin_size determined by the sequence index
            binary = bin_file.read(bin_size)
            
            # check the end of the file
            if binary == b'': 
                break 
                
            # when bin_size 4, need to add \x00 as 4th byte because I've removed the last byte for compression
            if bin_size ==4:
                encoded_data.append(struct.unpack(bin_type[bin_size], b''.join([binary[0:3], b'\x00', binary[3:]])))
            else:
                encoded_data.append(struct.unpack(bin_type[bin_size], binary))
            
            seq += 1
        
        if encoded_data[-1][1] == b'\x00':
            encoded_data[-1] = (encoded_data[-1][0], b'')
            
        encoded_data = [(d[0], d[1].decode()) for d in encoded_data]
        decoded_data = decoding(encoded_data)
        
        with open(decompressed_file, 'w') as decompressed_file:
            decompressed_file.write(decoded_data)

# check if all necessary files are given
if len(sys.argv) != 3:
    print("Usage : python3 decoding.py <input_file> <output_file>")
    exit(1)

decompress(sys.argv[1], sys.argv[2])