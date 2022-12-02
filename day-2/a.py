def main(input_file):
    """Prints the answer to the first part of the second day's puzzle.

    Args:
        input_file (str): The path to the input file.

    Returns:
        None
    """
    # read input
    with open(input_file, "r") as f:
        lines = f.readlines()

    # parse input
    rounds = []
    for line in lines:
        rounds.append(line.strip().split())

    # selection score
    score_values = {"rock": 1, "paper": 2, "scissors": 3}  # A, B, C
    # win/loss/draw score
    win_loss_draw = {"win": 6, "loss": 0, "draw": 3}  # Y, X, Z

    score = 0
    # calculate score
    for round in rounds:
        # Your opponend round[0] has chosen rock (A)
        if round[0] == "A":
            # You should choose paper (Y)
            if round[1] == "Y":
                score += score_values["paper"] + win_loss_draw["win"]
            # You should choose rock (X)
            if round[1] == "X":
                score += score_values["rock"] + win_loss_draw["draw"]
            # You should choose scissors (Z)
            if round[1] == "Z":
                score += score_values["scissors"] + win_loss_draw["loss"]

        # Your opponend round[0] has chosen paper (B)
        if round[0] == "B":
            # You should choose paper (Y)
            if round[1] == "Y":
                score += score_values["paper"] + win_loss_draw["draw"]
            # You should choose rock (X)
            if round[1] == "X":
                score += score_values["rock"] + win_loss_draw["loss"]
            # You should choose scissors (Z)
            if round[1] == "Z":
                score += score_values["scissors"] + win_loss_draw["win"]

        # Your opponend round[0] has chosen scissors (C)
        if round[0] == "C":
            # You should choose paper (Y)
            if round[1] == "Y":
                score += score_values["paper"] + win_loss_draw["loss"]
            # You should choose rock (X)
            if round[1] == "X":
                score += score_values["rock"] + win_loss_draw["win"]
            # You should choose scissors (Z)
            if round[1] == "Z":
                score += score_values["scissors"] + win_loss_draw["draw"]

    print(score)


if __name__ == "__main__":
    main("day-2/input.txt")
