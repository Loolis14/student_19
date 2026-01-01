*This project has been created as part of the 42 curriculum by mmeurer.*

## DESCRIPTION

This project involves writing a program that sorts data on a stack (actually a double-ended queue), with a limited set of instructions, using the lowest possible number of actions.

The set of allowed operations is:
- **Swap** : swap the first two elements of stack A, stack B or both;
- **Push** : push the first element of the stack and place it onto the other stack;
- **Rotate** : move the first element on the last position (stack A, stack B, or both);
- **Reverse rotate** : move the last element on the first position (stack A, stack B, or both);

To achieve a perfect score, the program must satisfy the following benchmarks:
- Sort 100 random numbers in fewer than 700 operations.
- Sort 500 random numbers in fewer than 5,500 opérations.



## TECHNICAL CHOICES

### Algorithm
I chose the **Turk algorithm** for sets with more than three numbers. It is efficient enough to obtain the maximum mark while keeping the code simple by not requiring different algorithms for different input sizes.

To understand how this algorithm works I read an [article from the author of the Turk algorithm](https://medium.com/@ayogun/push-swap-c1f5d2d41e97). 


### Data Structure
> [!IMPORTANT]
> To optimize data storage, I opted to implement the deque using a **circular array** instead of a doubly-linked list for several reasons:

- **Minimizes memory fragmentation:** With a linked list, each node requires a separate malloc, creating "holes" in the heap memory. An array is a single block. Additionally, managing fewer allocations reduces the risk of memory leaks.

- **Maximizes cache locality:** To process data, the CPU must first load it into the cache. With an array, the data is contiguous, meaning the CPU can load it efficiently. In contrast, linked list nodes are scattered in memory, resulting in expensive retrieval times.

- **O(1) Random Access:** Unlike linked lists, circular arrays allow direct access to any element via its index. No need to follow pointers.

- **It's cooler:** and, of course, I learned a lot from implementing this new concept.



## INSTRUCTIONS

### Compilation
- Generate the build files using the Makefile
```bash
make
```
- Run the binary with the numbers to sort
```bash
./push_swap
```

### Available input
I decided to implement number parsing considering all possible cases. 

The different input formats supported are:
- ```"3 6 5 1 8"```
- ``` 3 6 5 1 8```
- ```"3 6" 5 1 8```
- ```3 "6 5" 1 8```

Duplicates, numbers exceeding or below the limits of an integer and any input that is not a number or a sign without a following number will result in an error.

### How to use the checker
To use the provided checker, the usual command is:

```bash 
ARG="numbers_to_sorts"; ./push_swap $ARG | ./checker_Mac $ARG
```
```bash 
ARG="numbers_to_sorts"; ./push_swap $ARG | ./checker_linux $ARG
```
- OK: numbers are sorted.
- KO: numbers aren't sorted.


In order to pass this project, a certain level of performance is required. The command to verify how many instructions are used for sorting is:
```bash 
ARG="numbers_to_sorts"; ./push_swap $ARG | wc -l
```

> [!TIP]
> To get a better view of how my implementation work and how it runs, I used a [push swap vizualizer](https://push-swap42-visualizer.vercel.app/).



## RESSOURCES


*Algorithm*
- https://fr.wikipedia.org/wiki/Algorithme_de_tri

- https://42-cursus.gitbook.io/guide/2-rank-02/push_swap/building-the-thing

*Turk algorithm*
- https://medium.com/@ayogun/push-swap-c1f5d2d41e97

- https://www.youtube.com/watch?v=wRvipSG4Mmk&t=1155s

*Deque - Circular array*

- https://www.geeksforgeeks.org/dsa/introduction-to-circular-queue/

- https://www.geeksforgeeks.org/dsa/circular-array/

- https://www.geeksforgeeks.org/dsa/implementation-deque-using-circular-array/

- https://www.ewskills.com/embedded-c/circular-buffer

*push_swap vizualizer*

- https://push-swap42-visualizer.vercel.app/