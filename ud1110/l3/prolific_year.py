def most_prolific(discography):
    years = list(discography.values())
    max_count = 0
    count_years = {}
    for year in years:
        count = years.count(year)
        if count_years.get(count):
            count_years[count].add(year)
        else:
            count_years[count] = set([year])

    prolific_year = count_years[max(count_years)]
    if len(prolific_year) > 1:
        return prolific_year
    else:
        return prolific_year.pop()

test1= {"Please Please Me": 1963, "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964,
    "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

test2 = {'Rubber Soul': 1965, 'Magical Mystery Tour': 1967,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967, 'Revolver': 1966,
    'The Beatles': 1968, 'With the Beatles': 1963,
    'Beatles for Sale': 1964, 'Yellow Submarine': 1969,
    "A Hard Day's Night": 1964, 'Help': 1965, 'Let It Be': 1970,
    'Abbey Road': 1969, 'Twist and Shout': 1964, 'Please Please Me': 1963}

test3 = {'The Game': 1980, 'A Night at the Opera': 1975,
    'Jazz': 1978, 'Queen II': 1974, 'A Day at the Races': 1976,
    'News of the World': 1977, 'Queen': 1973, 'Sheer Heart Attack': 1974}

print(most_prolific(test1))
print(most_prolific(test2))
print(most_prolific(test3))
