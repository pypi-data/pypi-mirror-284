import os
import allure
import json
from datetime import datetime

from Framework.Utils.create_general_directory import RESULTS_DIR


class AllureUtils:
    @staticmethod
    def _get_timestamp():
        return datetime.now().strftime("%d-%m-%Y__%H-%M-%S")

    @staticmethod
    def attach_screenshot(driver, name='screenshot'):
        timestamp = AllureUtils._get_timestamp()
        allure.attach(driver.screenshot_as_png, name=f"{name}_{timestamp}", attachment_type=allure.attachment_type.PNG)

    @staticmethod
    def attach_text(text, name='text_attachment', attachment_type=allure.attachment_type.TEXT):
        timestamp = AllureUtils._get_timestamp()
        allure.attach(text, name=f"{name}_{timestamp}", attachment_type=attachment_type)

    @staticmethod
    def attach_html(html_content, name='html_attachment'):
        timestamp = AllureUtils._get_timestamp()
        allure.attach(html_content, name=f"{name}_{timestamp}", attachment_type=allure.attachment_type.HTML)

    @staticmethod
    def attach_file(file_path, name=None):
        timestamp = AllureUtils._get_timestamp()
        allure.attach.file(file_path, name=f"{name or os.path.basename(file_path)}_{timestamp}")

    @staticmethod
    def attach_json(json_data, name='json_attachment'):
        timestamp = AllureUtils._get_timestamp()
        allure.attach(json.dumps(json_data), name=f"{name}_{timestamp}", attachment_type=allure.attachment_type.JSON)

    @staticmethod
    def attach_xml(xml_data, name='xml_attachment'):
        timestamp = AllureUtils._get_timestamp()
        allure.attach(xml_data, name=f"{name}_{timestamp}", attachment_type=allure.attachment_type.XML)

    @staticmethod
    def attach_pdf(pdf_data, name='pdf_attachment'):
        timestamp = AllureUtils._get_timestamp()
        allure.attach(pdf_data, name=f"{name}_{timestamp}", attachment_type=allure.attachment_type.PDF)

    @staticmethod
    def attach_jpg(jpg_data, name='jpg_attachment'):
        timestamp = AllureUtils._get_timestamp()
        allure.attach(jpg_data, name=f"{name}_{timestamp}", attachment_type=allure.attachment_type.JPG)

    @staticmethod
    def attach_gif(gif_data, name='gif_attachment'):
        timestamp = AllureUtils._get_timestamp()
        allure.attach(gif_data, name=f"{name}_{timestamp}", attachment_type=allure.attachment_type.GIF)

    @staticmethod
    def attach_screenshot_to_allure(self, step_name: str = "Screenshot"):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshots_dir = os.path.join(RESULTS_DIR, "Screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshots_dir, f"{step_name.replace(' ', '_').lower()}_{timestamp}.png")
        self.page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG)

    @staticmethod
    def attach_video_to_allure(self, step_name: str = "Complete Test Case Video"):
        with allure.step(step_name):
            allure.attach.file(self.page.video.path(), attachment_type=allure.attachment_type.WEBM)
