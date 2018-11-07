import time
import unittest
from selenium import webdriver

class pruebaUnitaria(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        url = "https://samir04m.github.io/"
        self.driver.get(url)
        time.sleep(2)

    def test_prueba1(self):
        self.driver.find_element_by_id("zx1").send_keys("-8")
        self.driver.find_element_by_id("zx2").send_keys("-10")
        self.driver.find_element_by_id("f1x1").send_keys("2")
        self.driver.find_element_by_id("f1x2").send_keys("3")
        self.driver.find_element_by_id("s1").send_keys("1")
        self.driver.find_element_by_id("f1r").send_keys("600")
        self.driver.find_element_by_id("f2x1").send_keys("2")
        self.driver.find_element_by_id("f2x2").send_keys("1")
        self.driver.find_element_by_id("s2").send_keys("1")
        self.driver.find_element_by_id("f2r").send_keys("500")
        self.driver.find_element_by_id("f3x1").send_keys("0")
        self.driver.find_element_by_id("f3x2").send_keys("4")
        self.driver.find_element_by_id("s3").send_keys("1")
        self.driver.find_element_by_id("f3r").send_keys("600")
        self.driver.find_element_by_id("btn-run").click()
        time.sleep(3)

        z = self.driver.find_element_by_id("z").text
        self.assertNotEqual(z, "0")
        if (z != "0"):
            print("\nPrueba 1: No se encontraron problemas")
        else :
            print("\nPrueba 1: Se encontro 1 problema")

    def test_prueba2(self):
        self.driver.find_element_by_id("zx1").send_keys("-50")
        self.driver.find_element_by_id("zx2").send_keys("-80")
        self.driver.find_element_by_id("f1x1").send_keys("1")
        self.driver.find_element_by_id("f1x2").send_keys("2")
        self.driver.find_element_by_id("s1").send_keys("1")
        self.driver.find_element_by_id("f1r").send_keys("120")
        self.driver.find_element_by_id("f2x1").send_keys("1")
        self.driver.find_element_by_id("f2x2").send_keys("1")
        self.driver.find_element_by_id("s2").send_keys("1")
        self.driver.find_element_by_id("f2r").send_keys("90")
        self.driver.find_element_by_id("f3x1").send_keys("0")
        self.driver.find_element_by_id("f3x2").send_keys("0")
        self.driver.find_element_by_id("s3").send_keys("1")
        self.driver.find_element_by_id("f3r").send_keys("0")
        self.driver.find_element_by_id("btn-run").click()
        time.sleep(3)

        z = self.driver.find_element_by_id("z").text
        # self.assertNotEqual(z, "0")
        if (z != "0"):
            print("\nPrueba 2: No se encontraron problemas")
        else :
            print("\nPrueba 2: Se encontro 1 problema")

    def test_prueba3(self):
        self.driver.find_element_by_id("zx1").send_keys("8")
        self.driver.find_element_by_id("zx2").send_keys("10")
        self.driver.find_element_by_id("f1x1").send_keys("2")
        self.driver.find_element_by_id("f1x2").send_keys("3")
        self.driver.find_element_by_id("s1").send_keys("1")
        self.driver.find_element_by_id("f1r").send_keys("600")
        self.driver.find_element_by_id("f2x1").send_keys("2")
        self.driver.find_element_by_id("f2x2").send_keys("1")
        self.driver.find_element_by_id("s2").send_keys("1")
        self.driver.find_element_by_id("f2r").send_keys("500")
        self.driver.find_element_by_id("f3x1").send_keys("0")
        self.driver.find_element_by_id("f3x2").send_keys("4")
        self.driver.find_element_by_id("s3").send_keys("1")
        self.driver.find_element_by_id("f3r").send_keys("600")
        self.driver.find_element_by_id("btn-run").click()
        time.sleep(3)

        z = self.driver.find_element_by_id("z").text
        # self.assertNotEqual(z, "0")
        if (z != "0"):
            print("\nPrueba 3: No se encontraron problemas")
        else :
            print("\nPrueba 3: Se encontro 1 problema")

    def tearDown(self):
        self.driver.quit()

unittest.main()
