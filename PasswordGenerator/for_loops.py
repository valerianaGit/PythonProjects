fruits = ["apple", "pear", "peach"]
#for fruit in fruits:
    #print(fruits)

#====================================================================================Gauss problem sum all numbers from 1 to 100 
#==================================================================================== using gauss system
higher_numbers = []
for n in range(51, 101):
    higher_numbers.append(n)
print(higher_numbers)
higher_numbers.reverse()
print(higher_numbers) 
summation_list = []
for n in range(1, 51):
    summation_list.append(n + higher_numbers[n - 1])
summation_count = len(summation_list)
summation = summation_list[1]
print("summation is ",summation)
print("summation count is ",summation_count)
gauss_findings = summation * summation_count
print(gauss_findings)
#==================================================================================== using computer magic
x = 0 
for n in range(1,101):
    x+=n
print(x)
