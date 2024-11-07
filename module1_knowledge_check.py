#odd_or_even
def odd_or_even (number):
  return "Even" if number % 2 == 0 else "Odd"
odd_or_even(11)

#number_to_string
def number_to_string(num):
    # Return a string of the number here!
    string_num = str(num)
    return string_num
number_to_string(10)

#vowel_count
def get_count(sentence):
    vowels = 'aeiou'
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count
#return outputs value
get_count("abracadabra") 