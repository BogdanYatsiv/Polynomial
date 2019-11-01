import unittest
import Poly_tests

# calcTestSuite = unittest.TestSuite()
# calcTestSuite.addTest(unittest.makeSuite(Poly_tests.Poly_tests))

testCases = []
testCases.append(Poly_tests.Poly_tests)

testLoad = unittest.TestLoader()

suites = []
suites.append(testLoad.loadTestsFromTestCase(testCases[0]))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)