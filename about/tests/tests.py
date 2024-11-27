from django.test import TestCase
from about.models import Curriculum, Contact, Prestation, Presentation, Gallerie


class TestModels(TestCase):

    def setUp(self):
        """Initialise les données pour les tests"""
        self.curriculum = Curriculum.objects.create(
            photo="images/curriculum/photo.jpg",
            nom="Curriculum Test",
            description="<p>Description pour le curriculum</p>",
            cv="cv/curriculum/test_cv.pdf",
            status=True
        )

        self.contact = Contact.objects.create(
            nom="Contact Test",
            email="contact@test.com",
            subject="Sujet Test",
            telephone=123456789,
            message="Ceci est un message de test",
            status=True
        )

        self.prestation = Prestation.objects.create(
            titre="Prestation Test",
            description="Description de la prestation",
            image="images/prestations/prestation.jpg",
            status=True
        )

        self.presentation = Presentation.objects.create(
            titre="Présentation Test",
            image="image/presentation/presentation.jpg",
            description="<p>Description riche pour la présentation</p>",
            status=True
        )

        self.gallerie = Gallerie.objects.create(
            gallerie="gallerie/image/test.jpg",
            titre="Gallerie Test",
            status=True
        )

    # Tests pour Curriculum
    def test_curriculum_creation(self):
        self.assertEqual(self.curriculum.nom, "Curriculum Test")
        self.assertEqual(self.curriculum.cv, "cv/curriculum/test_cv.pdf")
        self.assertTrue(self.curriculum.status)

    # Tests pour Contact
    def test_contact_creation(self):
        self.assertEqual(self.contact.nom, "Contact Test")
        self.assertEqual(self.contact.email, "contact@test.com")
        self.assertEqual(self.contact.subject, "Sujet Test")
        self.assertEqual(self.contact.telephone, 123456789)
        self.assertTrue(self.contact.status)

    # Tests pour Prestation
    def test_prestation_creation(self):
        self.assertEqual(self.prestation.titre, "Prestation Test")
        self.assertEqual(self.prestation.description, "Description de la prestation")
        self.assertTrue(self.prestation.status)

    # Tests pour Presentation
    def test_presentation_creation(self):
        self.assertEqual(self.presentation.titre, "Présentation Test")
        self.assertEqual(self.presentation.image, "image/presentation/presentation.jpg")
        self.assertTrue(self.presentation.status)

    # Tests pour Gallerie
    def test_gallerie_creation(self):
        self.assertEqual(self.gallerie.titre, "Gallerie Test")
        self.assertEqual(self.gallerie.gallerie, "gallerie/image/test.jpg")
        self.assertTrue(self.gallerie.status)
