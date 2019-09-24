# def ab(a):
#     print("a")


# c = "a" + "b"
# print(c)
# print(3, 0)

"""--------------------------------"""
# def count(n):
# ...     def say(s0, s1):
# ...         print(n)
# ...         return count(n + 1)
# ...     return say

# def test(a):
#     def test2(b,c):
#         print()
#     print(a)
#     return test


# def test(a):
#     print(a)

#     def test2():
#         return a = 5

#     return test2

#     print(a)


# c = test(2)
# c()


# n = 1
# a = 1
# while n < 3:

#     test(a)
#     a += 1
#     n += 1

# print("*", 0)


def announce_highest(who, previous_high=0, previous_score=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 11)
    11 point(s)! That's the biggest gain yet for Player 1
    >>> f3 = f2(20, 11)
    >>> f4 = f3(13, 20)
    >>> f5 = f4(20, 35)
    15 point(s)! That's the biggest gain yet for Player 1
    >>> f6 = f5(20, 47) # Player 1 gets 12 points; not enough for a new high
    >>> f7 = f6(21, 47)
    >>> f8 = f7(21, 77)
    30 point(s)! That's the biggest gain yet for Player 1
    >>> f9 = f8(77, 22) # Swap!
    >>> f10 = f9(33, 77) # Swap!
    55 point(s)! That's the biggest gain yet for Player 1
    """
    assert who == 0 or who == 1, "The who argument should indicate a player."
    # BEGIN PROBLEM 7
    def announce(score0, score1):
        last_score = previous_score
        last_high = previous_high
        print("s0=", score0, "s1=", score1, "ls=", last_score, "lh=", last_high)

        if who == 0:
            change = score0 - last_score
            if change > last_high:
                print(change, "point(s)! That's the biggest gain yet for Player", who)
                last_high = change
            last_score = score0
        elif who == 1:
            change = score1 - last_score
            if change > last_high:
                print(change, "point(s)! That's the biggest gain yet for Player", who)
                last_high = change
            last_score = score1
        print("s0=", score0, "s1=", score1, "ls=", last_score, "lh=", last_high)
        return announce_highest(who, last_high, last_score)

    return announce


f0 = announce_highest(1)
print("f1 = f0(12, 0)")
f1 = f0(12, 0)
print("f2 = f0(12, 10)")
f2 = f0(12, 10)
print("f3 = f2(20, 10)")
f3 = f2(20, 10)
print("f4 = f3(22, 20)")
f4 = f3(22, 20)
print("f5 = f4(22, 35)")
f5 = f4(22, 35)
