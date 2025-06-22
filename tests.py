from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


def test():
    print("")
    
    # result = get_files_info("calculator", ".")
    # print("Result for current directory:")
    # print(f"{result}\n")

    # result = get_files_info("calculator", "pkg")
    # print("Result for 'pkg' directory:")
    # print(f"{result}\n")

    # result = get_files_info("calculator", "/bin")
    # print("Result for '/bin' directory:")
    # print(f"{result}\n")

    # result = get_files_info("calculator", "../")
    # print("Result for '../' directory:")
    # print(f"{result}\n")
    
    # result = get_file_content("calculator", "lorem.txt")
    # print("Result for 'lorem.txt:")
    # print(f"{result}\n")
    
    # result = get_file_content("calculator", "main.py")
    # print("Result for 'main.py':")
    # print(f"{result}\n")
    
    # result = get_file_content("calculator", "pkg/calculator.py")
    # print("Result for 'pkg/calculator.py':")
    # print(f"{result}\n")
    
    # result = get_file_content("calculator", "/bin/cat")
    # print("Result for '/bin/cat':")
    # print(f"{result}\n")
    
    # result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    # print("Result for 'lorem.txt':")
    # print(f"{result}\n")
    
    # result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # print("Result for 'pkg/morelorem.txt':")
    # print(f"{result}\n")
    
    # result = write_file("calculator","/tmp/temp.txt", "this should not be allowed")
    # print("Result for '/tmp/temp.txt':")
    # print(f"{result}\n")
    
    
    result = run_python_file("calculator", "main.py")
    print("Result for 'main.py':")
    print(f"{result}\n")
    
    result = run_python_file("calculator", "tests.py")
    print("Result for 'tests.py':")
    print(f"{result}\n")
    
    result = run_python_file("calculator", "../main.py")
    print("Result for '../main.py':")
    print(f"{result}\n")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for 'nonexistent.py':")
    print(f"{result}\n")

if __name__ == "__main__":
    test()
