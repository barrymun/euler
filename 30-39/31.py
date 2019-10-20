def number_of_ways_to_form_coin(coin):
    """
    """
    count = 0
    for two_pound in xrange(0, 2):
        if (two_pound * 200) > coin:
            break
        for one_pound in xrange(0, 3):
            if (one_pound * 100) > coin:
                break
            for fifty_p in xrange(0, 5):
                if (fifty_p * 50) > coin:
                    break
                for twenty_p in xrange(0, 11):
                    if (twenty_p * 20) > coin:
                        break
                    for ten_p in xrange(0, 21):
                        if (ten_p * 10) > coin:
                            break
                        for five_p in xrange(0, 41):
                            if (five_p * 5) > coin:
                                break
                            for two_p in xrange(0, 101):
                                if (two_p * 2) > coin:
                                    break
                                for one_p in xrange(0, 201):

                                    value = (two_pound * 200) + \
                                        (one_pound * 100) + \
                                        (fifty_p * 50) + \
                                        (twenty_p * 20) + \
                                        (ten_p * 10) + \
                                        (five_p * 5) + \
                                        (two_p * 2) + \
                                        (one_p * 1)

                                    if value > coin or value < coin:
                                        continue

                                    count += 1

    return count

if __name__ == "__main__":
    print number_of_ways_to_form_coin(coin=200)


# better method, much faster
# TODO: solve using dynamic programming method
#
# def number_of_ways_to_form_coin():
#     """
#     """
#     count = 0
#     for two_pound in xrange(201, 0, -200):  # 201 to handle >=, not just > decrement case
#         for one_pound in xrange(two_pound, 0, -100):
#             for fifty_p in xrange(one_pound, 0, -50):
#                 for twenty_p in xrange(fifty_p, 0, -20):
#                     for ten_p in xrange(twenty_p, 0, -10):
#                         for five_p in xrange(ten_p, 0, -5):
#                             for two_p in xrange(five_p, 0, -2):
#                                 count += 1
#
#     return count
#
# if __name__ == "__main__":
#     print number_of_ways_to_form_coin()
