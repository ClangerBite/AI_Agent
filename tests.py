from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

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
    
    result = get_file_content("calculator", "main.py")
    print("Result for 'main.py':")
    print(f"{result}\n")
    
    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for 'pkg/calculator.py':")
    print(f"{result}\n")
    
    result = get_file_content("calculator", "m/bin/cat")
    print("Result for '/bin/cat':")
    print(f"{result}\n")


if __name__ == "__main__":
    test()