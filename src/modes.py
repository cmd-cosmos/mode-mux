#pylint: skip-file

modes_map = {
    0 : "fun", 
    1 : "study", 
    2 : "work" 
}

def fun():
    print("Running fun setup routine")

def study():
    print("Running study setup routine")

def work():
    print("Running work setup routine")

name_func_map = {
    "fun"  : fun,
    "study": study,
    "work" : work
}