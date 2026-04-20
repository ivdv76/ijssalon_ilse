def decoreer (tekst=""):
    tekst = "header"
    lengte = len(tekst) + 4
    print ()
    print (lengte * "*")
    print (f"* {tekst} *")
    print (lengte * "*")
    print()


def fooi_pp (bedrag, personen):
   # try:
    bedrag_pp = bedrag/personen
   # except:
   #     bedrag_pp = "??"
    return f"Het bedrag per persoon is {bedrag_pp} euro"

# b = int(input("Welk bedag zit er in de fooienpot?"))
# p = int(input("Over hoeveel personen moet de pot verdeeld worden?"))
# print(fooi_pp(b,p))

def onderstreep (tekst=""):
    uit = []
    uit.append(tekst)
    lengte = (len(tekst))
    uit.append(lengte*"=")
    return (uit)


def som (dictionary):
    values = dictionary.values ()
    return sum(values)

