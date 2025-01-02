import time,functions.fib as fib, functions.loop as loop

number = int(input("What fibonnaci would you like to calculate? "))

start = time.time()
print(f"The fibonacci sequence of {number} is: {fib.memo_fib(number)}")
end = time.time()

total_time = end - start

if(total_time >= 1):
    print (f"The time it took for this operation was {total_time} s.")
else:
    print (f"The time it took for this operation was {(total_time) * 1000} ms.")
    
loop.loop(9)
loop.list_loop(10)
    


    

