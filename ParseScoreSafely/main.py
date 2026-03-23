def parse_scores(raw_scores):
    valid_scores = []
    
    for num in raw_scores:  
        try:
            number = int(num)
        except ValueError:
            continue
        except TypeError:
            continue
            
        if(number >= 0):
            valid_scores.append(number) 
        
    if(len(valid_scores) == 0):
        raise ValueError("no valid scores")

    return valid_scores

print(parse_scores(["10", "20", "30"]))
# [10, 20, 30]

print(parse_scores(["10", "oops", "25", "-5", None]))
# "oops" and None are ignored (cannot be converted)
# -5 is ignored (negative)
# [10, 25]

print(parse_scores(["abc", None, "-3"]))
# raises ValueError("no valid scores")
