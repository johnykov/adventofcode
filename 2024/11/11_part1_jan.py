
def solution(arr, blink):
    for i in range(blink):
        newarr=[]
        for j in range(len(arr)):
            if arr[j]=='0':
                newarr.append('1')
            elif len(arr[j])%2==0:
                mid = len(arr[j])//2
                newarr.append(arr[j][:mid])
                # if arr[j][mid:]=='0':
                #     newarr.append(1)
                newarr.append(f"{int(arr[j][mid:])}")
            else:
                newarr.append(f"{int(arr[j])*2024}")
        arr=newarr
        print(i,len(arr))
    return len(arr)


# print(solution(['0','1','10','99','999'],1))
# print(solution(open('./example').read().split(' '),6))
# print(solution(open('./input').read().split(' '),25))
print(solution(open('./input').read().split(' '),75))