def hex_to_base64(hex_string):
   byte_data = bytes.fromhex(hex_string)
   base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
   base64_string = ""

   for i in range(0, len(byte_data), 3):
        chunk = byte_data[i:i+3]
        binary_str = ''.join(f'{byte:08b}' for byte in chunk)

        while len(binary_str) % 6 != 0:
            binary_str += '0'

        for j in range(0, len(binary_str), 6):
            index = int(binary_str[j:j+6], 2)
            base64_string += base64_chars[index]
        
   return base64_string