# DunnDelivery class demonstrates core OOP concepts
# Encapsulation: data (menu and prices) and methods are bundled in the class
# Abstraction: complex delivery logic hiddem behind method calls

class DunnDelivery:
# Constructor method - create new instance of a delivery
    def __init__(self):
    #inside constructor-set class attributes(pieces of data that describe class)

        # menu attribute - menu of items you can order to be delivered
        self.menu = {
            # using dictionary with key and values
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee": ["Latte", "Cappucino"],
            "Breakfast Items": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Falafel Wrap", "Hummus and Pita", "Chicken Wrap"]
        }

        # Prices encapsulated within the class
        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Latte": 4.99, "Cappucino": 4.99,
            "Bagel": 2.99, "Muffin": 2.99, "Scone": 2.99,
            "Falafel Wrap": 8.99, "Hummus and Pita": 7.99, "Chicken Wrap": 8.99
        }

        # Delivery locations and number of minutes to deliver to that location
        self.delivery_locations = {
            "Library": 10,
            "Academic Success Center": 8,
            "Itec Computer Lab": 5
        }

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
            # show entire menu
            for category in self.menu: # show category name
                print(f"\n=== {category} ===") # category variable
                # nested for loop - go thru each item in category
                for item in self.menu[category]:
                    print(f"{item}: ${self.prices[item]:.2f}")

    # method to calculate total cost of order
    def calculate_total(self, items, has_student_id=False):
        # calculate the total
        total = sum(self.prices[item] for item in items)

        # calculate the discount based on the student id 
        if has_student_id and total > 10:
            total *= 0.9
        # this method returns total cost of order to code
        # that called the method
        return total;

    # method to calculate the delivery time based on location and time of dat
    def estimate_delivery(self, location, current_hour):
        # calculate the base time
        base_time = self.delivery_locations[location]

        # calculate delivery time based on time of day
        if(9 <= current_hour <= 10) or (11 <= current_hour <= 13):
            return base_time + 5
        
        # if not ordering during busy time, return base time with no adjustment
        return base_time

    # method prints order
    def print_order(self, location, items, current_hour, has_student_id=False):
        # display order info
        print("\n=== Order Summary ===")
        print(f"Delivery to {location}")
        print(f"\nItems Ordered:")
        # loop thru list of menu items ordered
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")

        # call the methods to get the total cost and delivery time
        total = self.calculate_total(items, has_student_id);
        delivery_time = self.estimate_delivery(location, current_hour)

        # display subtotal
        print(f"\nSubtotal: ${sum(self.prices[item] for item in items):.2f}")

        # calculate total with discount if customer has student id
        if has_student_id and total < sum(self.prices[item] for item in items):
            print("Student discount applied")

        # display total after discount and delivery time
        print(f"Total after discount: ${total:.2f}")
        print(f"Estimated delivery time: {delivery_time} minutes")


def main():
    # create new delivery object - instantiating new object
    delivery = DunnDelivery()

    # show the menu 
    delivery.show_menu("Coffee")

    # sample order at 930am
    order = ["Latte", "Bagel"]

    # display receipt for order
    delivery.print_order("ITEC Computer Lab", order, 9, has_student_id=True);

# add the line of code to automatically call the main method 
if __name__ == "__main__":
    main()