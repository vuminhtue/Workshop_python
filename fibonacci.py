def fibo_range(n = 10):
    fibo_list = [0,1]
    for i in range(2,n):
        fibo_list.append(fibo_list[i-1]+fibo_list[i-2])
    return(fibo_list,fibo_list[n-1])
