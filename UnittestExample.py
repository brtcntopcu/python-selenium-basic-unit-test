import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class BasicFormTest(unittest.TestCase):
    
    url = "https://www.seleniumeasy.com/test/ajax-form-submit-demo.html"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def fillForm(self):
        nameInput = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div[1]/input")
        commentInput = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div[2]/textarea")
        
        nameInput.send_keys("Name Input Content")
        commentInput.send_keys("Comment Input Content")

        submitButton = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div[3]/input")
        submitButton.click()
    
    def test_form_name_input_name_check(self):
        actualNameInputName = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div[1]/label")
        expectedNameInputName = "Name"
        self.assertEqual(actualNameInputName.text[:-1],expectedNameInputName,"Actual name input is not not equal to expected name")

    def test_form_comment_input_name_check(self):
        actualCommentInputName = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div[2]/label")
        expectedCommentInputName = "Comment"
        self.assertEqual(actualCommentInputName.text[:-1],expectedCommentInputName,"Actual comment input is not not equal to expected name")
    
    def test_form_title_name_check(self):
        actualFormTitle = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]")
        expectedFormTitle = "Ajax Form"
        self.assertEqual(actualFormTitle.text,expectedFormTitle,"Actual title is not not equal to expected title")

    def test_form_submit_process_message_check(self):
        self.fillForm()
        expectedProcessMessage = "Ajax Request is Processing!"
        actualProcessMessage = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div[3]"))
        )
        self.assertEqual(actualProcessMessage.text,expectedProcessMessage,"Actual process message is not equal to expected message")
    
    def test_form_submit_succes_message_check(self):
        self.fillForm()
        expectedSuccessMessage = "Form submited Successfully!"
        time.sleep(4)
        actualSuccesMessage = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div[3]")
        self.assertEqual(actualSuccesMessage.text,expectedSuccessMessage,"Actual success message is not equal to expected message")
        
    def tearDown(self):
        self.driver.close()
        



if __name__ == "__main__":
    unittest.main()
