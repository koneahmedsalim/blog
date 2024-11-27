from django.test import TestCase
from website.models import SiteInfo, SocialCount, Newsletter

class TestSiteInfoModel(TestCase):

    def setUp(self):
        """Initialisation des données pour SiteInfo"""
        self.site_info = SiteInfo.objects.create(
            email="test@example.com",
            nom="Nom du site",
            telephone=123456789,
            description="Description du site",
            logo="logo/site/logo.png",
            status=True
        )

    def test_site_info_creation(self):
        """Test de la création d'un objet SiteInfo"""
        self.assertEqual(self.site_info.email, "test@example.com")
        self.assertEqual(self.site_info.nom, "Nom du site")
        self.assertEqual(self.site_info.telephone, 123456789)
        self.assertTrue(self.site_info.status)

    def test_site_info_string_representation(self):
        """Test de la méthode __str__"""
        self.assertEqual(str(self.site_info), "Nom du site")


class TestSocialCountModel(TestCase):

    def setUp(self):
        """Initialisation des données pour SocialCount"""
        self.social_count = SocialCount.objects.create(
            nom="Facebook",
            lien="https://facebook.com",
            icones="facebook",
            status=True
        )

    def test_social_count_creation(self):
        """Test de la création d'un objet SocialCount"""
        self.assertEqual(self.social_count.nom, "Facebook")
        self.assertEqual(self.social_count.lien, "https://facebook.com")
        self.assertEqual(self.social_count.icones, "facebook")
        self.assertTrue(self.social_count.status)

    def test_social_count_string_representation(self):
        """Test de la méthode __str__"""
        self.assertEqual(str(self.social_count), "Facebook")


class TestNewsletterModel(TestCase):

    def setUp(self):
        """Initialisation des données pour Newsletter"""
        self.newsletter = Newsletter.objects.create(
            email="newsletter@example.com",
            status=True
        )

    def test_newsletter_creation(self):
        """Test de la création d'un objet Newsletter"""
        self.assertEqual(self.newsletter.email, "newsletter@example.com")
        self.assertTrue(self.newsletter.status)

    def test_newsletter_string_representation(self):
        """Test de la méthode __str__"""
        self.assertEqual(str(self.newsletter), "newsletter@example.com")
