import unittest


def is_single_riffle(half1, half2, shuffled_deck):
    #complexity-O(n)
    # Check if the shuffled deck is a single riffle of the halves
    len1=len(half1)
    len2=len(half2)
    
    totallen=len1+len2
    if(len(shuffled_deck)!=totallen):
        return False
    
    ptr1=0
    ptr2=0
    for i in shuffled_deck:
        if len(half1)-ptr1>0 and half1[ptr1]==i:
            ptr1+=1
        elif len(half2)-ptr2>0 and half2[ptr2]==i:
            ptr2+=1
        else:
            return False
    return True


# Tests

class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)
