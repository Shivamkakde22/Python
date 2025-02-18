def election_year(year):
    first_election = 2000
    if year >= first_election:
        return True
    elif(first_election - year)%5==0:
        return True
    return False

year = int(input("Enter the year: "))
if election_year(year):
    print(year,"is an election year")
else:
    print(year,"is not an election year")
    
