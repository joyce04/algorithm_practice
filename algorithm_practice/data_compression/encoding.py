# USE TRIE for encoding dictionary and INCLUDE comments
# possile alphabet = [a-zA-Z0-9?! ,.;:\n]

# encoding
# use arary format trie similar to aho-corasick implementation
# total number of possible alphabets is 70 -> default dictionary is size of 70
# With char dictionary, each column of each char can be found by char itself as index


import sys
import struct

def read_file(file_name):
    # read input file
    data = ''
    try:
        with open(file_name, 'r') as f:
            data = ''.join(f.readlines())
    except:
        print("Unexpected error while reading input file:", sys.exc_info()[0])
    
    return data

def get_default_trie(data):
    # possible alphabets = [a-zA-Z0-9 !?,.;:\n]
    pos_chars = [i for i in range(ord('a'), ord('z')+1)] + [i for i in range(ord('A'), ord('Z')+1)] + [i for i in range(ord('0'), ord('9')+1)] + [ord('!'), ord('?'), ord(' '), ord(','), ord('.'), ord(':'), ord(';'), ord('\n')]
    available_char_dict = {}
    for i, c in enumerate(pos_chars):
        available_char_dict[chr(c)] = i

    # initialize each cell with -1 to compare whether the given pattern does exist in the dictionary
    default_trie = [[-1]*70 for _ in range(len(data))]
    return default_trie, available_char_dict


def encoding(data):
     # build default trie and char dictionary
    trie, char_dic = get_default_trie(data)
    out = []

    present_state = 0
    data_state = 1

    for i in range(len(data)):#c in data:
        c = data[i]
        char = char_dic[c]
        # if there is no matching char in the trie
        if trie[present_state][char] == -1:
            trie[present_state][char] = data_state
            out.append((present_state, c))

            # reset for search
            present_state = 0
            data_state += 1
        # if matching prefix char exists in the trie
        else:
            present_state = trie[present_state][char]
            
    # if pattern exists in the trie
    if present_state >0:
        out.append((present_state, ''))
            
    return out

def compress(origin_file, compressed_file):

    data = read_file(origin_file)
    encoded_data = encoding(data)

    with open(compressed_file, 'wb') as compressed_file:
        for i, (idx, ch) in enumerate(encoded_data):
            save_char = ch.encode() if len(ch) > 0 else b'\x00'
            
            # when sequence is less than 256 (2^8 = 1 byte)
            # 2 byte = 1 byte of idx and 1 byte of ascii code for char
            if i <= 255:
                data = struct.pack('Bc', idx, save_char)
                compressed_file.write(data) 
            # when sequence is less than 65536 ((2^8)^2 = 2 byte)
            # 3 byte = 2 byte of idx and 1 byte of ascii code for char
            elif i <= 65535:
                data = struct.pack('Hc', idx, save_char)
                compressed_file.write(data) 
            # when sequence is less than 16777216 (((2^8)^2)^2 = 2 byte)
            # 4 byte = 3 byte of idx and 1 byte of ascii code for char
            elif i <= 16777215:
                data = struct.pack('Ic', idx, save_char)
                compressed_file.write(b''.join([data[0:3], data[4:]])) 
            # when sequence is greater than 16777216 (((2^8)^2)^2 = 2 byte)
            # 5 byte = 4 byte of idx and 1 byte of ascii code for char
            else:
                data = struct.pack('Ic', idx, save_char)
                compressed_file.write(data)            

# check if all necessary files are given
if len(sys.argv) != 3:
    print("Usage : python3 encoding.py <input_file> <output_file>")
    exit(1)

compress(sys.argv[1], sys.argv[2])