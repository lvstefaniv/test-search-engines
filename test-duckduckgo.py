from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

# Arrange
browser.config.hold_browser_open = True
browser.open('https://duckduckgo.com/')

# Act
s('[id=search_form_input_homepage]').type('yashaka selene').press_enter()
browser.all('.result:not(.result--more)').first.click()

# Assert
ss('[href="/yashaka/selene"]').should(have.size(3))

browser.close()
