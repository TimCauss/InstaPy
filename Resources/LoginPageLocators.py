from selenium.webdriver.common.by import By


class InstaLocators(object):
    # Locators For Login Page :
    username_field = (By.NAME, 'username')
    password_field = (By.NAME, 'password')
    connect_btn = (By.XPATH,
                   '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div')

    # Login error message
    login_error_class = (By.CLASS_NAME, "_ab2z")
    login_error_text = (
        By.XPATH, "//*[text()='Désolé, votre mot de passe est  incorrect. Veuillez vérifier votre mot de passe.']")

    # Cookies Toasts Locators :
    cookies_accept_btn = (By.XPATH, "//*[text()='Autoriser tous les cookies']")
    cookies_reject_btn = (By.XPATH, "//*[text()='Refuser les cookies optionnels']")
