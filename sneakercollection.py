print('This Will Record Your Sneaker Collection!')
sneakers=[]
while True:
    name=input('What Is The Name Of Shoe #' +str(len(sneakers) +1) +' (or enter nothing to stop): ')
    if name == '':
        break
    sneakers= sneakers + [name]
print('So here is your sneaker collection: ')
for name in sneakers:
    print(' ' + name)
    
while True:
    print('Did you forget a sneaker?: ')
    confirm=input()
    if confirm.lower()=='no':
        break
    if confirm.lower()=='yes':
        xtraname=input('What was the name of the sneaker?: ')
    sneakers=sneakers +[xtraname]
print('Here is your sneaker collection(updated): ')
for name in sneakers:
    print(name)

input('Press ENTER to Stop')

