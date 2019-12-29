def write(letter_template, name):
    with open(letter_template, "r") as file_in:
        msg = ""
        while True:
            temp = file_in.read(1)
            if temp == "#":
                temp = name
            elif temp == '':
                break
            msg += temp

    with open(letter_template, "w") as file_out:
        file_out.write(msg)
