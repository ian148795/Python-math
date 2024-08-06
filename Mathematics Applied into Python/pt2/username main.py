def username(first,middle,last):
    name=first[0]
    for letra in "aeiouAEIOU":
        consonante=letra
        break
    name=name+consonante+last
    user=name[0:8].lower()
    return user

def main(): 
    print(username('Scarlett', 'Ingrid', 'Johansson'))
    print(username('Donald', 'Ervin', 'Knuth'))
    print(username('Alan', 'Mathison', 'Turing')) 
    print(username('Martin', 'Luther', 'King')) 
    print(username('Stephen', 'William', 'Hawking'))
    print(username('Alejandro', 'Gonzalez', 'Inarritu'))
main()
