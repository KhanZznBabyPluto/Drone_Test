from scipy.stats import norm

def integrating(district):
    loc = 0
    for i in district.neighbours:
        loc += i.rating
    loc /= len(district.neighbours)

    sum_sqr_deviation = 0
    for i in district.neighbours:
        sum_sqr_deviation += (i.rating - loc) ** 2

    scale = (sum_sqr_deviation / len(district.neighbours)) ** 0.5

    if scale == 0:
        return district.rating

    max_prob = 0
    x = -100
    for i in range(-14, 15):
        prob = norm.cdf(i, loc, scale)
        if max_prob <= prob:
            max_prob = prob
            x = i

    if max_prob > 0.3:
        new_rating = district.rating + x
    else:
        new_rating = district.rating


    if new_rating < 0:
        new_rating = 0
    elif new_rating > 100:
        new_rating = 100

    district.rating = new_rating