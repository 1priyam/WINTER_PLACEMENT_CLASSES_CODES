file_name = open("expense_data.txt")
expense = []


#LOAD DATA
def load_data():
    global expenses
    try:
        file = open(file_name,"r")
        lines = file.readlines()
        file.close()
    for line in lines:
        line = line.strip()
        amount,category,note=line.split(",")                     #these are storing values by splitting the lines
        expense = {
            "amount":int(amount),
            "category":category,
            "note":note
        }
        expense.append
