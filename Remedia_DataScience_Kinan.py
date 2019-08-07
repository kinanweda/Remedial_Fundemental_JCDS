# #No.1
# def find_short(kata):
#     a= kata.split()
#     b = []
#     for item in a:
#         b.append(len(item))
#     b.sort()
#     print(b[0])
# find_short('Many People get up early in the morning')
# find_short('Every office would getting newest monitor')
# find_short('Create new file after this morning')
# #No.2
# def persistence(num):
#     angka = num
#     b = 0
#     while (angka>=10):
#         a = angka
#         string = str(a)
#         jumlah = 1
#         for item in range (len(string)):
#             jumlah *= int(string[item])
#         b += 1
#         angka = jumlah
#     print(b)
# persistence(39)
# persistence(999)
# persistence(4)
##No.3
# def multiplication_table(row,col):
#     lists=[1,2,3]
#     z=''
#     for item2 in range(row):
#         for item3 in range(col):
#             if item2 > item3:
#                 z+='{}'.format(lists[item3]*(item2+1))
#             else:
#                 z+='{}'.format(lists[item2]*(item3+1))
#         z+='\n'
#     print(z)
# multiplication_table(5,3)
# multiplication_table(3,3)
# multiplication_table(3,5)
# #No.4
# def alphabet_position(huruf):
#     dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
#     'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
#     'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'
#     }
#     lists = []
#     kata = huruf.lower()
#     for item in list(kata):
#         for idx, val in dict.items():
#             if idx == item:
#                 lists.append(val)
#     return ' '.join(lists)
# print(alphabet_position("The sunset sets at twelveo'clock"))
# print(alphabet_position("It's never too late to try"))
# print(alphabet_position("Have you done your homework"))
##No.Bonus
# def is_prime(nomor):
#     if nomor == 1:
#         prime = False
#     elif nomor == 2:
#         prime = True
#     elif nomor < 1:
#         prime = False    
#     else:
#         prime = True
#         for check_number in range(2, int(nomor/2)+1):
#             if nomor % check_number == 0:
#                 prime = False
#                 break
#     print(prime)
# is_prime(1)
# is_prime(2)
# is_prime(-1)
# is_prime(5099)

    
