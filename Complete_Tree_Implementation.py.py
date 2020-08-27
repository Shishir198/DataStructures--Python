def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


d,parts = map(int,input().split())
hour_per_day = d//parts
# print("hours per day" , hour_per_day)
res = 0

for i in range(1,hour_per_day+1):
    if is_prime(i):
        # print("i",i)
        count=0
        for x in range(1,parts):
            if is_prime(i+(x)*hour_per_day):
                # print("i+hrday",i+(x)*hour_per_day)
                count+=1
            # print("count",count)
        if count==parts-1:
            res+=1


print(res)

