from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from django.contrib.auth.models import User
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from website.models import Son, EnAvantStyle
from website.forms import SonForm


class HomePageSeleniumTest(StaticLiveServerTestCase):

    def setUp(self):
        self.son = Son.objects.create(
                        titre='test_titre',
                        resume='resume blabla',
                        realisation='realiser pour test',
                        youtube='https://www.youtube.com/embed/-iNWEwLfkv8',
                        deezer='www.deezer.com',
                        spotify='www.spotify.com',
                        en_avant=True
        )
        self.son2 = Son.objects.create(
                        titre='test_titre_without_en_avant',
                        resume='resume blabla',
                        realisation='realiser pour test',
                        youtube='https://www.youtube.com/embed/-iNWEwLfkv8',
                        deezer='www.deezer.com',
                        spotify='www.spotify.com'
                        )
w        
        self.selenium = webdriver.Chrome(ChromeDriverManager().install())
    
    def tearDown(self):
        self.selenium.quit()
    
    def test_en_avant_song(self):
        selenium = self.selenium
        selenium.get(self.live_server_url)

        iframe = selenium.find_element_by_id('iframe_en_avant')
        self.assertEqual(iframe.get_attribute('src'), self.son.youtube)

        resume_p = selenium.find_element_by_id('p_resume')
        self.assertEqual(resume_p.text, self.son.resume)

        realisation_span = selenium.find_element_by_id('realisation_span')
        self.assertEqual(realisation_span.text, self.son.realisation)

    def test_dernier_song(self):
        selenium = self.selenium
        selenium.get(self.live_server_url)

        dernier_p = selenium.find_element_by_id('dernier_paragraph')
        self.assertEqual(dernier_p.text, self.son2.resume)

        iframe_dernier = selenium.find_element_by_id('iframe_dernier')
        self.assertEqual(iframe_dernier.get_attribute('src'), self.son2.youtube)

        span_dernier_realisation = selenium.find_element_by_id('realisation_span_dernier')
        self.assertEqual(span_dernier_realisation.text, self.son2.realisation)

    def test_styles_en_avant(self):
        selenium = self.selenium
        selenium.get(self.live_server_url)

        span_banniere_titre = selenium.find_element_by_id('en_avant_span')
        self.assertEqual(span_banniere_titre.text, self.styles.banniere_titre)

        span_banniere_titre_color = span_banniere_titre.getCssValue('color')
        self.assertEqual(span_banniere_titre_color, self.styles.banniere_couleur)
        
        resume_p_color = selenium.find_element_by_id('p_resume').getCssValue('color')
        self.assertEqual(resume_p_color, self.styles.couleur_corps)
        