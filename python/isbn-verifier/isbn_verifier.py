def verify(isbn):
    try:
        clean_isbn = isbn.replace('-', '')
        total_sum = 0
        for index, digit in enumerate(clean_isbn[:-1]):
            total_sum += (10-index) * int(digit)
        total_sum += 10 if clean_isbn[-1] == 'X' else int(clean_isbn[-1])
        return total_sum % 11 == 0
    except:
        return False
