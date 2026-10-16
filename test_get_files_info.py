from functions.get_files_info import get_files_info

print('Result for current directory:')
strings = (get_files_info("calculator", ".")).splitlines()
for str in strings:
    print(f'  {str}')
print("Result for 'pkg' directory:")
strings = (get_files_info("calculator", "pkg")).splitlines()
for str in strings:
    print(f'  {str}')
print("Result for '/bin' directory:")
strings = (get_files_info("calculator", "/bin")).splitlines()
for str in strings:
    print(f'  {str}')
print("Result for '../' directory:")
strings = (get_files_info("calculator", "../")).splitlines()
for str in strings:
    print(f'  {str}')
