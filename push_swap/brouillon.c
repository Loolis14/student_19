//stack a = argv, stack b empty
/* #include "push_swap.h"
#include <unistd.h>
#include <stdio.h>
#include <stddef.h> */
//printf("%c",argv[i][j]);

//printf("%c",argv[i][j]);

//création deque

#include "push_swap.h"

stack	create_stack(int *numbers, int count)
{
	stack	a;

	a.numbers = numbers;
	a.front = numbers[0];
	a.capacity = count;
	a.size = count;

	return (a);
}

//get_rear() rear = (front + size - 1) % capacity
//get_front() arr[front]


//move front forward : front = (front + 1) % capacity -> then --size;
//insert element at the reat : rear = (front + size) % capacity -> then ++size;
//Removed an element from the front : front = (front + 1 %) capacity then --size;