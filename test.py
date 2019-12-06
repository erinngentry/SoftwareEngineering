'''
created on Sep 2, 2019



@author: erinn

'''

import unittest 

from program import f, left_inches_margin, right_inches_margin





class Tests(unittest.TestCase):



    def setUp(self):

        pass



    def testReadableFile(self):

        if f.readable() == False:

            self.assertFalse(False, "Cannot read file.")

            

    def testReasonableLeftMargin(self):

        if left_inches_margin > 12:

            self.assertNotLess(left_inches_margin, 12, "Margin exceeds page size.")

            

    def testReasonableRightMargin(self):

        if right_inches_margin > 12:

            self.assertNotLess(right_inches_margin, 12, "Margin exceeds page size.")



if __name__ == "__main__":

    unittest.main()
