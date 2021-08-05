#!/usr/bin/env python
# coding: utf-8

# In[3]:


#PRODUCTS DICTIONARY
products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

#FUNCTIONS

#Problem 1: Product Information Lookup
def get_product(code):
    return products[code]

#Problem 2: Product Property Lookup
def get_property(code, property):
    return get_product(code)[property]

#Problem 3: The Point-of-Sale Terminal
def main():
    orders_dict = {}
    total = 0
    
    while True:
        order = input().split(',')
        
        if order[0] == '/':
            break
        elif order[0] not in products:
            pass
        elif order[0] in products:
            if order[0] in orders_dict:
                orders_dict[order[0]] = orders_dict[order[0]] + int(order[1])
            else:
                orders_dict[order[0]] = int(order[1])
    
    sorted_orders = sorted(orders_dict)    
    
    with open('receipt.txt', 'w') as receipt:
        receipt.write('''
    ==
    CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
    ''')
    
        subtotal_allproducts = []
        
        for product_code in sorted_orders:
            name = get_property(product_code,'name')
            quantity = orders_dict[product_code]
            subtotal = int(get_property(product_code, 'price')) * quantity
            subtotal_allproducts.append(subtotal)
            
            receipt.write(f"\n{product_code})\t\t{name}\t\t{quantity}\t\t\t\t{subtotal}")
            
        total = sum(subtotal_allproducts)
        receipt.write(f'''\nTotal:\t\t\t\t\t\t\t\t\t\t{total}
    ==
    ''')

#CALL MAIN
main()


# In[5]:


get_ipython().system('cat receipt.txt')


# In[ ]:




