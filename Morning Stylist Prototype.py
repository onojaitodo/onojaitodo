print('This program will suggest what outfit you should wear today')
name=input("Good Morning! What's your name?: ")
mood=input('Well '+str(name)+',' + " What's your mood today?: ")
goodmood=['Amazing','Happy','Excited','Good','Lit','Great','Thankful']
badmood=['Depressed','Tired','Anxious','Angry','Scared','Bad','Moody']
if str(mood) in goodmood:
    sneakersDict={'Option 1':'Air Jordan 1s','Option 2':'Dress Shoes','Option 3':'Offwhite Vans','Option 4':'Air Jordan 9s','Option 5':'Custom Converse Hightops'}
    shirtDict={'Option 1':'Ralph lauren Polo Shirt','Option 2':'Turtleneck','Option 3':'Furry Sweater','Option 4':'College Dropout Sweatshirt','Option 5':'Rose Colored Furry Sweater'}
    pantsDict={'Option 1':'Cargos','Option 2':'Denim Jeans','Option 3':'Dress Pants','Option 4':'Baggy Levis Jeans'}
    jacketsDict={'Option 1':'Furry Jacket','Option 2':'Puffer Northface Jacket','Option 3':'Leather Jacket'}
    print('Here are your options: ')
    print('For Sneakers')
    print(sneakersDict)
    print('For Shirts')
    print(shirtDict)
    print('For Pants')
    print(pantsDict)
    sneakers=input('Select From Your Footwear Options: ')
    shirt=input('Select From Your Shirt Options: ')
    pants=input('Select From Your Pants Options: ')
if str(mood) in badmood:
    sneakersDict={'Option 1':'Crocs','Option 2':'Running Shoes','Option 3':'New Balance Lowtops','Option 4':'Nike Air Max 90'}
    shirtDict={'Option 1':'Space Sweatshirt','Option 2':'Plain Grey Sweatshirt','Option 3':'Tanktop','Option 4':'Pink Hoodie','Option 5':'Boondocks Graphic Sweater'}
    pantsDict={'Option 1':'Black GAP Sweatpants','Option 2':'Sweatshorts(if it is warm)','Option 3':'Navy Blue Cargos','Option 4':'Black Baggy Levis Jeans'}
    jacketsDict={'Option 1':'OffBrand Puffer Jacket','Option 2':'Windbreaker'}
    print('Here are your options')
    print('For footwear')
    print(sneakersDict)
    print('For Shirts')
    print(shirtDict)
    print('For Pants')
    print(pantsDict) 
    sneakers=input('Select From Your Footwear Options: ')
    shirt=input('Select From Your Shirt Options: ')
    pants=input('Select From Your Pants Options: ')
    
weather=input('Is it Warm or Cold outside?: ')
if weather.lower() == 'cold' and str(mood) in goodmood:
    print('You may want to keep warm then. Here are your jacket options')
    print(jacketsDict)
    jacket=input('Select From Your Jacket Options: ')
    print('Here is your outfit for the day. Enjoy!')
    print(str(shirt) +'\n' +str(pants) +'\n' +str(sneakers) +'\n' +str(jacket))    
if weather.lower() == 'cold' and str(mood) in badmood:
    print('You may need to keep warm. Here are your jacket options')
    print(jacketsDict)
    jacket=input('Select From Your Jacket Options: ')
    print('Here is your outfit for the day. Feel Better!')
    print(str(shirt) +'\n' +str(pants) +'\n' +str(sneakers) +'\n' +str(jacket))    
if weather.lower() == 'warm' and str(mood) in goodmood:
    print('No worries. Here is your outfit for the day. Enjoy!')
    print(str(shirt) +'\n' +str(pants) +'\n' +str(sneakers))
if weather == 'warm' and str(mood) in badmood:
    print('Here is your outfit for the day. Feel Better!')
    print(str(shirt) +'\n' +str(pants) +'\n' +str(sneakers))
input('Press ENTER to exit')
