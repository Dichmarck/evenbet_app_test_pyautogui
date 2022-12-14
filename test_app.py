import time
import pytest
from evenbet_app_test.constants import *
import pyautogui
from evenbet_app_test.pages.BasePage import BasePage
from evenbet_app_test.pages.LoginPage import LoginPage

#pytest -s -v

pyautogui.PAUSE = 0.5


#@pytest.mark.skip
def test_registration(app):
    login_page = LoginPage(pyautogui.size())
    login_page.click_main_page_login_button()
    login_page.should_appear_login_window()
    login_page.click_sign_up_button()
    login_page.should_appear_sign_up_window()
    time_secs_int = int(time.time())  # some unique data for registration
    login_page.find_nick_field_click_it_and_type_nick(f"a{time_secs_int}test")
    login_page.find_email_field_click_it_and_type_email(f"a{time_secs_int}@test.com")
    login_page.find_password1_field_click_it_and_type_password(f"a{time_secs_int}test")
    login_page.find_password2_field_click_it_and_type_password(f"a{time_secs_int}test")
    login_page.click_send_button()
    avatar = login_page.should_appear_user_test_avatar()
    pyautogui.moveTo(avatar[0], avatar[1], duration=FAST)

#@pytest.mark.skip
def test_login(app):
    login_page = LoginPage(pyautogui.size())
    login_page.click_main_page_login_button()
    login_page.should_appear_login_window()
    login_page.find_user_name_field_click_it_and_type_user_name(LOGIN)
    login_page.find_password_login_field_click_it_and_type_password(PASSWORD)
    login_page.click_login_button()
    avatar = login_page.should_appear_user_test_avatar()
    pyautogui.moveTo(avatar[0], avatar[1], duration=FAST)


