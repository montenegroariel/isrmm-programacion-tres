from datetime import datetime
ahora = datetime.now()

alumnos = {
    "46251700": "RECALDE RENZO",
    "46252464": "MAXIMILIANO EZEQUIEL ACOSTA",
    "38094977": "NOELIA GAONA",
    "45899843": "SOSA JAVIER PATRICIO",
    "46394081": "RAMÍREZ ALAN",
    "46394033": "FLEITAS RAMIRO",
    "46522893": "HUBER RAMÍREZ",
    "41415458": "SANTIAGO MORA",
    "46154857": "VILLALBA HECTOR",
    "43329003": "ROMERO MIGUEL",
    "33481301": "VERA GABRIELA",
    "46321944": "KAYSER MARCOS",
    "29775014": "CHAVEZ MILTON",
    "44982366": "CABALLERO ESQUIVEL FACUNDO",
    "43068560": "VERA RENAUT MILENA DAYNARA",
    "45901768": "GAUNA GONZALO EXEQUIEL",
    "44344934": "MIGUEL ANGEL MULQUI",
    "46395230": "MARIANELLA MIERS",
    "41176729": "ANDREA CELESTE MOREL",
    "45903304": "LUJAN AILEN BENITEZ",
    "46393658": "VILLALBA GARCIA GUADALUPE"
}

def main():
    while True:
        dni = input('Ingrese un dni:')
        if dni == '': break
        print(alumnos[dni] + " "+ str(ahora))
        
if __name__ == "__main__":
    main()