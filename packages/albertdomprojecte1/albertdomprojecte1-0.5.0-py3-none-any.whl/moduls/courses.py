class course:
    def __init__(self, name,duration,link):
        self.name=name
        self.duration=duration
        self.link=link
    
    def __repr__(self):
        return f"{self.name}[{self.duration} hores]({self.link})"
courses=[
    course("Introduccion a linux", 15,"https://hack4u.io/cursos/introduccion-a-linux/"),
    course("Personalización de linux", 3,"https://hack4u.io/cursos/personalizacion-de-entorno-en-linux/"),
    course("Introduccion al hacking", 53,"https://hack4u.io/cursos/introduccion-al-hacking/"),

]
def list_courses():
    for course in courses:
        print(course)


def search_course(a):
    cursos_filtrats=(course for course in courses if course.name==a)
    for course in cursos_filtrats:            
        print(course)

