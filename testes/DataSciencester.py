users = [
    {"id":0, "name":"Hero"},
    {"id":1, "name":"Dunn"},
    {"id":2, "name":"Sue"},
    {"id":3, "name":"Chi"},
    {"id":4, "name":"Thor"},
    {"id":5, "name":"Clive"},
    {"id":6, "name":"Hicks"},
    {"id":7, "name":"Devin"},
    {"id":8, "name":"Kate"},
    {"id":9, "name":"klein"}
]

friendships = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),
              (5,6),(5,7),(6,8),(7,8),(8,9)]

for user in users:
    user["friends"]=[]

for i, j in friendships:
    # Isso funciona por users[i] é o usuario cuja id é i
    users[i]["friends"].append(users[j]) # Adiciona i como amigo de j
    users[j]["friends"].append(users[i]) # Adiciona j como amigo de i

def number_of_friends(user):
    # Quantos amigos o usuario tem?
    return len(user["friends"])

total_connections = sum(number_of_friends(user)
                        for user in users)

num_users = len(users)
agv_connection = total_connections / num_users

# Cria uma lista(user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))
                            for user in users]

sorted(num_friends_by_id,
            key=lambda(user_id, num_friends): num_friends, 
            reverse=True)
