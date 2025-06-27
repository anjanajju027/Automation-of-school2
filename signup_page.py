from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open_homepage(self):
        self.driver.get("https://proschool.ai/")

    def click_login_signup(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Login / Sign Up')]").click()

    def click_register_link(self):
        self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div/div/form/div/div[6]/span/a").click()

    def select_teacher_role(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Teacher')]").click()

    def enter_email_and_password(self, email, password):
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)

    def submit_registration(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def confirm_registration_modal(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='dialog']")))
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Confirm')]").click()

    def enter_otp(self, otp):
        otp_inputs = self.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'input[autocomplete=\"one-time-code\"]')
        ))
        assert len(otp_inputs) >= 6
        for i, digit in enumerate(otp):
            otp_inputs[i].send_keys(digit)

    def confirm_otp(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Confirm code')]").click()
