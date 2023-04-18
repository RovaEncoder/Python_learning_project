import random as np

# on a une chaine de caractère
# on transforme la chaine de caractère en une liste de mots avec la méthode split()
# ensuite on génère aléatoirement un index  pour tirer un mot aléatoire dans note liste de mots
# recupération du mot aléatoire

nb_life = 5

words = "abuser crottes fleches continental babiole etoile bougie coup coeur malade rova entretien chauvin arnoux"

words_list = words.split()

nb_alea = np.randint(0, len(words_list)-1)

secret_word = words_list[nb_alea]

# dictinaire contenant les info necessaire pour le jeux

dictionnaire = {

    "secret_word": secret_word,
    "guess_word": "_" * len(secret_word),
    "life": nb_life

}

print(f"{dictionnaire['guess_word']} | vie= {dictionnaire['life']}")

while True:

    enter_caract = input("Enter un caractère > ")
    if enter_caract in dictionnaire["secret_word"] and enter_caract not in dictionnaire['guess_word']:

        list_of_caract = list(dictionnaire['guess_word'])
        for index, current_letter in enumerate(dictionnaire["secret_word"]):
            if current_letter == enter_caract:
                list_of_caract[index] = enter_caract
        dictionnaire["guess_word"] = "".join(list_of_caract)

    elif enter_caract not in dictionnaire["secret_word"]:
        dictionnaire["life"] -= 1
    print(f"{dictionnaire['guess_word']} | vie= {dictionnaire['life']}")

    if "_" not in dictionnaire['guess_word']:
        print(
            f"Felicitation vous avez trouvé le mot: {dictionnaire['secret_word']}")

        break
    elif dictionnaire['life'] < 1:
        print(
            f"Vous avez perdu le mot est: {dictionnaire['secret_word']}")
        break
