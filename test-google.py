from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

# Arrange
browser.config.hold_browser_open = True
browser.open('https://google.com/ncr')

# Act
s('[type="text"]').type('yashaka selene').press_enter()
browser.all('#search .g').first.element('h3').click()

# Assert
ss('[href="/yashaka/selene"]').should(have.size(3))

browser.close()
