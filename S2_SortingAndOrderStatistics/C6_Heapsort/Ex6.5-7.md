Ans:

For Stack, we use a max priority queue; for Queue, we use a min PQ, or use a max priority queue with decreasing keys. Take Stack as an example.

1.  We can have a (key, value) tuple stored at each node, where key is the priority, which equals the order at which the item arrives to Stack.

  To push, we increase the key, then insert (key, val) to hq. This requires modification to the MaxPriorityQueue class because it expects a key in the node, not a tuple.

  To pop, we extract the tuple from the priority, then extract the value from the tuple.

2. Alternatively, we can use a dictionary, where key is the order that item arrives, and the value is the item itself. To pop, we extract the key, then use the key to find out the value. This doesn't require modification to the MaxPriorityQueue class, but it's cumbersome.

3. We can also push item to an array, then insert the index of that item to the pq. 
