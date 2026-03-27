#exs 1
#part a
rows = 3
for i in range(rows):
    # Spaces: 2, 1, 0
    # Stars:  1, 3, 5
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
    
    #part b
    rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)
    
    #part c
    rows = 5
# Top Part
for i in range(1, rows + 1):
    print("*" * i)

# Bottom Part
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * i)