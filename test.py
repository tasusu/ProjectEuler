'''
Created on 2012/11/14

@author: Tasuku
'''
import unittest
import itertools
from intlib import is_prime, primes, prime_iter, is_pandigit, is_square, ith_prime
from intlib import Primes

class IntTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_is_pandigit(self):
        counter = 1
        for tpl in itertools.permutations('123456789'):
            if counter > 10 ** 3: break
            n = ''.join(tpl)
            self.assertTrue(is_pandigit(n))
            counter += 1
        self.assertFalse(is_pandigit('112345678'))
    
    def test_is_square(self):
        for i in range(1, 10**3):
            self.assertTrue(is_square(i**2))

class PrimeTest(unittest.TestCase):

    def setUp(self):
        self.primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,
                       67,71,73,79,83,89,97,101,103,107,109,113,127,131,
                       137,139,149,151,157,163,167,173,179,181,191,193,
                       197,199,211,223,227,229,233,239,241,251,257,263,
                       269,271,277,281,283,293,307,311,313,317,331,337,
                       347,349,353,359,367,373,379,383,389,397,401,409,
                       419,421,431,433,439,443,449,457,461,463,467,479,
                       487,491,499,503,509,521,523,541,547,557,563,569,
                       571,577,587,593,599,601,607,613,617,619,631,641,
                       643,647,653,659,661,673,677,683,691,701,709,719,
                       727,733,739,743,751,757,761,769,773,787,797,809,
                       811,821,823,827,829,839,853,857,859,863,877,881,
                       883,887,907,911,919,929,937,941,947,953,967,971,
                       977,983,991,997]
        
        self.klass = Primes(10 ** 6)

    def test_class_is_prime(self):
        for p in self.primes:
            self.assertTrue(self.klass.is_prime(p))
            
    def test_class_ith_prime(self):
        for i, p in enumerate(self.primes):
            self.assertEqual(p, self.klass.ith_prime(i + 1)) 

    def test_is_prime(self):
        for p in self.klass:
            self.assertTrue(is_prime(p))
            
    def test_primes(self):
        ls = primes(10 ** 5)
        for p in ls:
            self.assertTrue(self.klass.is_prime(p))
            
    def test_prime_iter(self):
        for i, p in enumerate(prime_iter()):
            if i > 10**3 : break
            self.assertTrue(self.klass.is_prime(p), msg = '{}'.format(p))
            



if __name__ == "__main__":
    unittest.main()