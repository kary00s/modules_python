import sys


def ft_score_analytics():
    args = sys.argv
    i = 1
    lst = []
    try:
        while i < len(args):
            arg = int(args[i])
            lst.append(arg)
            i += 1

    except ValueError:
        print("OOPS , you put an invalid argument")

    print("=== Player Score Analytics ===")
    if len(lst) > 0:
        print(f"Scores processed: {len(args) - 1}")
        print(f"Total score : {sum(lst)}")
        print(f"Average score : {sum(lst) / (len(args) - 1)}")
        print(f"High score: {max(lst)}")
        print(f"Low score: {min(lst)}")
        print(f"Score range: {max(lst) - min(lst)}\n")
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " :wq!<score1> <score2> ...")


if __name__ == "__main__":
    ft_score_analytics()