from random import choice
coin=["head","tail"]
head_count=0
for i in range(100):
    result=choice(coin)
    if result=="head":
        head_count=head_count+1
print("head count in 100 tosses:",head_count)
print("tail count in 100 tosses:",100-head_count)
