#beginning of my palindrome code
from collections import deque

def is_palindrome_using_stack(s: str) -> bool:
    while not(1 <= len(s) <= 50):
        print("Error: input length must be between 1 and 50 characters.")
        s = input("Enter a word: ").strip()

    stack = []
    queue = deque()

    for ch in s:
        stack.append(ch)
        queue.append(ch)

    for _ in range (len(s) // 2):
        if stack.pop() != queue.popleft():
            return False

    return True

#main block
if __name__ == "__main__":
    s = input("Enter a word: ").strip()
    print(is_palindrome_using_stack(s))