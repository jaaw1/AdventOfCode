import re


def find_words_with_integer(text):
    pattern = r'\b(\d+)\s+(red|green|blue)\b'  # Define your words in place of word1, word2, word3
    matches = re.findall(pattern, text)

    return matches


def find_game_integer(text):
    pattern = r'\b(?:word1|game|Game)\s+(\d+)\b'  # Define your words in place of word1, word2, word3
    matches = re.findall(pattern, text)

    return int(matches[0])


colors = {
    'red': 12,
    'green': 13,
    'blue': 14,
    }


#print(colors['red'])
# Example text
sample_text = "2 blue, 1 red, 2 green"

result = find_words_with_integer(sample_text)
#print(result)
# Output: [('word1', '42'), ('word2', '10'), ('word3', '5')]


data = open('day2_input.txt', 'r')
Lines = data.readlines()

test_data = open('test_data_day2.txt', 'r')
Test_Lines = test_data.readlines()

id_count = 0

all_powers = 0

for line in Lines:
    cleaned = line.split('\n')[0]
    sliced = cleaned.split(';')
    game_id = find_game_integer(sliced[0])
    print("Game", game_id)
    possible = True

    # Create dictionary for adding the highest minimum number count the colors
    color_counts = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for game in sliced:
        #print(game)

        counted = find_words_with_integer(game)

        for color in counted:
            color_key = color[1]
            color_value = int(color[0])

            if color_value > color_counts[color_key]:
                color_counts[color_key] = color_value

            #print(color_key)
            #print(colors[color_key])
            #print(type(colors[color_key]))
            #print(type(color_value))
            #print(colors[color_key], color_value)
            if colors[color_key] < color_value:
                possible = False
            #else:
                #print(colors[color_key], "is equal to/bigger than", color_value)

    if possible:
        print("Game ", game_id, " is possible")
        id_count += game_id

    # get the power of the set
    power_of_set = 1
    for key in color_counts:
        #print(color_counts[key])
        power_of_set *= color_counts[key]

    print(power_of_set)
    all_powers += power_of_set
            #print(color[1])
        #print(find_game_integer(game))
        #print(counted)
print("SCORE:", end="")
print(id_count)
print("POWERS:", end="")
print(all_powers)