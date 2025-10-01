pangram="The quick brown fox jumps over the lazy dog"
letter=sorted(pangram)
print(letter)

numbers=[2.3,4.5,8.7,3.1,9.2,1.6]
numbers_sorted=sorted(numbers)
print(numbers_sorted)
print(numbers)

numbers.sort()
print(numbers)

literal="hello world"
sorted_literal=sorted(literal)  
print(sorted_literal)

missing_letter=sorted("The quick brown fox jumps over the lay dog",key=str.casefold)
print(missing_letter)

names=["Graham",
       "John",
       "terry",
       "eric",
       "Terry",
       "michael"]

names.sort(key=str.casefold);
print(names)


