# DunnDelivery class demonstrates core OOP concepts
# Encapsulation: data (menu and prices) and methods are bundled in the class
# Abstraction: complex delivery logic hiddem behind method calls

class DunnDelivery:
# Constructor method - create new instance of a delivery
    def __init__(self):
    #inside constructor-set class attributes(pieces of data that describe class)
        pass

    
    # override calculate_total to apply discount for 5 or more items
    def calculate_total(self, items, has_student_id=False):
        total = super().calculate_total(items, has_student_id)

        # apply group discount 10% if 5 or more items are ordered
        if len(items) >= 5:
            group_discount = 0.10 * total # 10% discount for study group
            total -= group_discount
            print(f"Group discount applied: -${group_discount:.2f}")

        return total
    
# Define StudyGroupOrder class
class StudyGroupOrder(DunnDelivery): 
    def __init__(self):
        # initialize the parent class
        super().__init__()

    def combine_orders(self, group_orders):
        # combine study groups into one and apply group discount
        # group_orders is a lsit of lists, each inner list represents an individual order
        combined_items = [] # initialize an empty list to combine all items from group orders

        # combine all items from each group into one list
        # loop through each group order - add items to combined list
        for order in group_orders:
            combined_items.extend(order)

        # display the combined order
        print("\n=== Combined Study Group Order ===")
        print(f"Total items ordered: {len(combined_items)}")
        print(f"Items: {combined_items}")

        # check if order qualifies for group discount
        if len(combined_items) >= 5: # if combined_items great than or equal to 5
            print("Group discount applied!") # discount applied
        else:
            print("No group discount applied.") # else no discount

        # call calculate_total to get final price with or without discount
        total = self.calculate_total(combined_items) 

        # display total cost
        print(f"Total after applying any discount: ${total:.2f}") # format total cost with .2f
        return combined_items
    
        # MENU FOR DIRNKS 
        # menu attribute - menu of items you can order to be delivered
        self.menu = {
            # using dictionary with key and values
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee": ["Latte", "Cappuccino", "Miel", "Espresso", "Americana"], # add 3 more coffee drinks
            "Breakfast Items": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Falafel Wrap", "Hummus and Pita", "Chicken Wrap"]
        }

        # DRINK PRICES WITHIN CLASS
        # Prices encapsulated within the class
        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Latte": 4.99, "Cappuccino": 4.99, "Miel": 3.99, "Espresso": 4.99, "Americana": 4.99, # add 3 more coffee drink prices 
            "Bagel": 2.99, "Muffin": 2.99, "Scone": 2.99,
            "Falafel Wrap": 8.99, "Hummus and Pita": 7.99, "Chicken Wrap": 8.99
        }

        # DELIVERY LOCATIONS
        # Delivery locations and number of minutes to deliver to that location
        self.delivery_locations = {
            "Library": 10,
            "Academic Success Center": 8,
            "Itec Computer Lab": 5
        }

    # LOOP THROUGH ITEMS FOR DELIVERY
    # show menu of items available for delivery
    def show_menu(self, category=None):
        if category: 
            # show menu items for chosen category
            print(f"\n=== {category} ===")
            # loop thru items in specific category on the menu
            # display them to user
            for item in self.menu[category]:
                print(f"{item}: ${self.prices[item]:.2f}") #2f to format decimal point
        # add else of if else statement
        else:
            # SHOW ENTIRE MENU
            for category in self.menu: # show category name
                print(f"\n=== {category} ===") # category variable
                # nested for loop - go thru each item in category
                for item in self.menu[category]:
                    print(f"{item}: ${self.prices[item]:.2f}")

    def search_under_price_items(self, max_price): 
        # Search for item under specified price
        print(f"\nItems under ${max_price:.2f}:") # print max price - part of heading
        found = False # for tracking items if found - track whether item meets condition or not
        for item, price in self.prices.items(): # loop thry menu items and prices
            if price < max_price: # check if item price is less than max price
                print(f"- {item}: $ {price:.2f}") # print item name and it's price
                found = True # tracker set to true since a matching item found
        if not found: # if item does not meet condition - print the message
            print("No items found under that price")

    # CALCULATE ORDER COST METHOD
    # method to calculate total cost of order
    def calculate_total(self, items, has_student_id=False):
        # calculate the total
        total = sum(self.prices[item] for item in items)

        # CALCULATE DISCOUNT
        # calculate the discount based on the student id 
        if has_student_id and total > 10:
            total *= 0.9
        # this method returns total cost of order to code
        # that called the method
        return total;

    # CALCULATE DELIVERY TIME
    # method to calculate the delivery time based on location and time of dat
    def estimate_delivery(self, location, current_hour):
        # calculate the base time
        base_time = self.delivery_locations[location]

        # calculate delivery time based on time of day
        if(9 <= current_hour <= 10) or (11 <= current_hour <= 13):
            return base_time + 5
        
        # if not ordering during busy time, return base time with no adjustment
        return base_time

    # PRINT ORDER 
    # method prints order
    def print_order(self, location, items, current_hour, has_student_id=False):
        # display order info
        print("\n=== Order Summary ===")
        print(f"Delivery to {location}")
        print(f"\nItems Ordered:")
        # loop thru list of menu items ordered
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")

        # CALL METHODS FOR TOTAL COST AND DELIVERY TIME
        subtotal = sum(self.prices)
        total = self.calculate_total(items, has_student_id);
        delivery_time = self.estimate_delivery(location, current_hour)

        # ASK USER IF THEY WANT PRIORITY DELIVERY
        print("\nWould you like priority delivery? It costs $2 extra dollars and reduces delivery time by 3 minutes. (Yes/no)?")
        priority = input("> ").lower()
        if priority == "yes":
            total += 2 # add $2 dollars for priority delivery
            delivery_time -= 3 # reduce delivery time by 3 minutes 
            print("\nPriority delivery selected!")


        # DISPLAY SUBTOTAL
        print(f"\nSubtotal: ${sum(self.prices[item] for item in items):.2f}")
        # calculate total with discount if customer has student id
        if has_student_id and total < sum(self.prices[item] for item in items):
            print("Student discount applied")

        # DISPLAY TOTAL AFER discount and delivery time
        print(f"Total after discount: ${total:.2f}")
        print(f"Estimated delivery time: {delivery_time} minutes")

    def rate_delivery(self):
        # Prompt customer to rate the delivery and store the rating
        print("\nPlease rate your delivery. Choose a number between 1 and 5 stars:")
        rating = input("> ") # get input from the user

        # validate the user's rating
        if rating in ["1", "2", "3", "4", "5"]: # check if user input is valid
            self.ratings.append(int(rating)) # covert to an int and store it
            print(f"Thank you for rating us {rating} stars!") # print message with the rating using {}
        else:
            print(f"Invalid rating. Please choose a number between 1 and 5.")

    



def main():
    # create new delivery object - instantiating new object
    delivery = DunnDelivery()

    # show the menu 
    delivery.show_menu("Coffee")

    # sample order at 930am
    order = ["Latte", "Bagel"]

    # display receipt for order
    delivery.print_order("Itec Computer Lab", order, 9, has_student_id=True);

    # call the rating method
    delivery.rate_delivery() # prompt user to rate their delivery

# add the line of code to automatically call the main method 
if __name__ == "__main__":
    main()