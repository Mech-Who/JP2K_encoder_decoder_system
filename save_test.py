import sys
import struct
import pickle
from pathlib import Path
from src.core.utils import get_correct_size

SAVE_ROOT = Path('./img/save_test')

string = "01010101"
bstring = b"01010101"
data_size = sys.getsizeof(string)
value, unit = get_correct_size(data_size)
print(f"string: {value=:.2f} {unit}")

data_size = sys.getsizeof(bstring)
value, unit = get_correct_size(data_size)
print(f"bstring: {value=:.2f} {unit}")

data = string.encode('utf-8')
data_size = sys.getsizeof(data)
value, unit = get_correct_size(data_size)
print(f"data: {value=:.2f} {unit}")

with open(SAVE_ROOT/"test1.png", "wb")as f:
    f.write(data)

with open(SAVE_ROOT/"test2.png", "wb")as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

bdata = struct.pack("I", 1)
data_size = sys.getsizeof(bdata)
value, unit = get_correct_size(data_size)
print(f"bdata: {value=:.2f} {unit}")

string = "01010101"*1024*5

byte_string = int(string, 2).to_bytes((len(string) + 7) // 8, byteorder='big')
data_size = sys.getsizeof(byte_string)
value, unit = get_correct_size(data_size)
print(f"byte_string: {value=:.2f} {unit} {len(byte_string)=}")
print(f"{len(byte_string)=}, {(len(string) + 7) // 8=}, {len(string)=}")

with open(SAVE_ROOT/"test3.png", "wb")as f:
    pickle.dump(byte_string, f, pickle.HIGHEST_PROTOCOL)

with open(SAVE_ROOT/"test4.png", "wb") as f:
    f.write(byte_string)

int_data = 500000

data = struct.pack("I", int_data)
data_size = sys.getsizeof(data)
value, unit = get_correct_size(data_size)
print(f"int_data: {value=:.2f} {unit} {len(data)=} {data=}")

data = int_data.to_bytes((int_data.bit_length() + 7) // 8, byteorder='little')
data_size = sys.getsizeof(data)
value, unit = get_correct_size(data_size)
print(f"int_data: {value=:.2f} {unit} {len(data)=} {data=}")
print(f"{(int_data.bit_length() + 7) // 8=}, {len(data)=}")

int_list = list(range(10))

bitstream = bytearray()
for num in int_list:
    data = num.to_bytes((num.bit_length()+7)//8, byteorder='big')
    length = struct.pack("I", len(data))
    bitstream += length
    bitstream += data
with open(SAVE_ROOT/"test5.png", "wb") as f:
    f.write(bitstream)

with open(SAVE_ROOT/"test5.png", "rb") as f:
    new_bitstream = f.read()

BYTE_LENGTH = 4
offset = 0
new_int_list = []
while offset < len(new_bitstream):
    length = struct.unpack_from('I', new_bitstream, offset)[0]
    offset += BYTE_LENGTH
    data = new_bitstream[offset:offset+length]
    offset += length
    num = int.from_bytes(data, byteorder='big')
    new_int_list.append(num)
print(f"{int_list=}, {new_int_list=}")

byte_str = ["0000100010101000", "1100101001101001", "0100010011010111"]
bitstream = bytearray()
for s in byte_str:
    data = int(s, 2).to_bytes((len(s)+7)//8, byteorder='big')
    bitstream += struct.pack("I", len(s))
    bitstream += struct.pack("I", len(data))
    bitstream += data

with open(SAVE_ROOT/"test6.png", "wb") as f:
    f.write(bitstream)
print(f"{len(bitstream)=}")

with open(SAVE_ROOT/"test6.png", "rb") as f:
    new_bitstream = f.read()

BYTE_LENGTH = 4
offset = 0
new_str_list = []
while offset < len(new_bitstream):
    print(f"{offset=}")
    str_length = struct.unpack_from('I', new_bitstream, offset)[0]
    offset += BYTE_LENGTH
    byte_length = struct.unpack_from('I', new_bitstream, offset)[0]
    offset += BYTE_LENGTH
    data = new_bitstream[offset:offset+byte_length]
    offset += byte_length
    binary_str = ''.join(format(byte, '08b') for byte in data)
    # 移除前导的多余位（如果有的话）,需要知道原始二进制字符串的长度
    binary_str = binary_str[:str_length]
    new_str_list.append(binary_str)
print(f"{byte_str}\n{new_str_list}")

def strbytes2bytes(str_data: str) -> bytearray:
    data = int(str_data,2).to_bytes((len(str_data)+7)//8, byteorder='big')
    bitstream = bytearray()
    bitstream += struct.pack("I", len(str_data))
    bitstream += struct.pack("I", len(data))
    bitstream += data
    return bitstream

def bytes2strbytes(byte_data: bytes) -> str:
    offset = 0
    BYTE_LENGTH = 4
    str_length = struct.unpack("I", byte_data, offset)[0]
    offset += BYTE_LENGTH
    data_length = struct.unpack("I", byte_data, offset)[0]
    offset += BYTE_LENGTH
    data = byte_data[offset:offset+data_length]
    offset += data_length
    data = ''.join(format(byte, '08b') for byte in data)
    data = data[:str_length]
    return data

import bitarray

bit_arr = bitarray.bitarray(byte_str[0])
print(f"{len(bit_arr)=}")
with open(SAVE_ROOT/"test7.png", "wb") as f:
    bit_arr.tofile(f)

new_bit_arr = bitarray.bitarray()
with open(SAVE_ROOT/"test7.png", "rb") as f:
    new_bit_arr.fromfile(f)
print(f"{len(new_bit_arr)=}")
data = new_bit_arr.to01()

print(f"{byte_str[0]}\n{data}")
