num = int(input("Enter a number: "))
odd_results = 0
even_results = 0
for i in range(1,11):
    result = num * i
    if result % 2 == 0:
        is_even = "Even"
    else:
        is_even = "Odd"
    if is_even == "Even":
        even_results += 1
    else:
        odd_results += 1
    print(num,"x",i,"=",result,"-",is_even)
print("Even Results: ",even_results)
print("Odd Results: ",odd_results)
