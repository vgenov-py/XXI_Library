import datetime as dt

def write_error(code:int=0,error:str="NULL" ,message:str="NULL"):
    with open("logs/errors.log", "a", encoding="utf-8") as file:
        file.write(f"{dt.datetime.now()}|{code}|{error}|{message}\n")