import random
colour=['red','yellow','green','brown','blue','pink','black']
item=['dog','car','bike','tie','shirt','cat']
x=0
while x<10:
    x=x+1
    start='Your '
    sentence=start+random.choice(item)
    sentence=sentence+' is '+random.choice(colour)
    print(sentence)
    print(x)

    
