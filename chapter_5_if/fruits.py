# 5-7: Favorite Fruit
# Make a list of your three favorite fruits and call it favorite_fruits.

def common_fruit(list1, list2): 
    # traverse in the 1st list 
    for x in list1: 
        # traverse in the 2nd list 
        for y in list2: 
            # if one common 
            if x == y: 
                print(f'I like {y} too.')

      
my_fruits = ['apples', 'oranges', 'blueberries']
your_fruits = ['bananas', 'apples', 'blueberries','kiwis', 'peaches']

print(common_fruit(my_fruits, your_fruits)) 
