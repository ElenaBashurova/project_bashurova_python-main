import allure
from selene import have, browser



class CategoryPageName:

    def select_subcategory(self, subcategory):
        with allure.step(f'Выбрать подкатегорию: "{subcategory}"'):
            browser.element('#bx_3909807802_458770').click()
            browser.element('[href="/catalog/3888/"]').should(have.text(subcategory))


category_name = CategoryPageName()