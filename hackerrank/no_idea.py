''' There is an array of n integers. There are also 2 disjoint sets, A and B , each containing m integers.
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0.
For each i integer in the array, if i (element) A, you add 1 to your happiness. If i (element) B, you add -1 to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  A and B  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints
1<=n<=10**5
1<=m<=10**5
1<= Any integer in the input <=10**9

Input Format

The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
Explanation

You gain 1 unit of happiness for elements 3 and 1 in set A. You lose 1 unit for 5 in set B.
The element 7 in set B does not exist in the array so it is not included in the calculation.

Hence, the total happiness is 2-1 = 1. '''

n, m = (input("Enter TWO numbers n (number of elements in array) and m (number of elements in each set)")).split()
input_array = (input("Enter numbers for the array " + n + " numbers")).split()
set_A = (input("Enter numbers for set A " + m + " numbers")).split()
set_B = (input("Enter numbers for set B " + m + " numbers")).split()

happiness = 0

for i in range(len(set_A)):
    for j in range(len(input_array)):
        if set_A[i] == input_array[j]:
            happiness += 1

for i in range(len(set_B)):
    for j in range(len(input_array)):
        if set_B[i] == input_array[j]:
            happiness -= 1

print("Happiness is", happiness)
