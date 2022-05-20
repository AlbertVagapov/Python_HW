# RLE алгоритм сжатия


# Str = 'AAAAAAAABBBXXXTNNNOOO'
file = 'DZ2_number4.txt'
with open(file, 'r') as Str:
    List = [i for i in Str.read()]
# print(List)
Str_rle = ''
a = List[0]
k = 0
for i in range(len(List)):    
    if List[i] == a: 
        k += 1
    else:
        Str_rle += (f'{k}{a}')
        a = List[i]
        k = 1
Str_rle += (f'{k}{List[len(List)-1]}')
print(Str_rle)
file2 = 'DZ2_number4.2.txt'
with open(file2, 'w') as data:
    data.write(Str_rle)