def main(prompt):
     return f"My favorite animal is also {prompt}"
user_input:str = str(input("What's your favorite animal? "))
res = main(user_input)
print(res)