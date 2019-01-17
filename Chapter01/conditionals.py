def main():
    defaultScore = 100
    kevinScore = 99
#     if kevinScore > defaultScore:
#         print("Pass")
#     elif kevinScore<defaultScore:
#         print("Fail")
#     else:
#         print("Equal")

    msg = "you did it awesome" if kevinScore > defaultScore else "You didn't made it"
    print(msg)
    
if __name__ == "__main__":main()