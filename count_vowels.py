vowels = 'aeiou'
sentance = 'Life is better when you\'re having fun.'
sentance = sentance.lower()
print('\n\nsentance: ',sentance)
count = 0
for char in sentance:
    if char in vowels:
        count +=1
    else:
        pass

print("Total number of vowels in the sentance : ",count,'\n')