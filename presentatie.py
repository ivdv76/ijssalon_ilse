def presenteer (dictionary, totaal):
    for keys, values in dictionary.items():
        print (f"{keys} : {values} euro")
    print (25* "=")
    return f"totaal : {totaal} euro"