def trick_or_treat(candies,children):
    total = candies - children
    if candies > children:
        return 'treat', total
    else:
        return 'trick!!!!', 0
    
candy = int(input("How many candies you have? "))
child = int(input("How many children? "))

result = trick_or_treat(candy,child)
print(result[0])
print(f"You have {result[1]} canides left")


# trick_or_treat(1 -2 3 5 0)