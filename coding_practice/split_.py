#!/usr/bin/env python3

#Trying to write a program that split a domain name from a url assuming
#the domain name is within the range [11:-4]

url=input("Please input a url: ")
domain_name=url[11:-4]
print("The domain name of the url is: " + domain_name)
