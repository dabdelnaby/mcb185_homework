import math

Y = 'Y'
N = 'N'

# Function to convert quality value symbols to error rates and vice versa
def erqvconverter(x):
    if x == Y:
        char = input('What is your quality value symbol? ')
        v = ord(char) - 33
        return print('1 in every 10 to the', v, 'power.')

    elif x == N:  
        prob = float(input('What is your error rate? '))
        if prob <= 0 or prob >= 1:  # Valid probability range
                return None
        else:
            Q= -10 * math.log10(prob)
            char = chr(int(Q) + 33)  # Convert to ASCII
            return print('Your Quality Value Symbol is', char, '.')

    else:
        return None


qv = input('Is your input a Quality Value Symbol? (Y or N) ')

erqvconverter(qv)
