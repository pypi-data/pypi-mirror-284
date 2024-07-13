def train_seat(seat_number):

    if seat_number > 0 and seat_number < 73:
        if seat_number % 8 == 1 or seat_number % 8 == 4:
            print("seat is lower",seat_number)
        elif seat_number % 8 == 2 or seat_number % 8 == 5:
            print("seat is middle",seat_number)
        elif seat_number % 8 == 3 or seat_number % 8 == 6:
            print("seat is upper",seat_number)
        elif seat_number % 8 == 7:
            print("seat is side lower",seat_number)
        else:
            print("seat is side upper",seat_number)
        
    else:
        print("invalid seat number")
