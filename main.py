import asyncio
import io

import pyppeteer
from bs4 import BeautifulSoup

from city_dict import cities_dict
from db import init, close, Job


async def fetch_html_with_js(url):
    browser = await pyppeteer.launch()
    page = await browser.newPage()
    await page.goto(url, waitUntil='domcontentloaded', timeout=60000)  # Очікувати завершення мережевих запитів
    # await page.waitForSelector('items-items-kAJAg', {'timeout': 60000})
    content = await page.content()
    await browser.close()
    # with io.open("context_f.html", "w", encoding="utf-8") as file:
    #     file.write(content)
    return content
# async def fetch_html_with_js(url):
#     options = Options()
#     options.headless = True
#     browser = webdriver.Chrome(options=options)
#
#     try:
#         browser.get(url)
#         content = browser.page_source
#         return content
#     finally:
#         browser.quit()


async def parse_avito_page(url, vacancies_limit=10):
    try:
        html_ = await fetch_html_with_js(url)
        # with io.open("context.html", "w", encoding="utf-8") as file:
        #     file.write(html_)
        soup = BeautifulSoup(html_, "html.parser")

        vacancies = []

        job_elements = soup.find_all("div", class_="styles-module-theme-CRreZ")  # items-items-kAJAg, styles-module-theme-CRreZ
        print(f"Found {len(job_elements)} job elements on the page.")

        for job_element in job_elements[:vacancies_limit]:
            title_element = job_element.find("div", class_="iva-item-title-py3i_")
            salary_element = job_element.find("div", class_="iva-item-priceStep-uq2CQ")  # iva-item-priceStep-uq2CQ
            description_element = job_element.find("div", class_="iva-item-descriptionStep-C0ty1")  # iva-item-descriptionStep-C0ty1

            # Перевірка, чи елементи знайдено перед викликом get_text()
            title = title_element.get_text(strip=True) if title_element else "No title"
            salary = salary_element.get_text(strip=True) if salary_element else "No salary"
            description = description_element.get_text(strip=True) if description_element else "No description"

            vacancy_data = {
                "title": title,
                "salary": salary,
                "description": description,
            }

            vacancies.append(vacancy_data)
        print(vacancies)
        print(f"Parsed {len(vacancies)} job vacancies from the page.")
        return vacancies

    except Exception as e:
        print(f"Error parsing page: {e}")
        return []


async def save_to_database(data, city, link):
    print(f"Data to insert into database: {data}")
    # Вставка даних в базу даних
    for item in data:
        print(f"Inserting into database: {city} - {link} - {item['title']} - {item['salary']} - {item['description']}")
        await Job.create(
            title=item['title'],
            salary=item['salary'],
            description=item['description'],
            city=city,
            link=link
        )


async def main():
    await init()

    for city, link in cities_dict.items():
        avito_base_url = f"https://www.avito.ru/{city}/vakansii"
        results = await parse_avito_page(avito_base_url, vacancies_limit=10)

        # Зберігаємо дані в базу даних
        print(f"Found {len(results)} vacancies in {city}")
        await save_to_database(results, city, link)

if __name__ == "__main__":
    asyncio.run(main())
