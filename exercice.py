#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
    if values is None:
        # TODO: Demander les valeurs ici
       values = [input(f"Entrez ... {n}") for n in range(10)]
       return values == sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: Demander les mots ici
        word1 , word2 = input("Write down your two words.\n").split()
    return( (len(word1) == len(word2) and (sorted(word2) == sorted(word1)) ) )

 
def contains_doubles(items: list) -> bool:
    found = None
    if items != None :
        for item in items :
            if items.count(item) != 1 :
                found = True
    if found == True :
        return True
    else :
        return False

def best_grades(student_grades: dict) -> tuple:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    
    grades = dict()

    for name in student_grades :
        grades[name] = round(sum(student_grades[name]) / len(student_grades[name]),3)
    
    values = grades.values()

    for name , grade in grades.items() :
        if grade == max(values) :
            student = name

    return (max(values) , student)

def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    histogram= { i : sentence.count(i) for i in sentence if i != " "}
    constant = 5
    frequent_words = [ k for k , v in histogram.items() if v > constant ]
    
    return histogram ,frequent_words


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    recipes = {}

    for _ in range(int(input("Enter the number of recipes wanted -> "))) :
        name = input("What is the name of the recipe -> ")
        number = input("Enter the number of total ingredients then enter each one ,ona at a time.")
        recipes[name] = [ input() for ingredient in range(int(number)) ]   
         
    return recipes

def print_recipe(ingredients):
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    recipe = input("What is the name of the recipe you are looking for? ")
    print(ingredients.get(recipe , "Recipe not found"))
    


def main() -> None :
    print(f"On essaie d'ordonner les valeurs...")
    print(order(),"\n")

    print(f"On vérifie les anagrammes...")
    print(anagrams(),"\n")

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}.\n")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}.\n")

    sentence = input("Donnez une phrase: ")
    print(histogram(sentence),"\n")
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
