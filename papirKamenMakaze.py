import random

opcije = ['papir', 'kamen', 'makaze']
izbor_igraca = None
nova_igra = 'yes'
izbor_racunara = None
rezultat_racunara = 0
tvoj_rezultat = 0
poena_do_pobede = 3

def poruka():
    print('Racunar je izabrao: ' + izbor_racunara + ' a ti si izabrao: ' + izbor_igraca)
    print('Trenutan rezultat je: ')
    if rezultat_racunara < poena_do_pobede and tvoj_rezultat < poena_do_pobede:
        print("Racunar:" + str(rezultat_racunara) + '({} poena do pobede)'.format(str(poena_do_pobede - rezultat_racunara)))
        print("Korisnik:" + str(tvoj_rezultat) + '({} poena do pobede)'.format(str(poena_do_pobede - tvoj_rezultat)))

    if rezultat_racunara==poena_do_pobede:
        print("Racunar je pobedio sa rezultatom: {}:{}".format(str(rezultat_racunara), str(tvoj_rezultat)))
    if tvoj_rezultat==poena_do_pobede:
        print("Pobedio si sa rezultatom: {}:{}".format(str(tvoj_rezultat), str(rezultat_racunara)))

while nova_igra == 'yes':
    while rezultat_racunara < poena_do_pobede and tvoj_rezultat < poena_do_pobede:
        while izbor_igraca not in opcije:
            izbor_igraca = input('Unesite svoj izbor (papir, kamen ili makaze):').lower()
        izbor_racunara = opcije[random.randint(0, 2)]
        if izbor_racunara == opcije[0]:
            if izbor_igraca == opcije[0]:
                print("Nereseno je!")
                poruka()
            elif izbor_igraca == opcije[1]:
                print('Vise srece drugi put jbg, racunar je pobedio :)')
                rezultat_racunara += 1
                poruka()
            else:
                print("Hej, pobedio si masinu!")
                tvoj_rezultat += 1
                poruka()
        elif izbor_racunara == opcije[1]:
            if izbor_igraca == opcije[0]:
                print("Hej, pobedio si masinu!")
                tvoj_rezultat += 1
                poruka()
            elif izbor_igraca == opcije[1]:
                print("nereseno je!")
                poruka()
            else:
                print('Vise srece drugi put jbg, racunar je pobedio :)')
                rezultat_racunara += 1
                poruka()
        else:
            if izbor_igraca == opcije[0]:
                print('Vise srece drugi put jbg, racunar je pobedio :)')
                rezultat_racunara += 1
                poruka()
            elif izbor_igraca == opcije[2]:
                print("nereseno je!")
                poruka()
            else:
                print("Hej, pobedio si masinu!")
                tvoj_rezultat += 1
                poruka()
        izbor_igraca = None
    nova_igra = input('Zelite li da probate ponovo? ').lower()
    rezultat_racunara=0
    tvoj_rezultat=0