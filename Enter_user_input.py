# project on list user input(adding data and deleting data)
user_name=input("Enter your Name Please:-\n")
user_phone_number=input("Enter your Phone Number Please:-\n")
user_email=input("Enter your Email Address Please:-\n")
user_zip_code=input("Enter your Zip code Please:-\n")

check_list=[user_name,user_phone_number,user_email,user_zip_code]
print(check_list)
print(" \n")

print("If you can add any other data in check list then Enter other data \n")
add=input("Enter Data for Add in list:-\n")
check_list.append(add)
print(check_list)
print(" \n")
print("If you can Delete any data in check list then Enter data index Number\n")
delete=int(input("Enter Data for Delete in list:-\n"))
check_list.pop(delete)
print(check_list)
