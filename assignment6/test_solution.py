import unittest
from des import answer


class testDes(unittest.TestCase):
    def testAnswer1(self) -> None:
        ans = answer('Kopavogur')
        self.assertEqual(ans, 'Reykjavik')

    def testAnswer2(self) -> None:
        ans = answer('Seltjarnarnes')
        self.assertEqual(ans, 'Reykjavik')

    def testAnswer3(self) -> None:
        ans = answer('Reykjavik')
        self.assertEqual(ans, 'Reykjavik')

    def testAnswer4(self) -> None:
        ans = answer('Reykjanesbaer')
        self.assertEqual(ans, 'Reykjavik')

    def testAnswer5(self) -> None:
        ans = answer('Akureyri')
        self.assertEqual(ans, 'Akureyri')

    def testAnswer6(self) -> None:
        ans = answer('Mulathing')
        self.assertEqual(ans, 'Akureyri')
