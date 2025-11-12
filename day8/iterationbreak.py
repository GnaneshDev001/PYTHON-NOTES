prod_prices=[99,199,299,399,499,599,699,799] #list supports
for price in prod_prices:
    if (price>300):
        break;
    print(price)

#while loop

i=0;
while i<=len(prod_prices)-1:
    if prod_prices[i]>500:
        break;
    print(prod_prices[i])
    i=i+1
#########################################
pr=(1,2,3,4,5,6) #tuple supports
for p in pr:
    if(p>4):
        break;
    print(p)

i=0;
while i<len(pr)-1:
    if(pr[i]>3):
        break;
    print(pr[i])
    i=i+1
###################################################
dic=[{12,13,14,15,16}] #dict not support
for di in dic:
    if(di>15):
        break;
    print(di)
 