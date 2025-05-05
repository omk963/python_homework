# Task 1: Hello
def hello():
    return("Hello!")

# Task 2: Greet with a Formatted String
def greet(name):
    return("Hello, " + name + "!")

# Task 3: Calculator
def calc(int1, int2, operation = "multiply"):
    try:
        match operation:
            case "multiply":
                return int1 * int2
            case "add":
                return int1 + int2
            case "subtract":
                return int1 - int2
            case "divide":
                return int1 / int2
            case "modulo":
                return int1 % int2
            case "int_divide":
                return int(int1 / int2)
            case "power":
                return int1 ** int2
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
# Task 4: Data Type Conversion
def data_type_conversion(value, type):
    try:
        match type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."
    
# Task 5: Grading System, Using *args
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."

# Task 6: Use a For Loop with a Range
def repeat(string, count):
    new_string = ""
    for str in range(count):
        new_string += string
    return new_string

# Task 7: Student Scores, Using **kwargs
def student_scores(positional, **kwargs):
    if positional == "best":
        return max(kwargs, key=kwargs.get)
    elif positional == "mean":
        return sum(kwargs.values()) / len(kwargs)
    
# Task 8: Titleize, with String and List Operations
def titleize(title):
    words = title.split()
    for i, word in enumerate(words):
        if len(word) > 3:
            words[i] = word.capitalize()
    words[0] = words[0].capitalize()
    words[-1] = words[-1].capitalize()
    return ' '.join(words)

# Task 9: Hangman, with more String Operations
def hangman(secret_word, guess):
    secret = ""
    for i in range(len(secret_word)):
        for j in range(len(guess)):
            if secret_word[i] == guess[j]:
                secret += guess[j]
        if(len(secret) != i + 1):
            secret += "_"
    return secret

# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(string):
    vowels = "aeiou"
    special_cases = "qu"
    words = string.split()
    pig_latin_words = []
    for word in words:
        if word[0] in vowels:
            pig_latin_words.append(word + "ay")
        elif special_cases in word:
            for i in range(len(word)):
                if word[i:i+2] == special_cases:
                    pig_latin_words.append(word[i+2:] + word[:i+2] + "ay")
                    break
        elif word[0] not in vowels:
            for i in range(len(word)):
                if word[i] in vowels:
                    pig_latin_words.append(word[i:] + word[:i] + "ay")
                    break
    return " ".join(pig_latin_words)

