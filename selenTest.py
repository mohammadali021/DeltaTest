from time import sleep

from selenium import webdriver
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest


class login(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        username = "09935263066"
        password = "123456789"

    def test_Dleta_web(self):
        self.driver.get("https://www.delta.ir")
        self.driver.maximize_window()
        # cities_list = ["تهران","کرج","کیش","رشت","پردیس","پرند","اصفهان","مشهد","تبریز","شیراز","شهرهای ساحلی شمال","سایر شهرها"]
        cities_list = ["سایر شهرها"]
        for city in cities_list:
            element = self.driver.find_element(By.LINK_TEXT, city).click()
            sleep(8)
            if city == "شهرهای ساحلی شمال":
                north_cities = ["بابلسر", "رویان", "چالوس", "چابکسر", " انزلی", "رشت", "لاهیجان"]

                for north_city in north_cities:
                    element = self.driver.find_element(By.PARTIAL_LINK_TEXT, north_city).click()
                    sleep(3)
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    sleep(3)
                    self.driver.back()
                    sleep(2)
                self.driver.back()

            elif city == "سایر شهرها":
                other_cities = ["آذربایجان شرقی", "آذربایجان غربی", "اردبیل", "البرز", "ایلام", "بوشهر", "تهران",
                                "اصفهان", "چهارمحال و بختیاری",
                                "خراسان جنوبی", "خراسان رضوی", "خراسان شمالی", "خوزستان", "زنجان", "سمنان",
                                "سیستان بلوچستان", "فارس", "قزوین",
                                "قم", "کردستان", "کرمان", "کرمانشاه", "کهکیلویه و بویراحمد", "گلستان", "گیلان",
                                "لرستان", "مازندان", "مرکزی",
                                "هرمزگان", "همدان", "یزد"]

                east_azarbaijan_cities = ["اهر","تبریز","جلفا","شبستر","مراغه","مرند","میانه" , "سایر شهرهای استان آذربایجان شرقی"]
                west_azarbaijan_cities = ["ارومیه","مهاباد","خوی","پیرانشهر","میاندوآب","بوکان","سایر شهرهای استان آذربایجان غربی"]
                ardebil = ["اردبیل","خلخال","سرعین","مشکین شهر","سایر شهرهای استان اردبیل"]
                esfahan = ["اصفهان","شاهین شهر","بهارستان","خوانسار","کاشان","گلپایگان","نجف آباد","نطنز","فولادشهر","سایر شهرهای استان اصفهان"]
                alborz = ["هشتگرد","کرج","محمد شهر","ماهدشت","نظر آباد","مشکین دشت","شهرجدید هشتگرد","کردان","فردیس","کمالشهر","سایر شهرهای استان البرز"]
                ilam = ["ایلام","دره شهر","مهران","دهلران","سایر شهرهای استان ایلام"]
                booshehr = ["بوشهر","برازجان","بندر دیلم","بندر گناوه","عسلویه","سایر شهرهای  استان بوشهر"]
                tehran = ["تهران","اسلامشهر","اندیشه","پردیس","پرند","دماوند","رباط کریم","شهریار","لواسانات","ورامین","سایر شهرهای استان تهران"]
                chaharmahar = ["شهرکرد","بروجن","سامان","سایر شهرهای استان چهار محال بختیاری"]
                south_khorasan = ["بیرجند","قاین","طبس","نهبندان","سایر شهرهای استان خراسان جنوبی"]
                khorasan_razavi = ["مشهد","تربیت حیدریه","سبزوار","قوچان","گناباد","نیشابور","سایر شهرهای استان خراسان رضوی"]
                north_khorasan = ["بجنورد","اسفراین","شیروان","سایر شهرهای استان خراسان شمالی"]
                khuzestan = ["اهواز","آبادان","بندر ماهشهر","خرمشهر","دزفول","سایر شهرهای استان خوزستان"]
                zanjan = ["زنجان","ابهر","خرم دره","جورزق","سایر شهرهای استان زنجان"]
                semnan = ["سمنان","دامغان","شاهرود","گرمسار","سایر شهرهای استان سمنان"]
                sistan = ["زاهدان","چابهار","زابل","سایر شهرهای استان سیستان و بلوچستان"]
                fars = ["شیراز","آباده","جهرم","داراب","کازرون","صدرا","سایر شهرهای استان فارس"]
                qazvin = ["قزوین","آبیک","اقبالیه","بوئین زهرا","تاکستان","شهرک محمدیه","سایر شهرهای استان قزوین"]
                qom = ["سلفچگان","پردیسان","قم","سایر شهرهای استان قم"]
                kordestan = ["سنندج","بانه","بیجار","سقز","مریوان","سایر شهرهای استان کردستان"]
                kerman = ["کرمان","بم","جیرفت","رفسنجان","سیرجان","سایر شهرهای استان کرمان"]
                kermanshah=["کرمانشاه","بیستون","سنقر","قصرشیرین","هرسین","صحنه","سایر شهرهای استان کرمانشاه"]
                kohkiluye=["یاسوج","گچساران","سایر شهرهای استان کهکلویه و بویر احمد"]
                golestan = ["گرگان","بندرترکمن","گنبد کاووس","آزادشهر","کردکوی","مینودشت","سایر شهرهای استان گلستان"]
                yazd = ["یزد","اردکان","مهریز","میبد","سایر شهرهای استان یزد"]
                hamedan = ["همدان","ازندریان","تویسرکان","سامن","ملایر","نهاوند","سایر شهرهای استان همدان"]
                hormozgan = ["کیش","بندرعباس","قشم","میناب","سایر شهرهای استان هرمزگان"]
                markazi = ["اراک","آشتیان","تفرش","ساوه","سایر شهرهای استان مرکزی"]
                lorestan = ["خرم آباد","بروجرد","دورود","سایر شهرهای استان لرستان"]
                gilan = ["آستارا","رشت","رودبار","لاهیجان","لوشان","ماسوله","منجیل","فومن","چابکسر","کلاچای","رودسر","چاف وچمخاله","کیاشهر"
                    ,"زیباکنار","انزلی","آستانه","لنگرود","کوچصفهان","خمام","لشت نشا","سایر شهرهای استان گیلان"]
                mazandran = ["آمل","ساری","بابل","قائم شهر","کلاردشت","نکا","بابلسر","فریدون کنار","سرخرود","محمودآباد","ایزدشهر","نور",
                             "رویان","نوشهر","چالوس","کلارآباد","سلمانشهر","عباس","نشتارود","تنکابن","کتالم و سادات شهر","رامسر","چمستان","امیرکلا","سایر شهرهای استان مازندران"]

                for other_city in other_cities:
                    element = self.driver.find_element(By.LINK_TEXT, other_city).click()
                    sleep(3)
                    if other_city == "آذربایجان شرقی":
                        for east_azarbaijan_city in east_azarbaijan_cities:
                            element = self.driver.find_element(By.LINK_TEXT, east_azarbaijan_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()

                    if other_city == "آذربایجان غربی":
                        for west_azarbaijan_cities_city in west_azarbaijan_cities:
                            element = self.driver.find_element(By.LINK_TEXT, west_azarbaijan_cities_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "اردبیل":
                        for ardebil_city in ardebil:
                            element = self.driver.find_element(By.LINK_TEXT, ardebil_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()

                    if other_city == "البرز":
                        for alborz_city in alborz:
                            element = self.driver.find_element(By.LINK_TEXT, alborz_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "ایلام":
                        for ilam_city in ilam:
                            element = self.driver.find_element(By.LINK_TEXT, ilam_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "بوشهر":
                        for booshehr_city in booshehr:
                            element = self.driver.find_element(By.LINK_TEXT, booshehr_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "تهران":
                        for tehran_city in tehran:
                            element = self.driver.find_element(By.LINK_TEXT, tehran_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "اصفهان":
                        for esfahan_city in esfahan:
                            element = self.driver.find_element(By.LINK_TEXT, esfahan_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "چهارمحال و بختیاری":
                        for chaharmahar_city in chaharmahar:
                            element = self.driver.find_element(By.LINK_TEXT, chaharmahar_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "خراسان جنوبی":
                        for south_khorasan_city in south_khorasan:
                            element = self.driver.find_element(By.LINK_TEXT, south_khorasan_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "خراسان رضوی":
                        for khorasan_razavi_city in khorasan_razavi:
                            element = self.driver.find_element(By.LINK_TEXT, khorasan_razavi_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "خراسان شمالی":
                        for north_khorasan_city in north_khorasan:
                            element = self.driver.find_element(By.LINK_TEXT, north_khorasan_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "خوزستان":
                        for khuzestan_city in khuzestan:
                            element = self.driver.find_element(By.LINK_TEXT, khuzestan_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "زنجان":
                        for zanjan_city in zanjan:
                            element = self.driver.find_element(By.LINK_TEXT, zanjan_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "سمنان":
                        for semnan_city in semnan:
                            element = self.driver.find_element(By.LINK_TEXT, semnan_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "سیستان بلوچستان":
                        for sistan_city in sistan:
                            element = self.driver.find_element(By.LINK_TEXT, sistan_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "فارس":
                        for fars_city in fars:
                            element = self.driver.find_element(By.LINK_TEXT, fars_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "قزوین":
                        for qazvin_city in qazvin:
                            element = self.driver.find_element(By.LINK_TEXT, qazvin_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "قم":
                        for qom_city in qom:
                            element = self.driver.find_element(By.LINK_TEXT, qom_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "کردستان":
                        for kordestan_city in kordestan:
                            element = self.driver.find_element(By.LINK_TEXT, kordestan_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "کرمان":
                        for kerman_city in kerman:
                            element = self.driver.find_element(By.LINK_TEXT, kerman_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "کرمانشاه":
                        for kermanshah_city in kermanshah:
                            element = self.driver.find_element(By.LINK_TEXT, kermanshah_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "کهکیلویه و بویراحمد":
                        for kohkiluye_city in kohkiluye:
                            element = self.driver.find_element(By.LINK_TEXT, kohkiluye_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "گلستان":
                        for golestan_city in golestan:
                            element = self.driver.find_element(By.LINK_TEXT, golestan_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "گیلان":
                        for gilan_city in gilan:
                            element = self.driver.find_element(By.LINK_TEXT, gilan_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "لرستان":
                        for lorestan_city in lorestan:
                            element = self.driver.find_element(By.LINK_TEXT, lorestan_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "مازندان":
                        for mazandran_city in mazandran:
                            element = self.driver.find_element(By.LINK_TEXT, mazandran_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "مرکزی":
                        for markazi_city in markazi:
                            element = self.driver.find_element(By.LINK_TEXT, markazi_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "هرمزگان":
                        for hormozgan_city in hormozgan:
                            element = self.driver.find_element(By.LINK_TEXT, hormozgan_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "همدان":
                        for hamedan_city in hamedan:
                            element = self.driver.find_element(By.LINK_TEXT, hamedan_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()
                    if other_city == "یزد":
                        for yazd_city in yazd:
                            element = self.driver.find_element(By.LINK_TEXT, yazd_city).click()
                            sleep(2)
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            sleep(2)
                            self.driver.back()
                            sleep(2)
                        self.driver.find_element(By.ID, "BackToOtherLocations").click()








            else:

                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(3)

                self.driver.back()
                sleep(2)






