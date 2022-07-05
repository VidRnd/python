price = [57.08, 46.51, 97, 5, 12.7,966,42.00,25.12,85,78.01,89.27,2,5,8.90,50.33, 88.55,47]
print(', '.join(map(str,price)))
for i in price:
    ruzult = str(float(i)).split ( "." )
    rubles = ruzult[0]
    kopecks = ruzult[1]
    if int(kopecks) == 0:
        kopecks = "00"
    elif len(kopecks) == 1:
        kopecks = kopecks + "0"
    print(""+str(rubles)+" руб " +str(kopecks) + " коп")

print(id(price))
price.sort()
print(', '.join(map(str,price)))
print(id(price))
price.sort(reverse=True)
print(price)
price_new_list = price[:]
print(id(price_new_list))
print(price_new_list[:4])
