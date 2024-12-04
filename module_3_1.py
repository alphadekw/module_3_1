calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return upper, lower, length


def is_contains(string, list_to_search):
    count_calls()
    string_low = string.lower()
    return string_low in (i.lower() for i in list_to_search)

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['ccle', 'cyclic'])) # No matches

print(calls)

