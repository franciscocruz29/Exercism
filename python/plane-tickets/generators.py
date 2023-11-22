"""Functions to automate Conda airlines ticketing system."""

def generate_seat_letters(number):
    """
    Generate a series of seat letters for an airline.

    This function creates a cycle of seat letters from 'A' to 'D'. 
    Once 'D' is reached, it starts again from 'A'.

    Args:
    number (int): The total number of seat letters to be generated.

    Yields:
    str: The next seat letter in the sequence.

    Example:
        generate_seat_letters(6) would yield 'A', 'B', 'C', 'D', 'A', 'B'.
    """

    START_LETTER = 'A'
    END_LETTER = 'D'
    NUM_LETTERS = ord(END_LETTER) - ord(START_LETTER) + 1

    for index in range(number):
        letter_offset = index % NUM_LETTERS
        yield chr(ord(START_LETTER) + letter_offset)

def generate_seats(number):
    """
    Generate a series of seat numbers for an airplane, each combining a row number with a seat letter (A to D).
    Skips row 13 in the numbering sequence.

    Args:
    number (int): Total number of seats to be generated.

    Yields:
    str: The next seat number in the format 'row letter'.

    Example:
        generate_seats(5) would yield '1A', '1B', '1C', '1D', '2A'.
    """

    SEATS_PER_ROW = 4
    SKIPPED_ROW = 13

    if number < 1:
        raise ValueError("Number of seats must be a positive integer.")

    seat_letters = generate_seat_letters(number)
    for seat_index in range(1, number + 1):
        row = (seat_index - 1) // SEATS_PER_ROW + 1  # Calculate row number
        if row >= SKIPPED_ROW:
            row += 1  # Adjust for the absence of row 13

        seat_letter = next(seat_letters)
        yield f"{row}{seat_letter}"

def assign_seats(passengers):
    """
    Assign seats to passengers in the order they appear in the list. Each passenger is assigned a unique seat.

    Args:
    passengers (list of str): A list of passenger names.

    Returns:
    dict: A dictionary mapping each passenger to a unique seat number.

    Raises:
    ValueError: If passengers is not a list or contains non-string elements.

    Example:
        assign_seats(['Jerimiah', 'Eric', 'Bethany', 'Byte', 'SqueekyBoots', 'Bob']) 
        would return {'Jerimiah': '1A', 'Eric': '1B', 'Bethany': '1C', 'Byte': '1D', 'SqueekyBoots': '2A', 'Bob': '2B'}
    """

    if not isinstance(passengers, list) or not all(isinstance(p, str) and p for p in passengers):
        raise ValueError("Passengers must be a list of non-empty strings.")

    seat_generator = generate_seats(len(passengers))
    return {passenger: next(seat_generator) for passenger in passengers}

def generate_codes(seat_numbers, flight_id):
    """
    Generate 12-character long ticket codes for a flight. Each code consists of a seat number, 
    followed by the flight ID, and is padded with zeros to reach a total length of 12 characters.

    Args:
    seat_numbers (list of str): List of seat numbers.
    flight_id (str): Flight identifier.

    Yields:
    str: A 12-character long ticket code.

    Raises:
    ValueError: If the input types are incorrect or the combined length of seat number and flight ID exceeds 12 characters.

    Example:
        generate_codes(['1A', '17D'], 'CO1234') would yield '1ACO12340000', '17DCO1234000'.
    """

    CODE_LENGTH = 12

    if not all(isinstance(seat, str) for seat in seat_numbers) or not isinstance(flight_id, str):
        raise ValueError("Seat numbers and flight ID must be strings.")

    for seat_number in seat_numbers:
        combined_length = len(seat_number) + len(flight_id)
        if combined_length > CODE_LENGTH:
            raise ValueError("The combined length of seat number and flight ID exceeds 12 characters.")

        yield f"{seat_number}{flight_id}{'0' * (CODE_LENGTH - combined_length)}"
