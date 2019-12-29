def table(filename_in, filename_out, width):
    with open(filename_in, "r") as file_out:
        listt = file_out.readlines()
        for i in range(len(listt)):
            listt[i] = listt[i].rstrip("\n")
            listt[i] = listt[i] + " " * width
            listt[i] = listt[i][:width]

    with open(filename_out, "w") as file_out:
        head = "+{0}+".format("-"*(width + 2))
        output = [head + "\n"]
        for j in range(len(listt)):
            output.append("| {0} |\n".format(listt[j]))
        output.append(head)

        file_out.writelines(output)
