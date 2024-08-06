#quizz username

def username(name,last):
    username=last[:2]+name+"#"
    return username.lower()
#programa principal
print(username("ivan","araluce"))
