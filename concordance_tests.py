import unittest
import filecmp
from concordance import *


class TestList(unittest.TestCase):

    # def test_01(self):
    #     conc = Concordance()
    #     conc.load_stop_table("stop_words.txt")
    #     conc.load_concordance_table("file1.txt")
    #     conc.write_concordance("file1_con.txt")
    #     self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))

    # def test_02(self):
    #     conc = Concordance()
    #     conc.load_stop_table("stop_words.txt")
    #     conc.load_concordance_table("file2.txt")
    #     conc.write_concordance("file2_con.txt")
    #     self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))

    def test_03(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        self.assertTrue(
          filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("War_And_Peace.txt")
        conc.write_concordance("war_con.txt")

    # def test_edges(self):
    #     test_heap = Concordance()
    #     with self.assertRaises(FileNotFoundError):
    #         test_heap.load_concordance_table("blahJV.txt")
    #     with self.assertRaises(FileNotFoundError):
    #         test_heap.load_stop_table("blahJV.txt")
    #     test_heap.load_concordance_table("test_JV.txt")
    #     self.assertEqual(test_heap.concordance_table.num_items, 8)


if __name__ == '__main__':
    unittest.main()
