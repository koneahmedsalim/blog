from django.test import TestCase
from ..models import Categorie, Publication, Commentaire, ReponseCommentaire, Video, Like, Evenement, Cours, Textes
from datetime import datetime

class TestModels(TestCase):

    def setUp(self):
        """Initialise les données pour les tests"""
        self.categorie = Categorie.objects.create(
            nom="Catégorie Test",
            description="Description de test",
            status=True
        )
        self.publication = Publication.objects.create(
            titre="Publication Test",
            description="<p>Description riche pour la publication</p>",
            image="image/test.jpg",
            categorie=self.categorie,
            status=True
        )
        self.commentaire = Commentaire.objects.create(
            publication=self.publication,
            nom="Utilisateur Test",
            email="test@example.com",
            commentaire="Ceci est un commentaire test",
            status=True
        )
        self.video = Video.objects.create(
            titre="Vidéo Test",
            description="Description de la vidéo",
            image="video/test.jpg",
            video="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            status=True
        )



    # Tests pour Categorie
    def test_categorie_creation(self):
        self.assertEqual(self.categorie.nom, "Catégorie Test")
        self.assertTrue(self.categorie.status)

    # Tests pour Publication
    def test_publication_slug_generation(self):
        self.assertIsNotNone(self.publication.slug)
        self.assertIn("publication-test", self.publication.slug)

    # Tests pour Commentaire
    def test_commentaire_association(self):
        self.assertEqual(self.commentaire.publication, self.publication)
        self.assertEqual(self.commentaire.nom, "Utilisateur Test")

    # Tests pour Video
    def test_video_get_video(self):
        video_id = self.video.get_video
        self.assertEqual(video_id, "dQw4w9WgXcQ")

    # Tests pour Like
    def test_like_creation(self):
        like = Like.objects.create(publication=self.publication)
        self.assertEqual(like.publication, self.publication)
        self.assertTrue(like.status)

    # Tests pour Evenement
    def test_evenement_creation(self):
        evenement = Evenement.objects.create(
            titre="Événement Test",
            description="Description de l'événement",
            image="evenement/test.jpg",
            status=True
        )
        self.assertEqual(evenement.titre, "Événement Test")
        self.assertIsNotNone(evenement.slug)

    # Tests pour Cours
    def test_cours_creation(self):
        cours = Cours.objects.create(
            titre="Cours de Test",
            niveau="Niveau Test",
            annee=2024,
            description="Description du cours",
            image="cours/test.jpg",
            cours="cours/test.pdf",
            status=True
        )
        self.assertEqual(cours.titre, "Cours de Test")
        self.assertTrue(cours.status)
        self.assertIsNotNone(cours.cours)

    # Tests pour Textes
    def test_textes_creation(self):
        texte = Textes.objects.create(
            titre="Texte de Test",
            description="Description du texte",
            image="textes/test.jpg",
            pdf="pdf/textes/test.pdf",
            status=True
        )
        self.assertEqual(texte.titre, "Texte de Test")
        self.assertTrue(texte.status)
        self.assertIsNotNone(texte.pdf)

