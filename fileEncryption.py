file_hand=open('ex1.txt','rb')
data=file_hand.read()
bin_list=bytearray()
for char in data:
    xor_char= char ^ 8
    bin_list.append(xor_char)
file_hand=open('ex1.txt','wb')
file_hand.write(bin_list)




