from ENUM import Enum
try:
    class dev(Enum):
        games = ['c++','csharp','rust','java','c']
        web = ['html','css','python','nodejs']
        designer = ['xd','photoshop','figma']
        app = ['kotlin','swift','fluter']

    devs = input("Dasturlash tilini kiriting: ").lower()
    for i in dev:
        if devs in i.value:
            print("Kiritilgan dasturlash tilining nimaga ishlatilishi -> ",i.name)
except:
    print("ERROR")