import string

def cipher(key, user_input, e_or_d):
  # converts all inputs to numeric representations of inputs until the end of calculations.
  master_a_to_z = string.ascii_uppercase
  letter_to_number = {i:x for x,i in enumerate(master_a_to_z)}
  print(letter_to_number)

  # create dictionaries and variables that help convert letters into their numeric positions in the alphabet
  key = [letter_to_number[i] for i in key.upper()]
  print('key, converted to # of shifts: ', key)
  key_length = len(key)
  print('key length:', key_length)

  # handles exceptions in the case of a space in the input
  user_input = [letter_to_number[i] if i!=' ' else i for i in user_input.upper()]
  print('userinputs, converted to alphabetical position: ', user_input)

  # converts letters to their cyphered counterparts in numeric position form
  output = ''
  for input_position, alphabet_position in enumerate(user_input):
    if alphabet_position==' ':
      output = output + alphabet_position
      continue
    print('letter number:', input_position)
    shifts_due_to_key = key[input_position%key_length]
    print('shifts_due_to_key', shifts_due_to_key)

    # changes the equation depending on whether we want to decrypt or encrypt
    if e_or_d.upper() == 'E':
      output_letter_alphabet = master_a_to_z[(alphabet_position+shifts_due_to_key)%len(master_a_to_z)]
    else:
      output_letter_alphabet = master_a_to_z[(alphabet_position-shifts_due_to_key)%len(master_a_to_z)]
    # output_letter_alphabet = eval('master_a_to_z[(alphabet_position{}shifts_due_to_key)%len(master_a_to_z)]'.format('+'if e_or_d.upper() == 'E' else '-'))


    # creates the output string
    output = output + output_letter_alphabet
  return output

def generator_cipher(key, user_input, e_or_d):
  # converts all inputs to numeric representations of inputs until the end of calculations.
  master_a_to_z = string.ascii_uppercase
  letter_to_number = {i:x for x,i in enumerate(master_a_to_z)}
  print(letter_to_number)

  # create dictionaries and variables that help convert letters into their numeric positions in the alphabet
  key = [letter_to_number[i] for i in key.upper()]
  print('key, converted to # of shifts: ', key)
  key_length = len(key)
  print('key length:', key_length)

  # handles exceptions in the case of a space in the input
  user_input = [letter_to_number[i] if i!=' ' else i for i in user_input.upper()]
  print('userinputs, converted to alphabetical position: ', user_input)

  # converts letters to their cyphered counterparts in numeric position form
  output = ''
  for input_position, alphabet_position in enumerate(user_input):
    if alphabet_position==' ':
      output = output + alphabet_position
      continue
    print('letter number:', input_position)
    shifts_due_to_key = key[input_position%key_length]
    print('shifts_due_to_key', shifts_due_to_key)

    # changes the equation depending on whether we want to decrypt or encrypt
    if e_or_d.upper() == 'E':
      final_alphabet_position = (alphabet_position+shifts_due_to_key)%len(master_a_to_z)
      output_letter_alphabet = master_a_to_z[final_alphabet_position]
    else:
      final_alphabet_position = (alphabet_position-shifts_due_to_key)%len(master_a_to_z)
      output_letter_alphabet = master_a_to_z[final_alphabet_position]
    # output_letter_alphabet = eval('master_a_to_z[(alphabet_position{}shifts_due_to_key)%len(master_a_to_z)]'.format('+'if e_or_d.upper() == 'E' else '-'))


    # yield the output string (one character)
    yield (output_letter_alphabet, 
           [alphabet_position, 
            shifts_due_to_key, 
            final_alphabet_position,
            e_or_d])
  
# prompts the user for inputs
decrypt_or_encrypt = input('decrypt or encrypt, d/e: ')
if decrypt_or_encrypt == 'd':
  user_input = input('input_plaintext: ')
  key = input('key: ' )
elif decrypt_or_encrypt == 'e':
  user_input = input('input_ciphertext: ')
  key = input('key: ' )
print(cipher(key, user_input, decrypt_or_encrypt))
