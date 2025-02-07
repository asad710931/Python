import os


FILE_NAME="todolist.txt"

def loadingList():
    todo_list={}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,'r') as file:
            for line in file:
                todo_id,title,status=line.strip(). split(" | ")
                todo_list[int(todo_id)]={"title":title,"status":status}
    return todo_list


def saveTodos(todos):
    with open(FILE_NAME,'w') as file:
        for todo_id,todo in todos.items():
            file.write(f"{todo_id} | {todo["title"]} | {todo["status"]}\n")

def saveAsCSV(todos):
    
    with open("data.csv",'w') as file:
        for todo_id,todo in todos.items():
            file.write(f"{todo_id},{todo["title"]},{todo["status"]}\n")

def viewtodos(todos):
    print("----------Todos-------------\n")
    if not todos:
        print("Todos list is empty")
    else:
        for todo_id,todo in todos.items():
            print(f"[{todo_id}]-{todo["title"]}-{todo["status"]}")
    print("\n-----------------------------")



def addTodos(todos):
    title=input("Write title for Todo :")
    todo_id=max(todos.keys(),default=0)+1
    todos[todo_id]={"title":title,"status":"!Done[ ]"}
    print("New Todos added")


def RemoveTodos(todos):
    Input_id=int(input("Write id for remove :"))
    if Input_id in todos:
        removedId=todos.pop(Input_id)
        print(f"{removedId} has been removed")
    else:
        print("Id not found in Todos List")


def markStatus(todos):
    Input_id=int(input("Write id for remove :"))
    if Input_id in todos:
        todos[Input_id]["status"]="Done [*]"
    else:
         print("Id not found in Todos List")


def updateTitle(todos):
    Input_id=int(input("Write id to update :"))
    if Input_id in todos:
        newTitle=input("Write new title to update :")
        todos[Input_id]["title"]=newTitle
    else:
         print("Id not found in Todos List")

 
def main():
    todos=loadingList()
    while True:
        print("1 | for add New Todos")   
        print("2 | for View Todos")
        print("3 | for mark A done")
        print("4 | for remove Todos")
        print("5 | update title of Todos")
        print("6 | Save and Exit From Todos")
        print("7 | save as CSV")
        print("8 | Exit without saving")


        choice=input("Choose your option > ")
        if choice=="1":
            addTodos(todos)
        elif choice=="2":
            viewtodos(todos)
        elif choice=="3":
            markStatus(todos)
        elif choice=="5":
            updateTitle(todos)
        elif choice=="4":
            RemoveTodos(todos)
        elif choice=="6":
            saveTodos(todos)
            print("Todos save in File")
            break
        elif choice=="7":
            saveAsCSV(todos)
            print("CSV file saved")
            # break
        elif choice=="8":
            print("exiting without saving")
            break
        else:
            print("Invalid Input")

if __name__=="__main__":
    main()
            




