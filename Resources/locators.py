from selenium.webdriver.common.by import By


class LoginPageLocators:

    """
    WebElement Locators
    """
    username_field = (By.NAME, 'username')
    password_field = (By.NAME, 'password')
    connect_btn = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div')
    cookies_reject_btn = (By.XPATH, "//*[text()='Refuser les cookies optionnels']")
    password_error_msg1 = (By.CLASS_NAME, "_ab2z")
    password_error_msg2 = (By.XPATH, "//*[text()='Désolé, votre mot de passe est  incorrect. Veuillez vérifier votre mot de passe.']")
