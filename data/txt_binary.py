def text_to_binary(text):
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary



def binary_to_text (binary):
    only_binary = ''.join(bit for bit in binary if bit in '01')
    text = ''.join(chr(int(only_binary[i:i+8], 2)) for i in range(0, len(only_binary), 8))
    return text



