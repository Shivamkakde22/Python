def is_valid_date(day, month, year):
  

  # Check for invalid month or day values
  if month < 1 or month > 12:
    return False
  if day < 1 or day > 31:
    return False

  # Check for leap year
  if month == 2:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # Leap year
      return day <= 29
    else:
      return day <= 28

  # Check for month lengths
  if month in (4, 6, 9, 11):
    return day <= 30
  else:
    return True

# Example usage
date_str = input("Enter date (DD-MM-YYYY): ")
day, month, year = map(int, date_str.split("-"))

if is_valid_date(day, month, year):
  print("Valid date")
else:
  print("Invalid date")