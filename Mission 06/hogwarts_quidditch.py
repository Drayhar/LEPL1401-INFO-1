def referee(score_file):
    with open(score_file, "r") as _:
        wholeList = ['A\n', 'B\n', 'A 10\n', 'B 10\n', 'A 10\n', 'A 10\n',
                     'B 10\n', 'A 10\n', 'A 10\n', 'B 150\n']  # file.readlines()
        team1, team2 = wholeList[0].rstrip("\n"), wholeList[1].rstrip("\n")
        points = wholeList[2:]
        print(points)
        for i in range(len(points)):
            points[i] = points[i].rstrip("\n")
            points[i] = points[i].split(" ")
        j = 0
        team1S = 0
        team2S = 0
        while True:
            if points[j][0] == team1:
                team1S += int(points[j][1])
                if team1S >= 150:
                    return team1
            elif points[j][0] == team2:
                team2S += int(points[j][1])
                if team2S >= 150:
                    return team2
