import pytest
from pages.signup_page import SignupPage

@pytest.mark.parametrize("email, password, otp", [
    ("anjanajju027@gmail.com", "Govindha1@", "264200")
])
def test_signup_flow(driver, email, password, otp):
    signup = SignupPage(driver)
    signup.open_homepage()
    signup.click_login_signup()
    signup.click_register_link()
    signup.select_teacher_role()
    signup.enter_email_and_password(email, password)
    signup.submit_registration()
    signup.confirm_registration_modal()
    signup.enter_otp(otp)
    signup.confirm_otp()
    print("Signup flow completed successfully.")


# use command to run pytest tests/test_signup.py -v