print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

harf = "abcdefghij"
sayi = "0123456789"

# for i in harf:
#     for j in sayi:
#         list1 = (j+i)
#         print(list1, end="")
# for j in sayi:
#     for i in harf:
#         list2 = (i+j)

#veya asagidaki sekilde yapabiliriz.


list1 = [(j+i) for j in sayi for i in harf]
print("First list is :\n", list1, end="\n\n")

list2 = [(i+j) for i in harf for j in sayi]
print("Second list is :\n", list2, end="")