import re

txt = "@why(692,996)[&}}^where(81,407)mul(247,89):[&[{<mul(980,958),?mul(529,895)!<#~!$&~when()+mul(519,986)what())#mul(710,934)%??*'!<mul(813,338)! +$what()<don't(){^mul(396,693)mul(337,541)}what()*<](@?~mul(64,644)[where()who()~,))mul(528,450)!' -do()who()#]where():(mul(909,368)mul(259,743)'"
txt = open('03input').read()
x = re.findall( r'(mul\(\d+,\d+\))', txt)
# print(x)
def multi(str):
    a, b = map(int, re.findall(r'\d+', str))
    # print(a,b)
    return a*b

products = [multi(item) for item in x]
# print(products)
print(sum(products))


# Part 2

y = re.findall( r'(don\'t\(\)|do\(\)|mul\(\d+,\d+\))', txt)
print(y)
final = []
skip = False
for it in y:
    if it == 'do()':
        skip = False
    elif it == 'don\'t()':
        skip = True
    elif not skip:
        final.append(multi(it))
print(final)
print(sum(final))