from datetime import datetime


def sa_id_number(sa_id_number: str):
        if len(sa_id_number) != 13 or not sa_id_number.isdigit():
            return False
        # Extract parts of the ID
        dob = sa_id_number[:6]
        citizenship = int(sa_id_number[10])
        check_digit = int(sa_id_number[-1])

        # Validate date of birth
        try:
            dob = datetime.strptime(dob, '%y%m%d')
        except ValueError:
            return False

        # Validate citizenship
        if citizenship not in [0, 1, 2]:
            return False

        # Calculate checksum using the Luhn algorithm
        def calculate_luhn_checksum(number):
            total = 0
            multiplier = 1
            for digit in number[:-1]:
                digit = int(digit) * multiplier
                if digit > 9:
                    digit = digit - 9
                total += digit
                multiplier = 3 - multiplier
            return (10 - (total % 10)) % 10
        
        calculated_checksum = calculate_luhn_checksum(sa_id_number)
        if calculated_checksum != check_digit:
            return False
        
        return True
