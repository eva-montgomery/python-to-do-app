# to-do's: 
# -> todo's are a collection of individual variables in list as a string

# choose one -> adding a todo
# Enter a todo -> prompt user for the new todo then .append() to list of todo's

# Use a for loop to print each todo in our list of todo's

# how can I delete item from a list?
#  --> del keyword and the index
# ex. del pets[1] -> deletes second item in pet list
###################################

# keep track of todo's unsing a list.
todo_list = []

# I neeed a way to add todos.
def add_todo(todo):
    # We receive a todi, which is a string
    todo_list.append(todo)
# print the empty todo list
print(todo_list)
# add a todo my calling our function
add_todo("feed the cat")
# print the todo list again, making sure our code got added
print(todo_list)

# I nmeed to be able to delete todo's.

# I need to print my todo's

# Show user the main menu.