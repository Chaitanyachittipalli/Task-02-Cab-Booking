import random

def cab_booking_chatbot():
    print("=" * 45)
    print("      WELCOME TO CAB BOOKING CHATBOT")
    print("=" * 45)

    # 1. Main menu infinite loop
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Book Ride")
        print("2. Exit")
        
        main_choice = input("Enter your choice (1 or 2): ").strip()

        # Step 7: Exit condition
        if main_choice == '2':
            print("\nThank you for using our Cab Booking Service. Have a great day!")
            break

        # Step 1: Book Ride
        elif main_choice == '1':
            
            # Step 2: Choose cab type
            print("\nSelect Cab Type:")
            print("1. Auto  - Rs. 12/km")
            print("2. Sedan - Rs. 18/km")
            print("3. SUV   - Rs. 25/km")
            
            cab_choice = input("Enter your choice (1-3): ").strip()
            
            if cab_choice == '1':
                cab_type = "Auto"
                rate_per_km = 12
            elif cab_choice == '2':
                cab_type = "Sedan"
                rate_per_km = 18
            elif cab_choice == '3':
                cab_type = "SUV"
                rate_per_km = 25
            else:
                print("Invalid Cab Type! Returning to Main Menu.")
                continue

            # Step 3: Choose route
            print("\nSelect Route:")
            print("1. Pune Station to Shivajinagar (5 km)")
            print("2. Swargate to Kothrud (8 km)")
            print("3. Hinjawadi to Wakad (10 km)")
            
            route_choice = input("Enter route choice (1-3): ").strip()
            
            if route_choice == '1':
                source = "Pune Station"
                destination = "Shivajinagar"
                distance = 5
            elif route_choice == '2':
                source = "Swargate"
                destination = "Kothrud"
                distance = 8
            elif route_choice == '3':
                source = "Hinjawadi"
                destination = "Wakad"
                distance = 10
            else:
                print("Invalid Route Selection! Returning to Main Menu.")
                continue

            # Step 4: Calculate fare
            total_fare = distance * rate_per_km

            print("\n" + "=" * 35)
            print("          RIDE DETAILS")
            print("=" * 35)
            print(f"Cab Type    : {cab_type}")
            print(f"Route       : {source} -> {destination}")
            print(f"Distance    : {distance} km")
            print(f"Rate        : Rs. {rate_per_km}/km")
            print(f"Total Fare  : Rs. {total_fare}")
            print("=" * 35)

            # Step 5: Cancellation before OTP
            print("\nConfirm Booking:")
            print("1. Confirm & Share OTP")
            print("2. Cancel Ride")
            
            confirm_choice = input("Enter choice (1 or 2): ").strip()

            if confirm_choice == '2':
                print("\n[Ride Cancelled] Your ride has been cancelled successfully.")
                print("Returning to Main Menu...")
                continue
            elif confirm_choice == '1':
                # Step 6: Generate 4-digit OTP and lock ride
                otp = random.randint(1000, 9999)
                print("\n" + "*" * 45)
                print("           BOOKING CONFIRMED!")
                print(f"Your 4-Digit OTP is: {otp}")
                print("RULE: OTP has been shared. Cancellation is strictly NOT allowed now.")
                print("*" * 45)
            else:
                print("Invalid choice! Ride not confirmed. Returning to Main Menu.")
                continue

        else:
            print("Invalid input! Please enter 1 or 2.")

if __name__ == "__main__":
    cab_booking_chatbot()