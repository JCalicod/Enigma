import random

def decryptMessage(message, rings, positions):
    counters = getCounters(len(rings))
    decrypted_message = ''
    for character in message:
        if character != ' ':
            i = 0
            last = len(rings) - 1
            for ring in reversed(rings):
                if i == 0:
                    res = chr(
                            (ring.index(character) - counters[last] - positions[last]) % 26 + 97
                        )
                else:
                    res = res.lower()
                    res = chr(
                            (ring.index(res) - counters[last - i] - positions[last - i]) % 26 + 97
                        )
                i = i + 1
            decrypted_message = decrypted_message + res
            counters = moveRings(rings, counters)
        else:
            decrypted_message = decrypted_message + ' '
    return decrypted_message

def moveRings(rings, counters):
    for i in range(len(rings)):
        if (i != 0 and counters[i - 1] == 0) or (i == 0):
            counters[i] = (counters[i] + 1) % 25
    return counters

def getCounters(nb_rings):
    counters = []
    for i in range(nb_rings):
        counters.append(0)
    return counters

def encryptMessage(message, rings, positions):
    counters = getCounters(len(rings))
    encrypted_message = ''
    for character in message:
        if character != ' ':
            for i in range(len(rings)):
                if i == 0:
                    res = rings[i][(ord(character) - 97 + counters[i] + positions[i]) % 26]
                else:
                    res = rings[i][(ord(res) - 97 + counters[i] + positions[i]) % 26]
            encrypted_message = encrypted_message + res
            counters = moveRings(rings, counters)
        else:
            encrypted_message = encrypted_message + ' '
    return encrypted_message

def getMessage():
    message = ''
    while message == '':
        print('Saisie du message à déchiffrer :')
        message = input().lower()
    return message

def showRingsPosition(positions):
    for i in range(len(positions)):
        print(positions[i])

def getRingsPosition(number_of_rings):
    rings_position = []
    for i in range(number_of_rings):
        position = -1
        while position < 0 or position > 25:
            print("Choix de la position de l'anneau " + str(i + 1) + " (entre 0 et 25 inclus) :")
            position = int(input())
        rings_position.append(position)
    return rings_position

def showRings(rings):
    for i in range(len(rings)):
        print(rings[i])

def getRings(number_of_rings):
    rings = []

    for i in range(number_of_rings):
        abc = list('abcdefghijklmnopqrstuvwxyz')
        random.shuffle(abc)
        rings.append(abc)
    return rings

def getNumberOfRings():
    nb = 0
    while nb < 2 or nb > 10:
        print("Veuillez choisir le nombre d'anneaux à intégrer à la machine (compris entre 2 et 10 inclus)")
        nb = int(input())
    return nb



if __name__ == "__main__":
    number_of_rings = getNumberOfRings()
    rings = getRings(number_of_rings)
    positions = getRingsPosition(number_of_rings)
    message = getMessage()
    print('Message de base : ' + str(message))
    encrypted_message = encryptMessage(message, rings, positions)
    print('Message crypté : ' + str(encrypted_message))
    decrypted_message = decryptMessage(encrypted_message, rings, positions)
    print('Message décrypté : ' + str(decrypted_message))
