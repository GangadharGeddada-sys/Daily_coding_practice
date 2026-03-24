amount=int(input().strip())
discount=0
if(amount<1000):
    discount=amount*(5/100)
elif(amount>=1000 and amount<5000):
    discount=amount*(10/100)
elif(amount>=5000):
    discount=amount*(15/100)
result=amount-discount
print(f"{result:.2f}")