Q: Can we improve the worst-case running time of isnertion sort to theta(nlgn) by using binary search when finding the place to insert?

Ans: No, we cannot. Even A[1..j-1] is already sorted, and it only takes (nlg) to find the place to insert, insertin the item A[j] requires
shifting on average j/2 items forward by one. For an array, this still takes theta(j) time. So we didn't save any time compared with 
the linear search version.
