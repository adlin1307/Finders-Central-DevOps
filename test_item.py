import unittest
from item import validate_item


class TestItem(unittest.TestCase):

    def test_lost_item(self):
        self.assertEqual(
            validate_item("Wallet", "Accessories", "Library",
                          "Black wallet", "Lost"),
            "Valid Report"
        )

    def test_found_item(self):
        self.assertEqual(
            validate_item("ID Card", "Documents", "Classroom",
                          "College ID", "Found"),
            "Valid Report"
        )

    def test_empty_name(self):
        self.assertEqual(
            validate_item("", "Books", "Library",
                          "Notebook", "Lost"),
            "Invalid Report"
        )

    def test_empty_category(self):
        self.assertEqual(
            validate_item("Wallet", "", "Library",
                          "Black wallet", "Lost"),
            "Invalid Report"
        )

    def test_invalid_report_type(self):
        self.assertEqual(
            validate_item("Watch", "Accessories", "Canteen",
                          "Silver watch", "Missing"),
            "Invalid Report"
        )


if __name__ == "__main__":
    unittest.main()