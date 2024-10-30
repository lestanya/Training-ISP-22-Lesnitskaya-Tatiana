import bs4
import re
import time
import random


class FlatPageParser:
    def __init__(self, session, url):
        self.session = session
        self.url = url

    def __load_page__(self):
        res = self.session.get(self.url)
        if res.status_code == 429:
            time.sleep(10)
        res.raise_for_status()
        self.offer_page_html = res.text
        self.offer_page_soup = bs4.BeautifulSoup(self.offer_page_html, 'html.parser')

    def __parse_flat_offer_page_json__(self):
        page_data = {
            "year_of_construction": -1,
            "object_type": -1,
            # "ceiling_height": -1,
            # "ceiling_height": -1,
            "have_loggia": -1,
            "parking_type": -1,
            "house_material_type": -1,
            "heating_type": -1,
            "finish_type": -1,
            "living_meters": -1,
            "kitchen_meters": -1,
            "floor": -1,
            "floors_count": -1,
            "phone": "",
        }
        ot = self.offer_page_soup.select_one('[data-name="OfferSummaryInfoItem"] p:nth-of-type(2)').get_text()
        page_data["object_type"] = ot
        time.sleep(random.uniform(0, 5))
        # ch = self.offer_page_soup.select_one('[data-name="OfferSummaryInfoItem"] p:nth-of-type(10)').get_text()
        # page_data["ceiling_height"] = ch
        # it = self.offer_page_soup.select_one('[data-name="OfferSummaryInfoItem"] p:nth-of-type(10)').get_text()
        # page_data["ceiling_height"] = it
        # et = self.offer_page_soup.select_one('[data-name="OfferSummaryInfoItem"] p:nth-of-type(14)').get_text()
        # page_data["have_loggia"] = et

        pt_elements = self.offer_page_soup.select('[data-name="OfferSummaryInfoItem"] p')
        for i, p_element in enumerate(pt_elements):
            if "Парковка" in p_element.get_text():
                parking_type_element = pt_elements[i + 1]
                print(i)
                page_data["parking_type"] = parking_type_element.get_text()
                time.sleep(random.uniform(0, 5))
                break
        else:
            page_data["parking_type"] = -1

        hl_elements = self.offer_page_soup.select('[data-name="OfferSummaryInfoItem"] p')
        for i, hl_element in enumerate(hl_elements):
            if "Балкон/лоджия" in hl_element.get_text():
                have_loggia_element = hl_elements[i + 1]
                print(i)
                page_data["have_loggia"] = have_loggia_element.get_text()
                time.sleep(random.uniform(0, 5))
                break
        else:
            page_data["have_loggia"] = -1
        ch_elements = self.offer_page_soup.select('[data-name="OfferSummaryInfoItem"] p')
        for i, ch_element in enumerate(ch_elements):
            if "Высота потолков" in ch_element.get_text():
                ceiling_height_element = ch_elements[i + 1]
                print(i)
                page_data["ceiling_height"] = ceiling_height_element.get_text()
                time.sleep(random.uniform(0, 5))
                break
        else:
            page_data["ceiling_height"] = -1


        # et = self.offer_page_soup.select_one('[data-name="OfferSummaryInfoItem"] p:nth-of-type(2)').get_text()
        # page_data["heating_type"] = et


        spans = self.offer_page_soup.select("span")
        for index, span in enumerate(spans):
            # if "Тип жилья" == span.text:
            #     page_data["object_type"] = spans[index + 1].text

            if "Тип дома" == span.text:
                page_data["house_material_type"] = spans[index + 1].text
                time.sleep(random.uniform(0, 5))

            # if "Отопление" == span.text:
            #     page_data["heating_type"] = spans[index + 1].text

            if "Отделка" == span.text:
                page_data["finish_type"] = spans[index + 1].text
                time.sleep(random.uniform(0, 5))

            

            if "Площадь кухни" == span.text:
                page_data["kitchen_meters"] = spans[index + 1].text
                time.sleep(random.uniform(0, 5))

            if "Жилая площадь" == span.text:
                page_data["living_meters"] = spans[index + 1].text
                time.sleep(random.uniform(0, 5))

            if "Год постройки" in span.text:
                page_data["year_of_construction"] = spans[index + 1].text
                time.sleep(random.uniform(0, 5))

            if "Год сдачи" in span.text:
                page_data["year_of_construction"] = spans[index + 1].text
                time.sleep(random.uniform(0, 5))

            if "Этаж" == span.text:
                ints = re.findall(r'\d+', spans[index + 1].text)
                if len(ints) == 2:
                    page_data["floor"] = int(ints[0])
                    page_data["floors_count"] = int(ints[1])
                time.sleep(random.uniform(0, 5))

        if "+7" in self.offer_page_html:
            page_data["phone"] = self.offer_page_html[self.offer_page_html.find("+7"): self.offer_page_html.find("+7") + 16].split('"')[0]. \
                replace(" ", ""). \
                replace("-", "")
            time.sleep(random.uniform(0, 5))

        return page_data

    def parse_page(self):
        self.__load_page__()
        return self.__parse_flat_offer_page_json__()
