"""class for testing the register_order method"""
import unittest
from datetime import datetime
import hashlib

from unittest.mock import patch
from uc3m_consulting import EnterpriseManager
from uc3m_consulting import EnterpriseManagementException


class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""

    def test_tc1(self):
        """"""
        manager = EnterpriseManager()
        obj = manager.register_project("B12345678","PRO01", "car automatic development",
        "HR", "31/12/2027", 50000.00)
        self.assertIsInstance(obj, str, "return should be string")
        self.assertEqual(len(obj), 32, "should be length of 32")
        self.assertTrue(obj.isalnum(), "should not have special characters")

    def test_tc2(self):
        manager = EnterpriseManager()
        obj = manager.register_project("B12345678","890478", "valid texts",
        "Finance", str(datetime.today().strftime("%d/%m/%Y")), 50000.01)
        self.assertIsInstance(obj, str, "return should be string")
        self.assertEqual(len(obj), 32, "should be length of 32")
        self.assertTrue(obj.isalnum(), "should not have special characters")

    def test_tc3(self):
        manager = EnterpriseManager()
        obj = manager.register_project("B12345678","PR0000002", "valid textvalid textvalid tex",
        "Legal", "31/12/2027", 999999.99)
        self.assertIsInstance(obj, str, "return should be string")
        self.assertEqual(len(obj), 32, "should be length of 32")
        self.assertTrue(obj.isalnum(), "should not have special characters")

    def test_tc4(self):
        manager = EnterpriseManager()
        obj = manager.register_project("B12345678","PRCF538FG0", "valid text",
        "Logistics", "31/12/2026", 1000000.00)
        self.assertIsInstance(obj, str, "return should be string")
        self.assertEqual(len(obj), 32, "should be length of 32")
        self.assertTrue(obj.isalnum(), "should not have special characters")

    # INVALID TEST CASES
    # ECNV5
    def test_tc5(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException, manager.register_project, 12345678, "PR001",
                          "car automatic development", "HR", "1/1/2027", 50000.00)

    # ECNV3, BLNV1
    def test_tc6(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException, manager.register_project,"B1234567", "PR0000002",
                          "valid texts", "Legal", "31/12/2026", 75000.00)

    # ECNV4, BLNV2
    def test_tc7(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException, manager.register_project,"B123456789", "PR001", "valid texts",
                                           "Legal", "31/12/2026", 75000.00)

    # ECNV5
    def test_tc8(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException,manager.register_project,"712345678", "PR001",
                          "valid texts", "Legal", "31/12/2026", 50000.00)

    #ECNV6
    def test_tc9(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException,manager.register_project,"B12345678",
                          123456, "valid texts", "HR", "31/12/2026", 50000.00)

    # ECNV7, BLNV3
    def test_tc10(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException,manager.register_project,"B12345678", "PR07", "car automatic development",
                                       "HR", "31/12/2026", 50000.00)

    # ECNV8, BLNV4
    def test_tc11(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException, manager.register_project,"B12345678", "PRCF538FG07", "car automatic development",
                                       "HR", "31/12/2026", 50000.00)

    #ECNV9
    def test_tc12(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException, manager.register_project,"B12345678",
                          "PR_F538FG0", "car automatic development",
                                       "Logistics", "1/1/2027", 50000.00)

    #ECNV10
    def test_tc13(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException, manager.register_project,"B12345678",
                          "PR001", 12345678976, "Logistics", "1/1/2027", 50000.00)

    #ECNV11, BLNV5
    def test_tc14(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException, manager.register_project,"B12345678",
                          "PR001", "not valid", "HR", "31/12/2026", 50000.00)

    #ECNV12, BLNV6
    def test_tc15(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException, manager.register_project,"B12345678",
                          "PR001", "Real-time neural signal systems", "HR", "31/12/2026", 50000.00)

    #ECNV13
    def test_tc16(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException, manager.register_project,"B12345678",
                          "PR001", "valid texts", 13579 , "31/12/2026", 50000.00)

    #ECNV14
    def test_tc17(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException, manager.register_project,"B12345678",
                          "PR001", "valid texts", "Communications" , "1/1/2027", 50000.00)

    # ECNV15
    def test_tc18(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException, manager.register_project, "B12345678",
                          "PR001", "valid texts", "HR", 12122025, 50000.00)

    # ECNV16
    def test_tc19(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException, manager.register_project, "B12345678",
                          "PR001", "valid texts", "Logistics", "10/14/2025", 50000.00)

    # ECNV17 - BLNV7
    def test_tc20(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException, manager.register_project, "B12345678",
                          "PR001", "valid texts", "HR", "1/1/2024", 50000.00)

    # ECNV18 - BLNV8
    def test_tc21(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException, manager.register_project, "B12345678",
                          "PR001", "valid texts", "Finance", "12/12/2028", 50000.00)

    # ECNV19
    def test_tc22(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException, manager.register_project, "B12345678",
                          "PR001", "valid texts", "Legal", "12/12/2026", "50000.50")

    # ECNV20-BLNV19
    def test_tc23(self):
        manager = EnterpriseManager()
        self.assertRaises(EnterpriseManagementException, manager.register_project, "B12345678",
                          "PR001", "valid texts", "Logistics", "31/12/2026", 45000.00)

    # ECNV22
    @patch("uc3m_consulting.enterprise_project.hashlib.md5")
    def test_tc24(self, mock_md5):
        mock_md5.side_effect = Exception("MD5 failure")

        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_project("B12345678", "PRO01", "car automatic development",
                                     "HR", "31/12/2027", 50000.00)

    # ECNV23
    @patch("builtins.open")
    def test_tc25(self, mock_open):
        mock_open.side_effect = OSError("JSON Write Error")

        manager = EnterpriseManager()

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_project("B12345678", "PRO01", "car automatic development",
                                       "HR", "31/12/2027", 50000.00)

if __name__ == '__main__':
    unittest.main()
