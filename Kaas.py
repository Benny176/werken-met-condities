Gelekaas = input('is de kaas geel?')
if Gelekaas == "ja":
    Gatenkaas = input('zitten er gaten in?')
    if Gatenkaas == "ja": 
        duurdekaas = input('is de kaasbelachelijk duur? ')
        if duurdekaas == "ja":
            print('Uw kaas is Emmenthaler')
        else: 
            print('Uw kaas is Leerdammer')
    else: 
        hardekaas = input('is ur kaas hard als steen?')
        if hardekaas == "ja":
            print('Uw kaas is Parmigiano Reggiano')
        else:
            print('Uw kaas is Goude Kaas')
else: 
    Blauwekaas = input('heeft ur kaas blauwe schimmels?')
    if Blauwekaas == "ja":
        korstkaas = input('heeft de kaas een korst?')
        if korstkaas == "ja":
            print('Uw kaas is Bleu de Rochbaron')
        else:
            print('Uw kaas is Fourme d Amberst')
    else:
        input('heeft de kaas een korst?')
        if Blauwekaas == "ja":
            print('Uw kaas is Camembert')
        else:
            print('Uw kaas is Mozzarella')



    



