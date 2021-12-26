bande1_2 = {
    '0': 'black',
    '1': 'brown',
    '2': 'red',
    '3': 'orange',
    '4': 'yellow',
    '5': 'green',
    '6': 'blue',
    '7': 'violet',
    '8': 'grey',
    '9': 'white'
}


bande3 = {
    '': 'black',
    '0': 'brown',
    '00': 'red',
    '000': 'orange',
    '0000': 'yellow',
    '00000': 'green',
    '000000': 'blue',
    '0000000': 'violet',
    '00000000': 'grey',
    '000000000': 'white'
}

def value_resistance(resistance_value):
    if len(str(resistance_value)) == 2:
        digit0 = str(resistance_value)[0]
        digit1 = str(resistance_value)[1]
        liste_color = []
        liste_color.append(bande1_2[digit0])
        liste_color.append(bande1_2[digit1])
        liste_color.append('black')
        return  ',  '.join(liste_color)
    elif len(str(resistance_value)) >= 3:
        digit0 = str(resistance_value)[0]
        digit1 = str(resistance_value)[1]
        liste_color = []
        liste_color.append(bande1_2[digit0])
        liste_color.append(bande1_2[digit1])
        digit4 = str(resistance_value)[2]
        if digit4 == '0':
            end_digit = str(resistance_value)[2:]
            liste_color.append(bande3[end_digit])
        else:
            liste_color.append(bande1_2[digit4])
        return  ',  '.join(liste_color)

    else:
        return "no code color for this resistance"

    