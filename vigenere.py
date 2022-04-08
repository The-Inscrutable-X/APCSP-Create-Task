import string

def encrypt(key, user_input, e_or_d):
  # we should convert all inputs to numeric representations of inputs until the end of calculations.
  master_a_to_z = string.ascii_uppercase
  letter_to_number = {i:x for x,i in enumerate(master_a_to_z)}
  print(letter_to_number)
  
  key = [letter_to_number[i] for i in key.upper()]
  print('key, converted to # of shifts: ', key)
  key_length = len(key)
  print('key length:', key_length)

  user_input = [letter_to_number[i] if i!=' ' else i for i in user_input.upper()]
  print('userinputs, converted to alphabetical position: ', user_input)

  output = ''
  for input_position, alphabet_position in enumerate(user_input):
    if alphabet_position==' ':
      output = output + alphabet_position
      continue
    print('letter number:', input_position)
    shifts_due_to_key = key[input_position%key_length]
    print('shifts_due_to_key', shifts_due_to_key)
    
    output_letter_alphabet = eval('master_a_to_z[(alphabet_position{}shifts_due_to_key)%len(master_a_to_z)]'.format('+'if e_or_d.upper() == 'E' else '-'))
    
    output = output + output_letter_alphabet
  return output

    

decrypt_or_encrypt = input('decrypt or encrypt, d/e: ')
if decrypt_or_encrypt == 'd':
  user_input = input('input_plaintext: ')
elif decrypt_or_encrypt == 'e':
  user_input = input('input_ciphertext: ')
  key = input('key: ' )
print(encrypt(key, user_input, decrypt_or_encrypt))