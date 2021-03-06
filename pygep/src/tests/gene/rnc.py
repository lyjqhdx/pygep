from pygep.functions.mathematical.arithmetic import subtract_op
from pygep.gene import KarvaGene
import unittest


class KarvaTest(unittest.TestCase):
    '''Tests basic functionality of Karva genes'''
    def testDerivation(self):
        alleles = [subtract_op, '?', '?', 1, 0]
        gene = KarvaGene(alleles, 1, [2, 5])
        self.assertEqual(gene._evaluation, [subtract_op, 5, 2])
        self.assertEqual(gene.alleles, alleles)
        
        # Make sure the RNCs are evaluated correctly
        o = object()
        self.assertEqual(3, gene(o))
        
        # Make sure all caching is done
        self.assertTrue(o in getattr(gene, '___call___memo'))
        self.assertEqual(gene._evaluation, [3, 5, 2])

        # And that changes to the used RNCs eliminate that cache
        gene2 = gene.derive([(4, [1])])
        self.assertNotEqual(gene2._evaluation, gene._evaluation)
        self.assertRaises(AttributeError, getattr, gene2, '___call___memo')
        
        
    def testDCDerivation(self):
        '''TODO: test changes to DC'''
        
    
    def testDCVariation(self):
        '''TODO: RNC mutation/xover/etc'''
        

if __name__ == '__main__':
    unittest.main()
