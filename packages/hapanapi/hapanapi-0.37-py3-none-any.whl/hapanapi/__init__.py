import json
import re
import time
import logging
import datetime
import requests
from hapanapi.driver_tools import driver_init, CHROME_PATH, CHROME_BIN
from hapanapi.parsers import schedule_date_parser
from hapanapi.constants import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger("HapanaINIT")


class Hapana:
    def __init__(self, username, password, driver=None):
        self.username = username
        self.password = password
        if not driver:
            self.driver = driver_init(CHROME_PATH=CHROME_PATH, CHROME_BIN=CHROME_BIN)
        else:
            self.driver = driver

        # First Timer Report
        self.trial_present_sessions = {}

    def login(self, platform='core'):
        logger.info("--- Starting to login ---")
        self.driver.get(f"https://{platform}.hapana.com/")
        if platform == 'grow':
            logger.info("Unable to login, please re-code this again")
        else:
            signin_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'signin')))
            self.driver.find_element(By.NAME, 'email').send_keys(self.username)
            self.driver.find_element(By.NAME, 'password').send_keys(self.password)
            signin_button.click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'user-welcome')))
        logger.info("--- Login completed ---")

    def get_table(self):
        headers_el = self.driver.find_elements(By.XPATH, "//table[@id='masterTable']/thead/tr/th")
        row_el = self.driver.find_elements(By.XPATH, "//table[@id='masterTable']/tbody/tr")
        headers = [value.get_attribute("innerText") for value in headers_el]
        data = []
        for row in row_el:
            data_el = row.find_elements(By.TAG_NAME, "td")
            single_row = {}
            for i in range(len(headers)):
                single_row[headers[i]] = data_el[i].get_attribute("innerText")
            data.append(single_row)
        return data

    def add_client(self, first_name, last_name, email, phone, platform='core', url_override=None, method="form"):
        if platform == 'core' and method == "form":
            data = {
                "firstname": first_name,
                "lastname": last_name,
                "email": email,
                "phone": phone
            }
            headers = {}
            res = requests.request(
                "POST",
                "https://core.hapana.com/index.php?route=dashboard/leads/gymleadclient&trid=MTU1Nzk4Ng==",
                headers=headers,
                data=data,
                files=[]
            )
            return res
        elif platform == "core":
            self.driver.get(url_override if url_override else CORE_ADD_CLIENT_URL)
            time.sleep(2)
            self.driver.find_element(By.ID, 'first_name').send_keys(first_name)
            self.driver.find_element(By.ID, 'last_name').send_keys(last_name)
            self.driver.find_element(By.ID, 'email').send_keys(email)
            self.driver.find_element(By.ID, 'phone').send_keys(phone)
            self.driver.find_element(By.ID, "btn-add-client").click()
            time.sleep(2)
            return None
        elif platform == 'grow':
            self.driver.get(url_override if url_override else GROW_ADD_CLIENT_URL)
            time.sleep(1)
            self.driver.find_element(By.NAME, 'first_name').send_keys(first_name)
            self.driver.find_element(By.NAME, 'last_name').send_keys(last_name)
            self.driver.find_element(By.NAME, 'email').send_keys(email)
            self.driver.find_element(By.NAME, 'phone').send_keys(phone)
            self.driver.find_element(By.CLASS_NAME, "btn").click()
            time.sleep(2)
            return None
        else:
            logger.info("Wrong platform specified, client not added")
            return None

    def find_client(self, email=None, phone=None, platform='core'):
        logger.info("--- Starting to find client ---")
        if platform == 'core':
            self.driver.get(CORE_CLIENT_SUMMARY_URL)
            if email:
                search_term = email
            elif phone:
                search_term = phone
            else:
                logger.error("Did not specify email or phone, unable to search")
                return None
            searchbar = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, f"//input[@id='clientsearch']")))
            searchbar.send_keys(search_term)

            time.sleep(4)
            client_table = self.driver.find_elements(By.XPATH, f"//tbody[@id='clientresults']/tr")
            if len(client_table) < 1:
                logger.error(f"{search_term} is not found in {platform}!")
                return None
            elif len(client_table) > 2:
                logger.error("Client might not be unique, please try again with proper parameters")
                logger.error(f"Search Term: {search_term}")
                for client in client_table:
                    cols = client.find_elements(By.TAG_NAME, "td")
                    logger.info(cols[1].get_attribute('innerText'))
                return None
            else:
                first_client = client_table[0]  # TODO verify with phone number as well
                cols = first_client.find_elements(By.TAG_NAME, "td")
                client_link = cols[1].get_attribute('onclick')
                client_link = client_link.replace("window.location.href=", "").strip("'")
                logger.info("--- Client found ---")
                logger.info(f"Client Link: {client_link}")
                return client_link
        else:
            logger.error(f"The current platform {platform} is not supported")
            return None

    def find_membership(self, client_page):
        logger.info("--- Starting to find package ---")
        self.driver.get(client_page)
        time.sleep(3)
        logger.info(self.driver.find_element(By.XPATH, f"//tbody[@id='resultsrec']/tr").get_attribute("outerHTML"))
        all_memberships = self.driver.find_elements(By.XPATH, f"//tbody[@id='resultsrec']/tr")
        if len(all_memberships) < 1:
            logger.error("Can't find membership for this user!")
            return None
        else:
            for item in all_memberships:
                package_type = item.find_element(By.XPATH, "//td[@class='pkgType']/span").get_attribute('innerText')
                if package_type != "Active" and package_type != "Suspended":
                    package_link = None
                    continue
                else:
                    package_link = item.find_element(By.XPATH, "//td[@class='transaction-action']/a").get_attribute(
                        'href')
                    logger.info("--- Found package ---")
                    return package_link, package_type
            if not package_link:
                logger.error("No package found!")
                return package_link, None

    def pause_membership(self, package_page, start_date=None, end_date=None, date_format=None):
        logger.info("--- Starting to pause membership ---")
        self.driver.get(package_page)
        edit_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//i[@data-target='#editStatus']")))
        self.driver.execute_script("arguments[0].click();", edit_button)
        logger.info("--> Edit status button clicked")
        time.sleep(1)
        update_status_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "set_payment_status")))
        self.driver.execute_script("arguments[0].click();", update_status_button)
        logger.info("--> Status dropdown clicked")
        time.sleep(1)
        status_update_options = self.driver.find_elements(By.XPATH, "//select[@id='set_payment_status']/option")
        for option in status_update_options:
            if option.get_attribute("innerText") == "Suspended":
                option.click()
                break
        logger.info("--> Change to suspended")
        start_date_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "suspension_start_type")))
        end_date_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "reactive_duration_type")))
        if start_date:
            start_date_button.click()
            start_type_options = self.driver.find_elements(By.XPATH, "//select[@id='suspension_start_type']/option")
            for option in start_type_options:
                if option.get_attribute("innerText") == "On Date":
                    option.click()
                    break
            logger.info("Updated to 'On Date'")
            self.driver.find_element(By.ID, "suspension_date").click()
            sep = "/" if "/" in start_date else "-"
            if not date_format or date_format == "DDMMYYYY":
                day, month, year = start_date.split(sep)
            else:
                month, day, year = start_date.split(sep)
            self.datepicker(day=day, month=month, year=year)
            logger.info("Updated Start Date")
        if end_date:
            end_date_button.click()
            end_type_options = self.driver.find_elements(By.XPATH, "//select[@id='reactive_duration_type']/option")
            for option in end_type_options:
                if option.get_attribute("innerText") == "On Date":
                    option.click()
                    break
            logger.info("Updated to 'On Date'")
            self.driver.find_element(By.ID, "reactivation_date").click()
            sep = "/" if "/" in end_date else "-"
            if not date_format or date_format == "DDMMYYYY":
                day, month, year = end_date.split(sep)
            else:
                month, day, year = end_date.split(sep)
            self.datepicker(day=day, month=month, year=year)
            logger.info("Updated End Date")
        test_if_present = self.driver.find_element(By.XPATH,
                                                   "//div[@id='confirmtmodal']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-footer']")
        logger.info(test_if_present.get_attribute("outerHTML"))
        update_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-footer']/button[@id='updateStatus']")))
        update_button.click()
        time.sleep(1)
        test_if_present = self.driver.find_element(By.XPATH,
                                                   "//div[@id='confirmtmodal']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-footer']")
        logger.info(test_if_present.get_attribute("outerHTML"))
        confirm_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                                               "//div[@id='confirmtmodal']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-footer']/button[@id='confirmOk']")))
        self.driver.execute_script("arguments[0].click();", confirm_button)
        time.sleep(3)
        logger.info("--- Membership paused successfully ---")

    def datepicker(self, year, month, day,
                   year_tag="ui-datepicker-year", month_tag="ui-datepicker-month", day_tag="ui-datepicker-calendar"):
        # Year Picker
        self.driver.find_element(By.CLASS_NAME, year_tag).click()
        time.sleep(1)
        year_options = self.driver.find_elements(By.XPATH, f"//select[@class='{year_tag}']/option")
        for option in year_options:
            if option.get_attribute("innerText") == str(year):
                option.click()
                break
        # Month Picker
        self.driver.find_element(By.CLASS_NAME, month_tag).click()
        time.sleep(1)
        month_options = self.driver.find_elements(By.XPATH, f"//select[@class='{month_tag}']/option")
        for option in month_options:
            if option.get_attribute("value") == str(int(month) - 1):
                option.click()
                break
        # Day Picker
        day_options = self.driver.find_elements(By.XPATH, f"//table[@class='{day_tag}']/tbody/tr/td")
        for option in day_options:
            if option.get_attribute("innerText") == str(int(day)):
                option.click()
                break

    def schedule(self, date):
        today, day, day_of_week = schedule_date_parser(date)
        self.driver.get("https://core.hapana.com/index.php?route=dashboard/schedule")
        time.sleep(2)
        elems = self.driver.find_elements(By.XPATH,
                                          f"//div[@class='fc-content-skeleton']/table/tbody/tr[1]/td[{day_of_week}]/div[@class='fc-content-col']/div[@class='fc-event-container']/a")
        time.sleep(1)
        session_ids = [elem.get_attribute('href').split("=")[-1] for elem in elems]
        for session_id in session_ids:
            link = f"https://core.hapana.com/index.php?route=dashboard/schedule&seid={session_id}&dt={day}&eid={session_id}&curr={today}"
            self.driver.get(link)
            time.sleep(2)
            class_name = self.driver.find_element(By.XPATH, f"//div[@id='eventLoad']/div[1]/h4").text
            class_name = re.sub('[^A-Za-z0-9 ]+', '', class_name)
            user_table = self.driver.find_elements(By.XPATH,
                                                   f"//ul[@id='attendeesList']/li[contains(@class,'d-lg-block')]")
            if len(user_table) < 1:
                logger.info(f"{class_name} is empty!")
            else:
                for item in user_table[1:]:
                    cols = item.find_elements(By.TAG_NAME, "div")
                    visits = cols[1].find_element(By.CLASS_NAME, "milestone").get_attribute('innerText')
                    try:
                        if int(visits) > 1:
                            continue
                    except Exception as e:
                        print(f"Error: {e} detected in {class_name}")
                        continue
                    name = cols[1].find_element(By.TAG_NAME, "a").get_attribute('innerText')
                    name = re.sub('[^A-Za-z0-9 ]+', '', name)
                    package_name = cols[5].find_element(By.TAG_NAME, "span").get_attribute('innerText')
                    if "ClassPass" in package_name:
                        package_name = "ClassPass"
                    else:
                        booked_sessions = re.findall("\(\d{1,}\/\d{1,}\)", package_name)
                        if len(booked_sessions) > 0:
                            booked_pattern = "\\" + booked_sessions[0][:-1] + "\\" + booked_sessions[0][-1]
                            package_name = re.sub(booked_pattern, '', package_name)
                            # num, denom = booked_sessions[0].strip("()").split("/")

                    # home_location = cols[1].find_element(By.XPATH, f"//span[@aria-label='Home Location Alert']")
                    # print(home_location.get_attribute('style'))
                    if class_name not in self.trial_present_sessions:
                        self.trial_present_sessions[class_name] = [
                            {"name": name, "package": package_name, "visits": int(visits)}]
                    else:
                        self.trial_present_sessions[class_name].append(
                            {"name": name, "package": package_name, "visits": int(visits)})
                    print({
                        "name": name,
                        "visits": visits,
                        "package": package_name
                    })

    def get_absent_report(self, start_date, end_date, required_packages):
        self.driver.get(
            f"https://core.hapana.com/index.php?route=dashboard/advreports&report_type=client&filter=clientabsent2weeks&date_from={start_date}&date_to={end_date}")
        add_filters_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "addMoreFilters")))
        self.driver.execute_script("arguments[0].click();", add_filters_button)
        parent_selection_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "parent_selection2")))
        self.driver.execute_script("arguments[0].click();", parent_selection_button)
        field_options = self.driver.find_elements(By.XPATH, "//select[@id='parent_selection2']/option")
        for option in field_options:
            if option.get_attribute("innerText") == "Package Name":
                option.click()
                break
        package_options = self.driver.find_elements(By.XPATH, "//select[@id='pkg_names']/option")
        first_down = False
        for option in package_options:
            if option.get_attribute("innerText") in required_packages:
                logger.info(f"Clicking {option.get_attribute('innerText')}")
                if first_down:
                    ActionChains(self.driver).key_down(Keys.COMMAND).click(option).key_up(Keys.COMMAND).perform()
                else:
                    logger.info("First click")
                    ActionChains(self.driver).click(option).perform()
                    first_down = True
        parent_selection_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@data-original-title='Filter']")))
        self.driver.execute_script("arguments[0].click();", parent_selection_button)
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.ID, "pre-loading")))
        data = self.get_table()
        return data

    def get_transactions(self, days_back=1):
        today_raw = datetime.datetime.now()
        today = today_raw.strftime("%d/%m/%Y")
        day = (today_raw - datetime.timedelta(days=days_back)).strftime("%d/%m/%Y")
        url = f"https://core.hapana.com/index.php?route=dashboard/advreports&report_type=client&filter=getAllNetRevenueDetail2&date_from={day}&date_to={today}"
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.ID, "pre-loading")))
        edit_report_settings_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@data-target='#reportSettings']")))
        self.driver.execute_script("arguments[0].click();", edit_report_settings_button)
        telephone_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "displaytelephone")))
        self.driver.execute_script("arguments[0].click();", telephone_button)
        refresh_report_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, "//form[@id='displayoptions']/div[@class='modal-footer']/button")))
        self.driver.execute_script("arguments[0].click();", refresh_report_button)
        data = self.get_table()
        return data

    def get_first_visits_completed(self, days_back=1):
        today_raw = datetime.datetime.now()
        today = today_raw.strftime("%d/%m/%Y")
        day = (today_raw - datetime.timedelta(days=days_back)).strftime("%d/%m/%Y")
        url = f"https://core.hapana.com/index.php?route=dashboard/advreports&report_type=client&filter=firstvisits&date_from={day}&date_to={today}"
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.ID, "pre-loading")))
        data = self.get_table()
        return data

    def get_member_movements(self, days_back=1):
        today_raw = datetime.datetime.now()
        today = today_raw.strftime("%d/%m/%Y")
        day = (today_raw - datetime.timedelta(days=days_back)).strftime("%d/%m/%Y")
        url = f"https://core.hapana.com/index.php?route=dashboard/advreports&report_type=client&filter=membermovement&date_from={day}&date_to={today}"
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.ID, "pre-loading")))
        data = self.get_table()
        return data

    def add_credit(self, email, credit_type="FREE"):
        self.driver.get("https://core.hapana.com/index.php?route=payments/payments/addnew")
        logger.info("--- Starting to add package ---")
        packages_button = WebDriverWait(self.driver, 7).until(
            EC.visibility_of_element_located((By.XPATH, "//li[@data-target='#sessionPkg']")))
        self.driver.execute_script("arguments[0].click();", packages_button)
        single_free_button = WebDriverWait(self.driver, 7).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@data-pkgid='54122']")))
        self.driver.execute_script("arguments[0].click();", single_free_button)
        time.sleep(1)
        add_to_cart_button = WebDriverWait(self.driver, 7).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "sessionPkgSale")))
        self.driver.execute_script("arguments[0].click();", add_to_cart_button)

        logger.info("--- Starting to add client to package ---")
        add_client_button = WebDriverWait(self.driver, 7).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@data-original-title='Add Client']")))
        self.driver.execute_script("arguments[0].click();", add_client_button)
        searchbar = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, f"//input[@id='searchClient']")))
        searchbar.send_keys(email)

        time.sleep(6)
        client_table = self.driver.find_elements(By.XPATH, f"//ul[@id='clientresults']/li")

        if len(client_table) < 1:
            logger.error(f"{email} user is not found in Core!")
            raise Exception("User is not found in Core!")
        else:
            first_client = client_table[0]
            cols = first_client.find_elements(By.TAG_NAME, "label")
            click_checkbox = cols[0].click()
            time.sleep(3)

            add_client_button = WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located((By.XPATH, "//button[@id='addclientlist']")))
            self.driver.execute_script("arguments[0].click();", add_client_button)

            add_client_button = WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located((By.XPATH, "//button[@id='checkoutpaymentsreq']")))
            self.driver.execute_script("arguments[0].click();", add_client_button)

            logger.info("--- Done adding credit, pausing for the page to load ---")
            time.sleep(3)

            return {
                "message": "Credit successfully added!"
            }

    def add_schedule(self, email, date, time_interval, class_type):
        logger.info("--- Starting to add schedule ---")
        today, day, day_of_week = schedule_date_parser(date)
        self.driver.get("https://core.hapana.com/index.php?route=dashboard/schedule")
        time.sleep(3)
        elems = self.driver.find_elements(By.XPATH,
                                          f"//div[@class='fc-content-skeleton']/table/tbody/tr[1]/td[{day_of_week}]/div[@class='fc-content-col']/div[@class='fc-event-container']/a")
        time.sleep(1)
        session_ids = [elem.get_attribute('href').split("=")[-1] for elem in elems]

        logger.info("--- Finding the exact date and interval of class ---")
        if len(elems) <= 6:  # Weekday sweat
            session_id = session_ids[time_interval]
        elif len(elems) >= 10:  # Weekday Perform/Move
            before, after = (time_interval * 2), (time_interval * 2) + 1
            print(before, after)
            if class_type.upper() in elems[before].find_element(By.CLASS_NAME, "fc-title").get_attribute(
                    'innerText').upper():  # Found in before
                session_id = session_ids[before]
            else:
                session_id = session_ids[after]
        else:
            raise Exception("Unable to find class specified!")

        logger.info("--- Adding client to class ---")
        link = f"https://core.hapana.com/index.php?route=dashboard/schedule&seid={session_id}&dt={day}&eid={session_id}&curr={today}"
        self.driver.get(link)
        add_client_button = WebDriverWait(self.driver, 7).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@data-bs-target='#invite']")))
        self.driver.execute_script("arguments[0].click();", add_client_button)
        searchbar = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, f"//input[@id='searchClient']")))
        searchbar.send_keys(email)
        time.sleep(6)
        client_table = self.driver.find_elements(By.XPATH, f"//ul[@class='client-list list-unstyled']/li")

        if len(client_table) < 1:
            logger.error(f"{email} user is not found in Core!")
            raise Exception("User is not found in Core!")
        else:
            first_client = client_table[0]
            cols = first_client.find_elements(By.TAG_NAME, "label")
            click_checkbox = cols[0].click()
            time.sleep(3)

            try:
                error_found = WebDriverWait(self.driver, 1).until(
                    EC.visibility_of_element_located((By.XPATH, "//p[@id='add_session_client_error']")))
            except:
                error_found = None
            if error_found:
                raise Exception(error_found.get_attribute("innerText"))

            logger.info("--- Click add ---")
            add_client_button = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='modal-footer text-center']/button[@type='submit']")))
            self.driver.execute_script("arguments[0].click();", add_client_button)

        logger.info("--- Done adding class, pausing for the page to load ---")
        time.sleep(5)

        return {
            "message": "Class successfully added!"
        }

    def log_message(self, name, phone, message):

        def set_value_via_js(element, value):
            self.driver.execute_script("arguments[0].value = arguments[1];", element, value)
            self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", element)

        self.driver.get(GROW_LOG_INCOMING_MESSAGE_URL)
        # Wait for the chat widget to be present in the DOM
        chat_widget = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'chat-widget'))
        )

        # Access the shadow root
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', chat_widget)

        # Find the button inside the shadow root
        widget_button = WebDriverWait(shadow_root, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.widget-open-icon.active'))
        )

        # Use JavaScript to click the element to avoid interception
        self.driver.execute_script("arguments[0].click();", widget_button)

        # Fill the 'name' field
        name_field = WebDriverWait(shadow_root, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="name"]'))
        )
        try:
            name_field.send_keys(name)
        except ElementNotInteractableException:
            set_value_via_js(name_field, name)

        # Fill the 'phone' field
        phone_field = WebDriverWait(shadow_root, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="phone"]'))
        )
        phone = "+" + phone
        try:
            phone_field.send_keys(phone)
        except ElementNotInteractableException:
            set_value_via_js(phone_field, phone)

        # Fill the 'message' field
        message_field = WebDriverWait(shadow_root, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea[name="message"]'))
        )
        try:
            message_field.send_keys(message)
        except ElementNotInteractableException:
            set_value_via_js(message_field, message)

        # Click the 'Send' button
        send_button = WebDriverWait(shadow_root, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#lc_text-widget--send-btn'))
        )
        self.driver.execute_script("arguments[0].click();", send_button)

        time.sleep(5)
        return None
