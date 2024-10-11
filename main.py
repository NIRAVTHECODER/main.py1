

# f is format to apply variables in string   
#Boolean

#_____________________________________
import random
fortune_number= random.randint(4,6)
lucky_fortune=random.randint(1,100)
fortune_text=''
if fortune_number == 4:
    fortune_text ="Kavin is Cooked"

if fortune_number == 5:
    fortune_text="Kavin is Not Cooked"

if fortune_number == 6:
    fortune_text = "Kavin is cooking"

print(f"Your Fortune is {fortune_text} and you number is {lucky_fortune}")

#____________________________________________________________________________________
#print first number
fav_num = [1,2,3]
print(fav_num[0])

fav_num.insert(1,"SKIBIDIMAN")
print(fav_num)

del(fav_num[2])
print(fav_num)

movies = ["spiderman","batman","superman","poop","pee"]
for number in range(40):
 print(number*2)

#pooptionary
cats={"poop":123, "Tom":400, "pee":8}
print(cats["poop"])
cats["poop"] = 1

del(cats["Tom"])

print(cats)

inkey={1:True,2:False}

print(inkey)    
#________________________________________________________________________________________
number=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in number:
    if(i%2==0):     
       sum=i+sum
print(sum)
#____________________________________________________________________________----
text = """Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.
But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth
Abraham Lincoln"""
print(len(text.split()))

word_count={}

for word in text.split():
    if word in word_count:
       word_count[word]+=1
    else:
       word_count[word] = 1

    
print(word_count)
#_______________________________________________________________

def dog_info (name,age):
    print(f"This dogs name is {name} and it's {age}")

dog_info("Lucy",2)
#_________________________________________________________________________

def to_uppercase(word):
    return word.upper()

# Example usage
print(to_uppercase("hello"))  # Output: HELLO


namesage = {0:"pavan",1:"shirisha",2:"bunSun"}
print(namesage.keys())
print(namesage.values())
print(namesage)

namesage = {"pavan":46,"shirisha":42, "bunSun":13}


for i in namesage.keys():
    print(i)
    print(to_uppercase(f"{i} is {namesage[i]}"))
print(namesage["pavan"])
#___________________________________________________________________________
wallet = 40#poop
wallet-=2#poop
wallet+=40#poop
#poop#poop#poop#poop#poop#poop#poop#poop#poop#poop#poop#poop#poop        

#user_text =input('enter some text')

#print(to_uppercase(user_text))
#enter text
#user_number = input("Enter number")
#enter number
#print(float(user_number)*2)



#______________________________________________
#uppercase = input("enter 1 for uppercase")
#print(to_uppercase(user_text))

#lowercase = input("enter 2 for lower case")
#print(user_text.lower())
#up_or_lower = input("If you want to uppercase press 1, or if you want to lowercase press 2: ")
#if (int(up_or_lower)== 1):
 #print(to_uppercase(user_text))

 #if (int(up_or_lower) == 2):
    #print(user_text.lower())
#else:
    #print("invalid input")
    
def has_remainder(number1,number2):
    
    if (number1%number2 == 0):
        print("No remainder")
    else:
        print("Has a remainder")
num1 = input("Enter Your First Number: ")
num2 = input("Enter Your Second Number: ")
has_remainder(int(num1),int(num2))
#_____________________________________________________________