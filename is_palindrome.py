from collections import deque

class PalindromeChecker:
    def __init__(self):
        self.stack = []
        self.queue = deque()

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.popleft()


s=input("Enter a word:")  


# Create the PalindromeChecker object
checker = PalindromeChecker()

# Push and enqueue all characters
for ch in s:
    checker.pushCharacter(ch)
    checker.enqueueCharacter(ch)

# Check for palindrome
is_palindrome = True
for i in range(len(s) // 2):
    if checker.popCharacter() != checker.dequeueCharacter():
        is_palindrome = False
        break

# Output
if is_palindrome:
    print(f"The word, {s}, is a palindrome.")
else:
    print(f"The word, {s}, is not a palindrome.")
