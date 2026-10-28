import traceback

#Task 1: Diary
try:
    with open('diary.txt', 'a') as file:
        user_input = input("What happened today?")
 
        while user_input != "done for now":

            file.write(user_input) #  Write to the file
            file.write('\n')
        
            user_input = input("What else? ")

        file.write(user_input) #  Write to the file
        file.write('\n')

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")