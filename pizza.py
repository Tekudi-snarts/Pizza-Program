import tkinter as tk
from tkinter import ttk     

#slection on pizza choices, adding cost to the order
def calculate():
    total_price = 0
    if selected_pizza_1.get() in regular_pizzas:
        total_price+=8.50
    elif selected_pizza_1.get() in gourmet_pizzas:
        total_price+=12
    if selected_pizza_2.get() in regular_pizzas:
        total_price+=8.50
    elif selected_pizza_1.get() in gourmet_pizzas:
        total_price+=12
    if selected_pizza_3.get() in regular_pizzas:
        total_price+=8.50
    elif selected_pizza_1.get() in gourmet_pizzas:
        total_price+=12
    if selected_pizza_4.get() in regular_pizzas:
        total_price+=8.50
    elif selected_pizza_1.get() in gourmet_pizzas:
        total_price+=12
    if selected_pizza_5.get() in regular_pizzas:
        total_price+=8.50
    elif selected_pizza_1.get() in gourmet_pizzas:
        total_price+=12

    total_money_label.configure(text="{}".format(total_price))

regular_pizzas = ["Cheese", "Cheesy Garlic", "Pineapple, sausage", "Chocolate", "Racism", "Mr.Malaitai", "vegetales"]

gourmet_pizzas = ["Guilty Pleasure", "Anti-Vegan", "Big Boy Banger", "Fortnite", "Doja 'CAT'"]

#Decide what details to collect
root=tk.Tk

def transport():
    if transport_method.get() == 0:
        print("Pick up")
        address_entry.configure(state=tk.DISABLED)
        phone_entry.configure(state=tk.DISABLED)
    elif transport_method.get() == 1:
        print("Delivery")  
        address_entry.configure(state=tk.ACTIVE)
        phone_entry.configure(state=tk.ACTIVE)


#display total order
    if transport_method.get() == 0:
        order_label.configure(text="Order:\nCost:{}\nCustomer Name:{}".format(total_price, name_entry.get()))
    elif transport_method.get() == 1:
        total_price += 3
        order_label.configure(text="Order:\nCost:{}\nCustomer Name:{}\nAddress:{}\nPhone Number:{}".format(total_price, name_entry.get(), phone_entry.get(),address_entry.get()))




root = tk.Tk()

transport_method = tk.IntVar()
transport_method.set(0)

#Name of the ordering system, name of pizza lists
title_label = ttk.Label(root, text="Pizza ordering system", font='ComicSansMS 16 bold')
title_label.grid(row=1, column=0, columnspan=4, padx=100, pady=25)

regular_pizza_label = ttk.Label(root, text="Regular Pizza ($8.50)", font='ComicSansMS 12 bold')
regular_pizza_label.grid(row=2, column=0, padx=50, pady=15)

gourmet_pizza_label = ttk.Label(root, text="Gourmet Pizza $12", font='ComicSansMS 12 bold')
gourmet_pizza_label.grid(row=2, column=3, padx=50, pady=15)

#Labels for the normal pizza's
cheese_pizza_label = ttk.Label(root, text="Cheese Pizza")
cheese_pizza_label.grid(row=3, column=0, pady=10)

garlic_pizza_label = ttk.Label(root, text="Cheesey Garlic Pizza")
garlic_pizza_label.grid(row=4, column=0, pady=10)

pineapple_pizza_label = ttk.Label(root, text="Pineapple and Sausage 346")
pineapple_pizza_label.grid(row=5, column=0, pady=10)

chocolate_pizza_label = ttk.Label(root, text="Chocolate Pizza")
chocolate_pizza_label.grid(row=6, column=0, pady=10)

racism_pizza_label = ttk.Label(root, text="Racism (half burnt half raw) Pizza")
racism_pizza_label.grid(row=7, column=0, pady=10)

vegan_pizza_label = ttk.Label(root, text="The Mr Malaitai (Vegan) Pizza")
vegan_pizza_label.grid(row=8, column=0, pady=10)

vegetarian_pizza_label = ttk.Label(root, text="End of Vegetales Pizza")
vegetarian_pizza_label.grid(row=9, column=0, pady=10)


#This is all the labels for the gourmet pizza's
guilty_pizza_label = ttk.Label(root, text="The Guilty Pleasure Pizza")
guilty_pizza_label.grid(row=3, column=3, pady=10)

anti_pizza_label = ttk.Label(root, text="The Anti Vegan Pizza")
anti_pizza_label.grid(row=4, column=3, pady=10)

big_pizza_label = ttk.Label(root, text="The Big Boy Banger Pizza")
big_pizza_label.grid(row=5, column=3, pady=10)

fortnite_pizza_label = ttk.Label(root, text="The Fortnite Pizza")
fortnite_pizza_label.grid(row=6, column=3, pady=10)

