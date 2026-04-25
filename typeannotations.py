#What is type annotation?
x = 10

weather = "sunny"
#Code editor will become unhappy if we change weather w/out using it
print(weather)
weather = 100
#Issue: Weather converts from string to variable
#Typing weather by itself is not the descriptive!
#We dont know if weather is a int str eg
#So in python you ANNOTATE TYPES
#EG x: int = 10
#or weather:str = 'cloudy'
#Now we can know if we mess up later in our program!3
#Eg now if we try to change weather to value 100 w/out annotaing, code editor will warn "You passed wrong data type"
#If we pass in smth else like 'sunny' no complaints
#data = {'bob' : 1, 'alice' : 2}
#we can do
data: dict[str, int] = {{'bob' : 1, 'alice' : 2}}
#string is key, int is the value assigned to key!!!
#Now we are extra explicit abt what we are doing w/ data
#class fruit
#fruit: Fruit = Fruit()