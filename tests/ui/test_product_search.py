import allure
import pytest
from diploma_project.pages.product_pages import product_name
from diploma_project.pages.product_select import search_name


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@allure.story('Поиск товара')
@pytest.mark.xfail(reason='Этот тест не стабилен')
@allure.link('https://www.officemag.ru', name='Test')
@allure.title('Поиск товара "Кресло компьютерное"')
@pytest.mark.web
def test_search_product(browser_configs):
    search_name.open_page()
    search_name.search_product_enter("Кресло компьютерное")
    product_name.page_name_product("Кресло BRABIX «Fly MG-396», с подлокотниками, сетка, черное, 532083")


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@pytest.mark.web
@allure.title('Поиск товара "Шкаф"')
def test_search_by_part_of_name(browser_configs):
    search_name.open_page()
    search_name.search_part_product('Шк')


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@pytest.mark.web
@allure.title('Поиск товара "Кофе"')
def test_search_by_foreign_name(browser_configs):
    search_name.open_page()
    search_name.search_foreign_product('Кофе в зернах Якобс')
    product_name.foreign_name_product('Кофе в зернах JACOBS «Crema» 1 кг')


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@pytest.mark.web
@allure.title('Поиск товара "Чай"')
def test_search_by_foreign_keyboard_layout(browser_configs):
    search_name.open_page()
    search_name.search_keyboard_layout_product('Tea green')
