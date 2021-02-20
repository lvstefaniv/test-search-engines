from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

# Arrange
browser.config.hold_browser_open = True
browser.open('https://www.ecosia.org/')

# Act
s('[data-test-id=search-form-input]').type('yashaka selene').press_enter()
browser.all('.result-snippet').first.click()

# Assert
ss('[href="/yashaka/selene"]').should(have.size(3))

browser.close()
