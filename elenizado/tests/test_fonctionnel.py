from django.test import TestCase, Client
from django.urls import reverse
from website.models import SiteInfo, Publication, Evenement, Commentaire, ReponseCommentaire
from about.models import Gallerie
from tinymce.models import HTMLField


class TimelineViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.site_info = SiteInfo.objects.create(
            email="test@example.com",
            nom="Site Test",
            telephone=123456789,
            description="Description du site",
            logo="logo.png",
            status=True,
        )
        for i in range(10):
            Publication.objects.create(
                titre=f"Publication {i+1}",
                slug=f"publication-{i+1}",
                contenu="Contenu de la publication",
                status=True,
            )

    def test_timeline_view_status_code(self):
        response = self.client.get(reverse('timeline'))  # Remplacez 'timeline' par votre nom d'URL
        self.assertEqual(response.status_code, 200)

    def test_timeline_pagination(self):
        response = self.client.get(reverse('timeline') + '?page=1')
        self.assertContains(response, "Publication 1")
        self.assertContains(response, "Publication 4")


class DetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.site_info = SiteInfo.objects.create(
            email="test@example.com",
            nom="Site Test",
            telephone=123456789,
            description="Description du site",
            logo="logo.png",
            status=True,
        )
        self.publication = Publication.objects.create(
            titre="Publication Test",
            slug="publication-test",
            contenu="Contenu de la publication",
            status=True,
        )

    def test_detail_view_status_code(self):
        response = self.client.get(reverse('detail', kwargs={'slug': self.publication.slug}))
        self.assertEqual(response.status_code, 200)

    def test_detail_view_content(self):
        response = self.client.get(reverse('detail', kwargs={'slug': self.publication.slug}))
        self.assertContains(response, "Publication Test")
        self.assertContains(response, "Contenu de la publication")


class CommentaireViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.publication = Publication.objects.create(
            titre="Publication Comment",
            slug="publication-comment",
            contenu="Contenu avec commentaires",
            status=True,
        )

    def test_ajout_commentaire(self):
        response = self.client.post(
            reverse('is_commentaire'),  # Remplacez 'is_commentaire' par votre nom d'URL
            {
                'id': self.publication.id,
                'nom': 'Utilisateur Test',
                'email': 'test@comment.com',
                'commentaire': 'Ceci est un commentaire.',
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("success", response.json())
        self.assertTrue(response.json()["success"])


class EvenementViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.site_info = SiteInfo.objects.create(
            email="test@example.com",
            nom="Site Test",
            telephone=123456789,
            description="Description du site",
            logo="logo.png",
            status=True,
        )
        for i in range(5):
            Evenement.objects.create(
                titre=f"Evenement {i+1}",
                slug=f"evenement-{i+1}",
                description="Description de l'événement",
                status=True,
            )

    def test_evenement_view_status_code(self):
        response = self.client.get(reverse('evenement'))  # Remplacez 'evenement' par votre nom d'URL
        self.assertEqual(response.status_code, 200)

    def test_evenement_pagination(self):
        response = self.client.get(reverse('evenement') + '?page=1')
        self.assertContains(response, "Evenement 1")
        self.assertContains(response, "Evenement 4")


class VideoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.site_info = SiteInfo.objects.create(
            email="test@example.com",
            nom="Site Test",
            telephone=123456789,
            description="Description du site",
            logo="logo.png",
            status=True,
        )

    def test_video_view_status_code(self):
        response = self.client.get(reverse('video'))  # Remplacez 'video' par votre nom d'URL
        self.assertEqual(response.status_code, 200)
