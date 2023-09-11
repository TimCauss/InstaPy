class InstaLocators(object):
    # Locators For Login Page :
    username_field = 'username'
    password_field = 'password'
    connect_btn = ("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div["
                   "2]/form/div/div[3]/button/div")

    # Login error message
    login_error_class = "_ab2z"
    login_error_text = "//*[text()='Désolé, votre mot de passe est  incorrect. Veuillez vérifier votre mot de passe.']"

    # Cookies Toasts Locators :
    cookies_accept_btn = "//*[text()='Autoriser tous les cookies']"
    cookies_reject_btn = "//*[text()='Refuser les cookies optionnels']"
