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
    else:

        print(f"Scores processed: {len(args) - 1}")
        print(f"Total score : {sum(lst)}")
        print(f"Average score : {sum(lst) / (len(args) - 1)}")
        print(lst)
        print(f"High score: {max(lst)}")
        print(f"Low score: {min(lst)}")
        print(f"Score range: {max(lst) - min(lst)}")


ft_score_analytics()