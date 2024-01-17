# Linked Lists Insertions
<!-- Description of the challenge -->
Extend a Linked List to allow various insertion methods.

`append`

- arguments: new value
- adds a new node with the given value to the end of the list

`insert before`

- arguments: value, new value
- adds a new node with the given new value immediately before the first node that has the value specified

`insert after`

- arguments: value, new value
- adds a new node with the given new value immediately after the first node that has the value specified

## Whiteboard Process
<!-- Embedded whiteboard image -->
![linked lists insertions whiteboard](./linked_list_insertions_whiteboard.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
### Algorithm

```pseudocode
function append(newValue):
  newNode = newValue
  currentNode = linkedList.head
  WHILE currentNode.next NOT NULL
    currentNode = currentNode.next
  currentNode.next = newNode

function insert_before(value, newValue):
  newNode = newValue
  currentNode = linkedList.head
  WHILE currentNode.next != value
    currentNode = currentNode.next
  newNode.next = currentNode.next
  currentNode.next = newNode


function insert_after(value, newValue):
  newNode = newValue
  currentNode = linkedList.head
  WHILE currentNode != value
    currentNode = currentNode.next
  newNode.next = currentNode.next
  currentNode.next = NewNode
```

### Big O

Append

- Time:  O(n)
- Space:  O(1)

Insert Before

- Time:  O(n)
- Space:  O(1)

Insert After

- Time:  O(n)
- Space:  O(1)

## Solution
<!-- Show how to run your code, and examples of it in action -->
To test run `pytest -k linked_list` from the `~/python` directory.
