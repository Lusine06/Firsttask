#!/usr/bin/python3

import random

print("Welcome!")

choice = input("Pick a number (1, 2 or 3) or write 'random': ")

if choice == "random":
	templ_num = random.randint(1, 3)
else:
	templ_num = int(choice)

if templ_num == 1:
	print("Enter the information about first template:")

	number1 = input("Input a number: ")
	measure = input("Input a measure of time: ")
	transport = input("Input a mode of transportation: ")
	adj_hos1 = input("Input 1st adjective: ")
	adj_hos2 = input("Input 2nd adjective: ")
	noun1 = input("Input 1st noun: ")
	color = input("Input a color: ")
	body_part1 = input("Input a body part: ")
	verb1 = input("Input a verb: ")
	number2 = input("Input a number: ")
	noun2 = input("Input 2nd noun: ")
	noun3 = input("Input 3rd noun: ")
	body_part2 = input("Input a body part: ")
	verb2 = input("Input a verb: ")
	noun4 = input("Input 4th noun: ")
	adj_hos3 = input("Input 3rd adjective: ")
	silly_word = input("Input a silly word: ")
	noun5 = input("Input 5th noun: ")

	print("\nThe story we got :)\n")
	story = f"""It was about {number1} {measure} ago when I arrived at the hospital
in a {transport}. The hospital is a/an {adj_hos1} place, there are a lot of
{adj_hos2} {noun1} here. There are nurses here who have {color} {body_part1}.
If someone wants to come into my room I told them that they have to {verb1}
first. I've decorated my room with {number2} {noun2}. Today I talked to a
doctor and they were wearing a {noun3} on their {body_part2}. I heard that
all doctors {verb2} {noun4} every day for breakfast. The most {adj_hos3}
thing about being in the hospital is the {silly_word} {noun5}!"""

	print(story)

elif templ_num == 2:
    print("Enter the information about the second template:")

    name = input("Input a name: ")
    noun1 = input("Input a noun: ")
    adjective1 = input("Input an adjective (feeling): ")
    verb1 = input("Input the 1st verb: ")
    adjective2 = input("Input an adjective (feeling): ")
    animal1 = input("Input the 1st animal: ")
    verb2 = input("Input the 2nd verb: ")
    color1 = input("Input the 1st color: ")
    verb_ing = input("Input a verb + ing: ")
    adverb = input("Input an adverb + ly: ")
    number1 = input("Input the 1st number: ")
    measure = input("Input a measure of time: ")
    color2 = input("Input the 2nd color: ")
    animal2 = input("Input the 2nd animal: ")
    number2 = input("Input the 2nd number: ")
    silly_word = input("Input a silly word: ")
    noun2 = input("Input a noun: ")

    print("\nThe story we got :)\n")

    story = f"""This weekend I am going camping with {name}. I packed my lantern, sleeping bag, and {noun1}. I am so {adjective1} to {verb1} in a tent. I am {adjective2} we might see a(n) {animal1}, I hear they're kind of dangerous. While we're camping, we are going to hike, fish, and {verb2}. I have heard that the {color1} lake is great for {verb_ing}. Then we will {adverb} hike through the forest for {number1} {measure}. If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! At night we will tell {number2} {silly_word} stories and roast {noun2} around the campfire!!"""

    print(story)

elif templ_num == 3:
    print("Enter the information about the third template:")

    name = input("Input a person's name: ")
    adjective1 = input("Input an adjective: ")
    color = input("Input a color: ")
    animal = input("Input an animal: ")
    place = input("Input a place: ")
    adjective2 = input("Input an adjective: ")
    magical_creature1 = input("Input a magical creature (plural): ")
    adjective3 = input("Input another adjective: ")
    magical_creature2 = input("Input another magical creature (plural): ")
    room = input("Input a room in a house: ")
    noun1 = input("Input a noun: ")
    noun2 = input("Input another noun: ")
    noun3 = input("Input a noun (plural): ")
    adjective4 = input("Input an adjective: ")
    noun4 = input("Input a noun (plural): ")
    number = input("Input a number: ")
    measure = input("Input a measure of time: ")
    verb_ing = input("Input a verb ending in -ing: ")
    adjective5 = input("Input an adjective: ")
    noun5 = input("Input a noun: ")

    print("\nThe story we got :)\n")

    story = f"""Dear {name},

I am writing to you from a {adjective1} castle in an enchanted forest.I found myself here one day after going for a ride on a {color} {animal} in {place}. There are {adjective2} {magical_creature1} and {adjective3} {magical_creature2} here! In the {room} there is a pool full of {noun1}. 
I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} {noun4}. It feels as though I have lived here for {number} {measure}. I hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective5} {noun5}!"""

    print(story)


else:
    print("That number doesn't match any template.")
    

   

