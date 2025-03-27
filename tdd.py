def hex_to_base64(hex_string):
   try:
       byte_data = bytes.fromhex(hex_string)
   except ValueError:
       raise ValueError("Invalid Input")
       
   base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
   base64_string = []

   for i in range(0, len(byte_data), 3):
        chunk = byte_data[i:i+3]
        binary_str = ''.join(f'{byte:08b}' for byte in chunk)
        binary_str = binary_str.ljust((len(binary_str) + 5) // 6 * 6, '0')

        for j in range(0, len(binary_str), 6):
            index = int(binary_str[j:j+6], 2)
            base64_string.append(base64_chars[index])
        
   padding_length = (3 - len(byte_data) % 3) % 3
   base64_string.extend('=' * padding_length)
        
   return ''.join(base64_string)