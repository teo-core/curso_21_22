# https://www.codewars.com/kata/5650ab06d11d675371000003/train/python
"""
The aim of this kata is to split a given string into different strings 
of equal size (note size of strings is passed to the method)

Example:

Split the below string into other strings of size #3

'supercalifragilisticexpialidocious'

Will return a new string
'sup erc ali fra gil ist ice xpi ali doc iou s'
"""

def split_in_parts(s, part_length): 
    salida = []
    for i in range(0,len(s),part_length):
        salida.append(s[i:i+part_length])
    return ' '.join(salida)

print(split_in_parts("supercalifragilisticexpialidocious", 3))
#"sup erc ali fra gil ist ice xpi ali doc iou s"

