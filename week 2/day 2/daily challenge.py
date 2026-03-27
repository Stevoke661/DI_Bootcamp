#pegination implementation
import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        # Step 2: Initialize attributes
        self.items = items if items is not None else []
        self.page_size = int(page_size)
        self.current_idx = 0  # Internal 0-based index
        
        # Calculate total pages
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.items else 1

    def get_visible_items(self):
        # Step 3: Use slicing to get the current page's content
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        # Step 4: Handle 1-based user input and bounds checking
        page_num = int(page_num)
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page number must be between 1 and {self.total_pages}.")
        
        self.current_idx = page_num - 1
        return self # Allows chaining

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        # Step 5: Bonus - Format current items as a newline-separated string
        return "\n".join(map(str, self.get_visible_items()))
    
    #functionality test
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

# Test 1: Initial visible items
print(f"Page 1: {p.get_visible_items()}") 
# Output: ['a', 'b', 'c', 'd']

# Test 2: Moving forward
p.next_page()
print(f"Page 2: {p.get_visible_items()}") 
# Output: ['e', 'f', 'g', 'h']

# Test 3: Jumping to the end
p.last_page()
print(f"Last Page: {p.get_visible_items()}") 
# Output: ['y', 'z']

# Test 4: Chaining Methods (Bonus)
# Move to first page, then click 'next' three times
result = p.first_page().next_page().next_page().next_page().get_visible_items()
print(f"Chained Result: {result}") 
# Output: ['m', 'n', 'o', 'p']

# Test 5: Error Handling
try:
    p.go_to_page(10)
except ValueError as e:
    print(f"Caught expected error: {e}")