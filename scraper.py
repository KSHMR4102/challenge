from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        print("Ingresando a MercadoLibre...")
        page.goto('https://www.mercadolibre.com')
        page.screenshot(path='screenshots/homePage.png')

        print("Seleccionando México como país...")
        page.click('text=México')
        page.screenshot(path='screenshots/countrySelection.png')

        print("Buscando 'Playstation 5'...")
        page.fill('input[name="as_word"]', 'playstation 5')
        page.press('input[name="as_word"]', 'Enter')
        page.screenshot(path='screenshots/searchResults.png')

        print("Filtrando por condición 'Nuevo'...")
        page.wait_for_selector('span:has-text("Nuevo")', timeout=60000)
        page.click('span:has-text("Nuevo")')
        page.screenshot(path='screenshots/filterNew.png')

        print("Filtrando por ubicación 'Distrito Federal' (CDMX)...")
        page.wait_for_selector('span:has-text("Distrito Federal")', timeout=60000)
        page.click('span:has-text("Distrito Federal")')
        page.screenshot(path='screenshots/filterLocation.png')

        print("Haciendo clic en 'Más relevantes'...")
        page.wait_for_selector('button[aria-labelledby*="-label"]', timeout=60000)
        page.click('button[aria-labelledby*="-label"]')
        page.screenshot(path='screenshots/clickMoreRelevant.png')

        print("Filtrando por 'Mayor precio'...")
        page.wait_for_selector('text="Mayor precio"', timeout=60000)
        page.click('text="Mayor precio"')
        page.screenshot(path='screenshots/clickHighestPrice.png')

        # Esperar que los productos estén visibles
        try:
            print("Esperando los resultados de búsqueda...")
            page.wait_for_selector('div.ui-search-result__content-wrapper', state='visible', timeout=100000)  # Aumenté el tiempo de espera

            # Asegurarse de que los productos están presentes
            products = page.query_selector_all('div.ui-search-result__content-wrapper')
            if len(products) == 0:
                print("No se encontraron productos.")
                raise Exception("No se encontraron productos visibles.")
            
            print(f"Se encontraron {len(products)} productos. Tomando los primeros 5...")

            products = products[:5]  # Tomar solo los primeros 5
            product_list = []

            for product in products:
                name = product.query_selector('.ui-search-item_title').inner_text() if product.query_selector('.ui-search-item_title') else 'No title'
                price_element = product.query_selector('div.ui-search-price_second-line span.andes-money-amount_fraction')
                price = price_element.inner_text() if price_element else 'No price'
                product_list.append({'name': name, 'price': price})

            page.screenshot(path='screenshots/productsList.png')

            print("Primeros 5 productos:")
            for index, product in enumerate(product_list):
                print(f"{index + 1}. {product['name']} - {product['price']}")

            assert len(product_list) >= 5
        except Exception as e:
            page.screenshot(path='screenshots/errorFetchingProducts.png')
            print(f'Error obteniendo los productos: {e}')
            raise e

    finally:
        print("Cerrando el navegador...")
        browser.close()