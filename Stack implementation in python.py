#stack implementation in python

#create a stack
def create_stack():
  stack = []
  return stack

#creating a emply stack
def check_empty(stack):
  return len(stack) == 0

#adding item on the stack
def push(stack, item):
  stack.append(item)
  print("Pushed item: " + item)

#removing an element from the stack
def pop(stack):
  if(check_empty(stack)):
    return "stack is empty"
  return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("Popped item: " + pop(stack))
print("Stack after popping an elemnt: " + str(stack))
