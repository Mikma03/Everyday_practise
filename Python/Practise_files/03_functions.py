
# positional arguments
def subtract(x, y):
    return x - y

subtract(11, 4)
subtract(4, 11)


# Named arguments
def greet(name, surname):
    print("hello,", name, surname)

# non-keyword arguments
greet("Willy", "Wonka")

# Keyword arguments
greet(surname="Wonka", name="Willy")
greet("Frodo", surname="Baggins")

def responsibility(developer, tester, project_manager, designer):
    print(developer, "writes code")
    print(tester, "tests the system")
    print(project_manager, "manages the product")
    print(designer, "develops design")

responsibility(project_manager="Sara", developer="Abdul", tester="Yana", designer="Mark")
responsibility("Sara", "Abdul", "Yana", "Mark")

help(responsibility)