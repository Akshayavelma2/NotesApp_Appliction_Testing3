from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class HomePage(BasePage):

    add_note_btn = (By.XPATH, "//button[@data-testid='add-new-note']")
    title_input = (By.XPATH, "//input[@data-testid='note-title']")
    description_input = (By.XPATH, "//textarea[@data-testid='note-description']")
    category_dropdown = (By.XPATH, "//select[@data-testid='note-category']")
    save_btn = (By.XPATH, "//button[@data-testid='note-submit']")

    def create_note(self, title, description):
        self.click(self.add_note_btn)

        self.type(self.title_input, title)
        self.type(self.description_input, description)

        category = self.find(self.category_dropdown)
        category.send_keys("Home")

        time.sleep(1)

        self.click(self.save_btn)

    def is_note_visible(self, title):
        return title in self.driver.page_source
    
    def is_note_not_visible(self, title):
        return title not in self.driver.page_source