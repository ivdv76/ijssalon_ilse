from algemene_functies import mijn_functie_2

def aanbieding_1 (smaak, prijs, korting):
        return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs-prijs*korting} euro."
# print (aanbieding_1("aardbei", 4, 0.1))


def inkomsten_totaal (inkomsten, btw):
        return f"Het totaal van alle inkomsten van deze week is {sum(inkomsten)} euro, waarover {btw*sum(inkomsten)} euro btw betaald dient te worden."
inkomsten = [220,430,125,160,205,90,345]
btw = 0.09
#print (inkomsten_totaal (inkomsten, btw))


def laag_en_hoog(mijn_lijst):
        #return f"laagste: {min(mijn_lijst)}, hoogste: {max (mijn_lijst)}"
        return min(mijn_lijst), max (mijn_lijst)
#print (laag_en_hoog (inkomsten))


def gemiddelde (mijn_lijst):
        return f"De gemiddelde inkomsten deze week zijn {round(sum(inkomsten)/len(inkomsten))} euro."
#print (gemiddelde(inkomsten))

invoerlijst = [10,5,3,2,1,2,9]
def meervoudig(invoer_lijst):
        return laag_en_hoog(invoer_lijst)
#print (meervoudig (invoerlijst))


def combinatie (invoer_lijst_2):
       return laag_en_hoog(invoer_lijst_2)

korte_lijst = combinatie (invoerlijst)
invoerlijst = [10,5,3,2,1,2,9]
def meervoudig(invoer_lijst):
        return laag_en_hoog(invoer_lijst)
#print (meervoudig (invoerlijst))


def combinatie (invoer_lijst_2):
       return laag_en_hoog(invoer_lijst_2)

korte_lijst = combinatie (invoerlijst)
#print (korte_lijst)
print (mijn_functie_2 (korte_lijst))print (mijn_functie_2 (*korte_lijst))