import sys

arg_num = len(sys.argv)
print("=== Player Score Analytics ===")
score_list = list()
i = 1
if arg_num == 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
else:
    while i < arg_num:
        try:
            score_list.append(int(sys.argv[i]))
        except ValueError:
            print(f"Argument {i} is not a number: \"{sys.argv[i]}\""
                  f" and will not be added to the score list.")
        i += 1
    if len(score_list):
        print(f"Scores processed: {score_list[0:]}")
        print(f"Total players: {len(score_list)}")
        print(f"Total score: {sum(score_list)}")
        print(f"Average score: {(sum(score_list) / len(score_list))}")
        print(f"High score: {max(score_list)}")
        print(f"Low score: {min(score_list)}")
        print(f"Score range: {(max(score_list) - min(score_list))}")