kho = {
    'hp' : 20,
    'dell' : 50,
    'macbook' : 12,
    'asus' : 30
}
#7
for i, a in kho.items():
    print(i, a, sep = ": ")
print()
#8
print(sum(kho.values()))
#9
kho['FUJISU '] = 15
kho['ALIENWARE'] = 5
#10
for i, a in kho.items():
    print(i, a, sep = " : ")
print()

print(sum(kho.values()))