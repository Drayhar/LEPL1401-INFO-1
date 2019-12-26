def extract(code):
    vowel_up = "AEIOUY"
    vowel_low = "aeiouy"
    consonant_up = "BCDFGHJKLMNPQRSTVWXZ"
    consonant_low = "bcdfghjklmnpqrstvwxz"
    number = "1234567890"
    answer = ""
    for i in code:
        if i in number:
            answer += "number"
        elif i in vowel_up:
            answer += "vowel-up"
        elif i in vowel_low:
            answer += "vowel-low"
        elif i in consonant_up:
            answer += "consonant-up"
        elif i in consonant_low:
            answer += "consonant-low"
        answer += " "
    return answer
