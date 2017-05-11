Q: Describe an theta(nlgn) algorithm that, given a set S of n integers and another integer x, determines if there exist two elements in S
whose sum is exactly x

Ans:
 
1. Sort the numbers with merge sort: theta(nlgn)
2. Begin with the 1st number i, using the binary search algorithm to find x-i: theta(lgn)
3. Repeat the 2nd step till the last number: n*theta(lgn)
Overall it takes theta(nlgn)
