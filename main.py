

admin_dic = {
"name": "admins",
"mail": "admin@gmail.com",
"phone_number": "123456778",
"age": "67",
"password": "admin123"
}
user_dic = {
"name": "Vaibhav",
"mail": "vai@gmail.com",
"phone_number": "98876544",
"age": "21",
"password": "qweertyy",
"booked_ticket":[]
}
movie_dic= {
"title":"soty",
"genre":"thriller",
"len":"2hrs",
"cast":"alia",
"direc":"karan",
"admin_rating":10,
"lang":"Hindi",
"show_timing":['7-10', '12-3', '4-7'],
"capa":50
}
movies_list = []



movies_list.append(movie_dic)


def login():
    print("******Welcome to Book My Show******* ")
    input_email = input("Enter Email\n: ")
    input_pass = input("Enter Password\n: ")

    if input_email == admin_dic['mail'] and input_pass == admin_dic["password"]:
        while True:
            print("Logged in Successfully")
            print("\n******Welcome Admin*******")
            ch = input("1. Add New Movie Info\n2. Edit Movie Info\n3. Delete Movies\n4. Logout\nEnter Choice: ")
            if ch == '1':
                print('Add New Movie')
                title = input("Title\n: ")
                genre = input("Genre\n: ")
                len = input("Length\n: ")
                cast = input("Cast\n: ")
                direc = input("Director\n: ")
                admin_rating = int(input("Rating\n: "))
                lang = input("Language\n: ")
                show_timing = input("Sample: 7-10 11-1 4-7\nShow Timing\n: ").split()
                capa = int(input("Capacity\n: "))
                new_movie_dic = {
                    "title": title,
                    "genre": genre,
                    "len": len,
                    "cast": cast,
                    "direc": direc,
                    "admin_rating": admin_rating,
                    "lang": lang,
                    "show_timing": show_timing,
                    "capa": capa
                }
                movies_list.append(new_movie_dic)
                print('New Movie Successfuly')

            elif ch == '2':
                print('Edit movie titles')
                count = 0
                for movie in movies_list:
                    print(count, " ", movie['title'])
                    count += 1
                    ch = int(input("Movie No.\n:"))
            # change movie title

            elif ch == '3':
                print('Delete Movies')
                count = 0
                for movie in movies_list:
                    print(count, " ", movie['title'])
                    count += 1
                    ch = int(input("Movie No.\n:"))
                    movies_list.pop(ch)
                print('Movies Delete Successfuly')

            elif ch == '4':
                print('Logout')
                # exit(0)
                break

    elif input_email == user_dic['mail'] and input_pass == user_dic['password']:
        while True:
            print("Logged in Successfully")
            movies = []
            timing = []
            count = 0
            for movie in movies_list:
                print(count, " ", movie['title'])
                movies.append(movie['title'])
                timing.append(movie['show_timing'])
                count += 1

            usr_input = int(input("98 logout\n99 Exit\n100. My Bookings\n\n:"))
            if usr_input == 99:
                exit(0)
            elif usr_input == 100:
                print(user_dic['booked_ticket'])
            elif usr_input >= 0:
                ch = int(input("1. Book Tickets\n 2. Cancel Tickets\n:"))
                if ch == 1:
                    tim = []

                    count = 0
                    for time in timing:
                        tim.append(time)
                        print(count, " ", time)
                        count += 1
                        choice = input("Timing\n: ")
                        res = movies[usr_input] + " " + str(choice)
                        user_dic['booked_ticket'] = res.split()
                        print("Booked Tickets")

            elif ch == 2:
                print("Ticket Canceled")
                exit(0)
            else:
                print("Not a valid input")
                pass
                elif usr_input == 100:
                # movie details
                pass
                else:
                print("Not a valid input")

                else:
                print("Enter a valid Email and Password.")

def register_new_account():
    print("****Create new Account*****")
    user_dic['name'] = input("Name: ")
    user_dic['mail'] = input("Email: ")
    user_dic['phone'] = input("Phone: ")
    user_dic['age'] = input("Age: ")
    user_dic['password'] = input("Password: ")

print (" ******Welcome to Book My Show*******/n ")
print ("1. Login ")
print("2. Register new account ")
print("3. Exit ")
choice=int(input("Enter: "))
if choice==1:
    login()
elif choice==2:
    register_new_account()
elif choice==3:
    print("Exit")
    exit(0)
else:
    print("Enter a valid input")
# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
