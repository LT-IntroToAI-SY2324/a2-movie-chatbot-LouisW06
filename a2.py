from typing import List


def match(pattern: List[str], source: List[str]) -> List[str]:
    """Attempts to match the pattern to the source.

    % matches a sequence of zero or more words and _ matches any single word

    Args:
        pattern - a pattern using to % and/or _ to extract words from the source
        source - a phrase represented as a list of words (strings)

    Returns:
        None if the pattern and source do not "match" ELSE A list of matched words
        (words in the source corresponding to _'s or %'s, in the pattern, if any)
    """

    sind = 0  # current index we are looking at in source list
    pind = 0  # current index we are looking at in pattern list
    result: List[str] = []  # to store substitutions we will return if matched

    # keep checking as long as we haven't hit the end of either pattern or source while
    # pind is still a valid index OR sind is still a valid index (valid index means that
    # the index is != to the length of the list)

    # for j in range(len(pattern)): 
    #         print(f"{pattern[j]}") 
    #         print(f"j is {j}")
    print("Starting")
    if len(pattern) > len(source):
        return None
    for pind in range(len(pattern)):
        pword = pattern[pind]
        sword = source[sind]
        if pword == "%":
            if pind >= len(pattern) - 1:
                while sind < len(source) - 1:
                    result += sword
                    sind += 1
                    sword = source[sind]
            else:
                pword2 = pattern[pind + 1]
                while pword2 != sword:
                    result += sword
                    sind += 1
                    sword = source[sind]
                #print(f"pword2 = {pword2}, sword = {sword}, pword={pword}, sind={sind}")
        elif pword == "_":
            sind += 1
            result += sword
        else:
            if pword == sword:
                sind += 1
                print(pword)
            else:
                return None
        print(sind)
        # if len(pattern) > len(source):
        #     return None
        # elif len(pattern) < len(source):
        #     return None
    if sind < len(source):
        return None

        # 1) if we reached the end of the pattern but not source

        # 2) if the current thing in the pattern is a %
        # WARNING: this condition contains the bulk of the code for the assignment
        # If you get stuck on this one, we encourage you to attempt the other conditions
        #   and come back to this one afterwards

        # 3) if we reached the end of the source but not the pattern

        # 4) if the current thing in the pattern is an _

        # 5) if the current thing in the pattern is the same as the current thing in the
        # source

        # 6) else : this will happen if none of the other conditions are met it
        # indicates the current thing it pattern doesn't match the current thing in
        # source
    print(f"result is {result}")
    return result


if __name__ == "__main__":
    assert match(["x", "y", "z"], ["x", "y", "z"]) == [], "test 1 failed"
    assert match(["x", "z", "z"], ["x", "y", "z"]) == None, "test 2 failed"
    assert match(["x", "y"], ["x", "y", "z"]) == None, "test 3 failed"
    assert match(["x", "y", "z", "z"], ["x", "y", "z"]) == None, "test 4 failed"
    assert match(["x", "_", "z"], ["x", "y", "z"]) == ["y"], "test 5 failed"
    assert match(["x", "_", "_"], ["x", "y", "z"]) == ["y", "z"], "test 6 failed"
    assert match(["x", "%", "z"], ["x", "y", "z"]) == ["y"], "bob and louis test failed"
    assert match(["%"], ["x", "y", "z"]) == ["x y z"], "test 7 failed"
    assert match(["x", "%", "z"], ["x", "y", "z"]) == ["y"], "test 8 failed"
    assert match(["%", "z"], ["x", "y", "z"]) == ["x y"], "test 9 failed"
    assert match(["x", "%", "y"], ["x", "y", "z"]) == None, "test 10 failed"
    assert match(["x", "%", "y", "z"], ["x", "y", "z"]) == [""], "test 11 failed"
    assert match(["x", "y", "z", "%"], ["x", "y", "z"]) == [""], "test 12 failed"
    assert match(["_", "%"], ["x", "y", "z"]) == ["x", "y z"], "test 13 failed"
    assert match(["_", "_", "_", "%"], ["x", "y", "z"]) == [
        "x",
        "y",
        "z",
        "",
    ], "test 14 failed"
    # this last case is a strange one, but it exposes an issue with the way we've
    # written our match function
    assert match(["x", "%", "z"], ["x", "y", "z", "z", "z"]) == None, "test 15 failed"

    print("All tests passed!")
