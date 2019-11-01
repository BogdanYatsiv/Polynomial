import unittest
import Polynomial

class Poly_tests(unittest.TestCase):
    def test_init(self):
        values = [(1, 2), (13, 3), (-20, 5), (5, 7), (-10, 10)]

        self.assertEqual(self.a.values,values)

    def test_init_2(self):
        new_poly = Polynomial.Polinom()

        self.assertEqual(type(self.a),type(new_poly))

    def test_getter(self):
        item = (5,7)

        self.assertEqual(self.a[7],item)

    def test_setter(self):
        item = (15,7)
        self.a[7] = 15

        self.assertEqual(self.a[7],item)

    def test_setter_2(self):
        values = [(1, 2), (13, 3), (-20, 5), (-10, 10)]
        self.a[7] = 0

        self.assertEqual(self.a.values,values)

    #TODO: setter and getter with exception

    def test_str(self):
        line = "P_5(x) =  1*x^2 + 13*x^3  -20*x^5 + 5*x^7  -10*x^10"
        poly_line = self.a.__str__()

        self.assertEqual(poly_line,line)

    def test_str_2(self):
        line = "Polinom is empty"
        poly_line = Polynomial.Polinom().__str__()

        self.assertEqual(poly_line,line)

    def setUp(self):
        print(f"Set up for [{self.id()}]")
        values_a = [(1, 2), (13, 3), (-20, 5), (5, 7), (-10, 10)]
        self.a = Polynomial.Polinom(values_a,len(values_a))

        values_b = [(13,1), (1,2), (23,5)]
        self.b = Polynomial.Polinom(values_b,len(values_b))

    def tearDown(self):
        print(f"Tear down for [{self.id()}]")
        del self.a
        del self.b

if __name__ == "__main__":
    unittest.main()