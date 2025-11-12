#for num in range(1,11):
 #   if num==7:
  #      continue;
   # print(num)

prod_prices=[99,199,299,399,500,599,699,799]
i=0
while i<=len(prod_prices)-1:
    if prod_prices[i]==500:
        continue;
    print(prod_prices[i])
    i=i+1;