cat_pizza_label = ttk.Label(root, text="The Doja 'Cat' Pizza")
cat_pizza_label.grid(row=7, column=3, pady=10)

#buttons for delievery or takeaway (radio button)
var = tk.IntVar()
delivery_rb = ttk.Radiobutton(root , text="Delivery", variable=var, value=1, command=transport)
delivery_rb.grid(row=10, column=0, pady=25)

takeaway_rb = ttk.Radiobutton(root , text="Takeaway", variable=var, value=0, command=transport)
takeaway_rb.grid(row=10, column=3, pady=25)

#enter details (ttk.entry)
name_entry = ttk.Entry(root)
name_entry.grid(row=11, column=3, padx=5, pady=10)

name_label = ttk.Label(root, text="Name:")
name_label.grid(row=11, column=0, padx=5, pady=10)

phone_entry = ttk.Entry(root)
phone_entry.grid(row=12, column=3, padx=5, pady=10)

phone_label = ttk.Label(root, text="Phone number:")
phone_label.grid(row=12, column=0, padx=5, pady=10)

address_entry = ttk.Entry(root)
address_entry.grid(row=13, column=3, padx=5, pady=10)

address_label = ttk.Label(root, text="Address:")
address_label.grid(row=13, column=0, padx=5, pady=10)


#Select pizza combobox
selected_pizza_1 = tk.StringVar()
selected_pizza_1.set("Select a pizza!")
pizza_menu = ttk.Combobox(root, textvariable=selected_pizza_1)
pizza_menu.grid(row=14, column=0, padx=10, pady=5)
pizza_menu['values'] = ["Cheese", "Cheesy Garlic", "Pineapple, sausage", "Chocolate", "Racism", "Mr.Malaitai", "vegetales", "Guilty Pleasure", "Anti-Vegan", "Big Boy Banger", "Fortnite", "Doja 'CAT'"]
pizza_menu['state'] = 'readonly'

selected_pizza_2 = tk.StringVar()
selected_pizza_2.set("Select a pizza!")
pizza2_menu = ttk.Combobox(root, textvariable=selected_pizza_2)
pizza2_menu.grid(row=15, column=0, padx=10, pady=5)
pizza2_menu['values'] = ["Cheese", "Cheesy Garlic", "Pineapple, sausage", "Chocolate", "Racism", "Mr.Malaitai", "vegetales", "Guilty Pleasure", "Anti-Vegan", "Big Boy Banger", "Fortnite", "Doja 'CAT'"]
pizza2_menu['state'] = 'readonly'

selected_pizza_3 = tk.StringVar()
selected_pizza_3.set("Select a pizza!")
pizza3_menu = ttk.Combobox(root, textvariable=selected_pizza_3)
pizza3_menu.grid(row=16, column=0, padx=10, pady=5)
pizza3_menu['values'] = ["Cheese", "Cheesy Garlic", "Pineapple, sausage", "Chocolate", "Racism", "Mr.Malaitai", "vegetales", "Guilty Pleasure", "Anti-Vegan", "Big Boy Banger", "Fortnite", "Doja 'CAT'"]
pizza3_menu['state'] = 'readonly'

selected_pizza_4 = tk.StringVar()
selected_pizza_4.set("Select a pizza!")
pizza4_menu = ttk.Combobox(root, textvariable=selected_pizza_4)
pizza4_menu.grid(row=17, column=0, padx=10, pady=5)
pizza4_menu['values'] = ["Cheese", "Cheesy Garlic", "Pineapple, sausage", "Chocolate", "Racism", "Mr.Malaitai", "vegetales", "Guilty Pleasure", "Anti-Vegan", "Big Boy Banger", "Fortnite", "Doja 'CAT'"]
pizza4_menu['state'] = 'readonly'

selected_pizza_5 = tk.StringVar()
selected_pizza_5.set("Select a pizza!")
pizza5_menu = ttk.Combobox(root, textvariable=selected_pizza_5)
pizza5_menu.grid(row=18, column=0, padx=10, pady=5)
pizza5_menu['values'] = ["Cheese", "Cheesy Garlic", "Pineapple, sausage", "Chocolate", "Racism", "Mr.Malaitai", "vegetales", "Guilty Pleasure", "Anti-Vegan", "Big Boy Banger", "Fortnite", "Doja 'CAT'"]
pizza5_menu['state'] = 'readonly'

#Total, etc

total_label = ttk.Label(root, text="Your Order:", font='ComicSansMS 12 bold')
total_label.grid(row=19, column=0, pady=20)

total_money_label = ttk.Label(root, text="", font='ComicSansMS 12 bold')
total_money_label.grid(row=19, column=3, pady=20)

b1 = ttk.Button(root, text="Complete Order",command=calculate)
b1.grid(row=20, column=0)

root.mainloop()
