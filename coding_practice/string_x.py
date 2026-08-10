#!/usr/bin/env python3
#Practicing sequence (string) Multiplication Example
#Prints a sentence in a centered "box" of correct width

sentence=input("Please input a sentence: ")

screen_width=80
text_width=len(sentence)
box_width=text_width + 6
left_margine=(screen_width-box_width) // 2

print()
print(left_margine)
print(text_width)
print(box_width)
print(" "*left_margine+"+" + "-"*(box_width-2)+"+")
print(" "*left_margine+"|  "+ " "*text_width   +"  |")
print(" "*left_margine+"|  "+     sentence     +"  |")
print(" "*left_margine+"|  "+ " "*text_width   +"  |")
print(" "*left_margine+"+" + "-"*(box_width-2)+"+")
print()
