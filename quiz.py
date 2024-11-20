import random

# Store users and their credentials
users = {}

questions = [
    {"question": "What is the output of print(2 ** 3)?", "options": ["2", "6", "8", "16"], "answer": "8"},
    {"question": "What is the correct file extension for Python files?", "options": [".py", ".pyt", ".pyth", ".pt"], "answer": ".py"},
    {"question": "What is a correct syntax for defining a function in Python?", "options": ["def function():", "function() def:", "function def():", "function(): def"], "answer": "def function():"},
    {"question": "What is the keyword used to create a class in Python?", "options": ["class", "def", "object", "function"], "answer": "class"},
    {"question": "Which of the following is mutable in Python?", "options": ["string", "tuple", "list", "int"], "answer": "list"},
    {"question": "Which Python function is used to get the length of a list?", "options": ["size()", "len()", "length()", "count()"], "answer": "len()"},
    {"question": "How do you add an element to a list in Python?", "options": ["add()", "insert()", "append()", "extend()"], "answer": "append()"},
    {"question": "What is the purpose of the 'self' keyword in Python?", "options": ["It refers to the class", "It refers to the current instance of the class", "It refers to a global variable", "None of the above"], "answer": "It refers to the current instance of the class"},
    {"question": "What will be the output of print(type(3.14))?", "options": ["int", "float", "str", "complex"], "answer": "float"},
    {"question": "Which of the following is NOT a valid variable name in Python?", "options": ["my_variable", "1st_variable", "variable1", "_variable"], "answer": "1st_variable"},
    {"question": "What is the correct way to handle exceptions in Python?", "options": ["try except", "catch except", "try except finally", "try catch"], "answer": "try except"},
    {"question": "How do you write a comment in Python?", "options": ["//", "#", "/* */", "%%"], "answer": "#"},
    {"question": "Which of the following is used to import a module in Python?", "options": ["import", "include", "use", "require"], "answer": "import"},
    {"question": "What will be the output of print('Python' * 2)?", "options": ["PythonPython", "Python 2", "2 Python", "None of the above"], "answer": "PythonPython"},
    {"question": "What is the purpose of the 'pass' statement in Python?", "options": ["To skip the loop", "To skip the function", "To represent an empty code block", "None of the above"], "answer": "To represent an empty code block"},
    {"question": "Which of the following is used to declare a constant in Python?", "options": ["const", "final", "constant", "None of the above"], "answer": "None of the above"},
    {"question": "What will be the output of print('abc' == 'ABC')?", "options": ["True", "False", "None", "Error"], "answer": "False"},
    {"question": "What is a tuple in Python?", "options": ["A list that cannot be changed", "A function", "A dictionary", "A set"], "answer": "A list that cannot be changed"},
    {"question": "What does the 'len' function return?", "options": ["The length of an object", "The size of an object", "The value of an object", "None of the above"], "answer": "The length of an object"},
    {"question": "Which of the following methods is used to remove an item from a list in Python?", "options": ["remove()", "del", "pop()", "all of the above"], "answer": "all of the above"},
    {"question": "What is the default return value of a function in Python if no return statement is specified?", "options": ["None", "0", "False", "Empty string"], "answer": "None"}
]

# Function to handle registration
def register():
    print("\n--- Registration ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users:
        print("Username already exists. Try logging in.")
    else:
        users[username] = {'password': password, 'score': 0}
        print("Registration successful!")

# Function to handle login
def login():
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]['password'] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

# Function to take the quiz
def take_quiz(username):
    print("\n--- Quiz Time ---")
    selected_questions = random.sample(questions, 5)  # Randomly select 5 questions
    score = 0
    
    for i, question in enumerate(selected_questions, 1):
        print(f"\nQ{i}: {question['question']}")
        for idx, option in enumerate(question['options'], 1):
            print(f"{idx}. {option}")
        
        answer = input("Your answer (1-4): ")
        if question['options'][int(answer)-1] == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: {question['answer']}")

    print(f"\nYour final score: {score} out of 5")
    users[username]['score'] = score


def main():
    while True:
        print("\n--- Welcome to the Python Quiz App ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                take_quiz(username)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
