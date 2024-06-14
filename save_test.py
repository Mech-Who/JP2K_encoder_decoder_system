import sys
import struct
import pickle
from src.core.utils import get_correct_size

string = "01010101"*1024*5
bstring = b"01010101"*1024*5
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

with open("test1.png", "wb")as f:
    f.write(data)

with open("test2.png", "wb")as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

bdata = struct.pack("I", 1)
data_size = sys.getsizeof(bdata)
value, unit = get_correct_size(data_size)
print(f"bdata: {value=:.2f} {unit}")

string = "01010101"*1024*5

byte_string = int(string, 2).to_bytes((len(string) + 7) // 8, byteorder='big')
data_size = sys.getsizeof(byte_string)
value, unit = get_correct_size(data_size)
print(f"byte_string: {value=:.2f} {unit}")

with open("test3.png", "wb")as f:
    pickle.dump(byte_string, f, pickle.HIGHEST_PROTOCOL)

with open("test4.png", "wb") as f:
    f.write(byte_string)
