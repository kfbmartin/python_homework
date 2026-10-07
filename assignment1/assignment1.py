# Task #1: Hello
def hello():
    greeting = 'Hello!'
    return greeting

print(hello())

#Task 2: Greet with a Formatted String
def greet(name):
    return  f"Hello, {name}!"

print(greet('Khalilah'))

#Task 3: Calculator
def calc(num1, num2, operation="multiply"):
    try: 
        match operation:
            case "add":
                return num1+num2
            case "subtract": 
                return num1-num2
            case "multiply":
                return num1*num2
            case "divide":
                return num1/num2
            case "modulo":
                return num1%num2
            case "int_divide":
                return num1//num2
            case "power":
                return num1**num2
    except ZeroDivisionError:
        return "You can't divide by 0!"
    
    except TypeError: 
        return "You can't multiply those values!"
    



#Task 4: Data Type Conversion
def data_type_conversion(value, type):
    try:
       if type == "float":
           return float(value) 
       elif type == "int":
            return int(value)
       elif type == "str":
           return str(value)

    except ValueError:
        return f"You can't convert {value} into a {type}."

#Task 5: Grading System, Using *args
def grade(*args):
    try: 
        average_grade = sum(args) / len(args)
        if average_grade >=90:
            class_grade = "A"
        elif average_grade <=89 and average_grade >=80:
            class_grade = "B"
        elif average_grade <=79 and average_grade >=70:
            class_grade = "C"
        elif average_grade <=69 and average_grade >= 60:
            class_grade = "D"
        elif average_grade < 60:
            class_grade = "F"

        return class_grade
    
    except:
        
        return "Invalid data was provided."

#Task 6: Use a For Loop with a Range
def repeat(string, count):
    concat_string = ""

    for i in range(count):
        concat_string = concat_string + string
    
    return concat_string

#Task 7: Student Scores, Using **kwargs
def student_scores(position, **kwargs):
    if position == "best":
    
        student_value = 0
        
        for key, value in kwargs.items():
            if student_value < value:
                student_value = value
                student_name = key

        return student_name

    elif position == "mean":
        return sum(kwargs.values()) / len(kwargs)

#Task 8: Titleize, with String and List Operations
def titleize(title):

    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = title.split()
    new_words = []

    for index, word in enumerate(words):
        if index == 0:
           new_words.append(word.capitalize())
        
        elif index == len(words) - 1: 
            new_words.append(word.capitalize())

        elif word in little_words:
            new_words.append(word)

        else:
            new_words.append(word.capitalize())

    capitalize_title = " ".join(new_words)

    return capitalize_title


#Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result = result + letter

        else: 
            result = result + '_'

    return result


#Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(string):
    vowels = "aeiou"
    words = string.split()
    new_words = []

    for word in words:
        if word[0] in vowels:
            new_words.append(word + "ay")
        else:
            for index, letter in enumerate(word):
                if letter in vowels:
                    if letter == "u" and word[index -1] == "q":
                        continue

                    new_words.append (word[index:] + word[:index] + "ay")
                    break

    return " ".join(new_words)

