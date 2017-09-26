#Created by : Khoa Le
#Created on : 26 Sept. 2017
#Created for : ICS3UR
# This program calculates the cost of a pizza with the diameter inputed by user

import ui

def calculate_touch_up_inside(sender):
    #This calculates the price of the pizza
    
    #Constant
    LABOUR_COST = 0.75
    RENT_COST = 1.00
    MATERIALS_COST = 0.50
    HST = 1.13
    
    #input
    diameter = float(view['diameter_textbox'].text)
    
    #process
    total_cost = (LABOUR_COST+RENT_COST+MATERIALS_COST*diameter)*HST
    
    #output
    view['price_of_pizza_label'].text = "The cost is : "+"${:,.2f}".format(total_cost)
    
view = ui.load_view()
view.present('sheet')
