from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    # Локаторы
    PRODUCT_TITLE = (By.CLASS_NAME, "product_label")  # Заголовок "Products"
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_DESC = (By.CLASS_NAME, "inventory_item_desc")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.XPATH, ".//button[text()='ADD TO CART']")
    REMOVE_BUTTON = (By.XPATH, ".//button[text()='REMOVE']")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def init(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_page_loaded(self):
        """Проверяет, загружена ли страница товаров."""
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLE)).is_displayed()

    def get_product_titles(self):
        """Возвращает список названий всех товаров на странице."""
        items = self.driver.find_elements(*self.ITEM_NAME)
        return [item.text for item in items]

    def get_product_descriptions(self):
        """Возвращает список описаний всех товаров."""
        items = self.driver.find_elements(*self.ITEM_DESC)
        return [item.text for item in items]

    def get_product_prices(self):
        """Возвращает список цен всех товаров."""
        prices = self.driver.find_elements(*self.ITEM_PRICE)
        return [price.text for price in prices]

    def add_product_to_cart_by_name(self, product_name):
        """Добавляет товар в корзину по его названию."""
        items = self.driver.find_elements(*self.INVENTORY_ITEM)
        for item in items:
            name_elem = item.find_element(*self.ITEM_NAME)
            if name_elem.text == product_name:
                item.find_element(*self.ADD_TO_CART_BUTTON).click()
                return
        raise ValueError(f"Product '{product_name}' not found on the page.")

    def click_shopping_cart(self):
        """Переходит в корзину."""
        self.driver.find_element(*self.SHOPPING_CART_LINK).click()

    def select_sort_option(self, option_text):
        """Выбирает опцию сортировки из выпадающего списка."""
        dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
        dropdown.click()
        dropdown.find_element(By.XPATH, f"//option[text()='{option_text}']").click()