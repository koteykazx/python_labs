keys = ["id", "name", "username", "email"]
users = ["Harry Potter", "Ronald Wisley", "Hermyni Granger"]
 
data = [
       {
           key:(i if key == 'id'
               else users[i] if key == "name"
               else (users[i][0:3].lower() + users[i][-3:].lower()) if key == "username"
               else ("".join(j for j in users[i]).lower().replace(" ", "_"))+"@gmail.com")
           for key in keys
       }
       for i in range(len(users))
       ]
print(data)
