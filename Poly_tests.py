import unittest
import Polynomial

class Poly_tests(unittest.TestCase):
    def test_init(self):
        values = [(1, 2), (13, 3), (-20, 5), (5, 7), (-10, 10)]

        self.assertEqual(self.a.values,values)

    def test_init_2(self):
        new_poly = Polynomial.Polinom()

        self.assertEqual(type(self.a),type(new_poly))

    def test_init_3(self):
        with self.assertRaises(Exception) as context:
            p = Polynomial.Polinom([(1,1),(2,2)],1)

        self.assertTrue("To short polinom length" in str(context.exception))

    def test_getter(self):
        item = (5,7)

        self.assertEqual(self.a[7],item)

    def test_getter_2(self):
        with self.assertRaises(Exception) as context:
            self.a[1]

        self.assertTrue("There is no such index" in str(context.exception))

    def test_getter_3(self):
        with self.assertRaises(Exception) as context:
            self.a[-1]

        self.assertTrue("Bad index" in str(context.exception))

    def test_setter(self):
        item = (15,7)
        self.a[7] = 15

        self.assertEqual(self.a[7],item)

    def test_setter_2(self):
        values = [(1, 2), (13, 3), (-20, 5), (-10, 10)]
        self.a[7] = 0

        self.assertEqual(self.a.values,values)

    def test_setter_3(self):
        with self.assertRaises(Exception) as context:
            self.a[-1] = 1

        self.assertTrue("Bad index" in str(context.exception))

    def test_setter_4(self):
        with self.assertRaises(Exception) as context:
            self.a[1] = 0

        self.assertTrue("Empty value" in str(context.exception))

    def test_str(self):
        line = "P_10(x) =  1*x^2 + 13*x^3  -20*x^5 + 5*x^7  -10*x^10"
        poly_line = self.a.__str__()

        self.assertEqual(poly_line,line)

    def test_str_2(self):
        line = "Polinom is empty"
        poly_line = Polynomial.Polinom().__str__()

        self.assertEqual(poly_line,line)

    def test_call(self):
        value = self.b(5,2)

        self.assertEqual(value,25)

    def test_call_2(self):
        with self.assertRaises(Exception) as context:
            x = self.a(1,1)

        self.assertTrue("Bad index" in str(context.exception))

    def test_call_3(self):
        with self.assertRaises(Exception) as context:
            x = self.a(1,-1)

        self.assertTrue("Bad index" in str(context.exception))

    def tets_mul(self):
        values = [(26,1), (2,2), (46,5)]
        self.b*2

        self.assertEqual(self.b.values,values)

    def test_mul_2(self):
        values = []
        self.b*0

        self.assertEqual(self.b.values,values)

    def test_add(self):
        values = [(13,1), (2,2), (13,3), (3,5), (5,7), (-10,10)]
        c = self.a + self.b

        self.assertEqual(c.values,values)

    def setUp(self):
        print(f"Set up for [{self.id()}]")

        values_a = [(1, 2), (13, 3), (-20, 5), (5, 7), (-10, 10)]
        self.a = Polynomial.Polinom(values_a,10)

        values_b = [(13,1), (1,2), (23,5)]
        self.b = Polynomial.Polinom(values_b,len(values_b))

    def tearDown(self):
        print(f"Tear down for [{self.id()}]\n")
        del self.a
        del self.b

if __name__ == "__main__":
    unittest.main()