from django.db import models

# Create your models here.
class Wordtypes(models.Model):
    types = models.CharField(max_length=200,primary_key=True)
    def __str__(self):
        return self.types

class Wordsense(models.Model):
    word = models.CharField(max_length=200,primary_key=True)
    word_id = models.CharField(max_length=200)
    def __str__(self):             
        return self.word

    
class Meanings(models.Model):
    meaning= models.CharField(max_length=200)
    word_id1 = models.ForeignKey(Wordsense)
    wortype = models.ForeignKey(Wordtypes)
    def __str__(self):              
        return str(self.meaning)

class Examples(models.Model):
    example = models.CharField(max_length=200)
    wordsense = models.ForeignKey(Wordsense)
    wordtype = models.ForeignKey(Wordtypes)
    def __str__(self):
            return self.example

        
class Relate(models.Model):
    word_id2 = models.ForeignKey(Wordsense,null=True)
    derived=models.CharField(max_length=200)
    def __str__(self):            
        return self.derived

class Synonym(models.Model):
    word_id3 = models.ForeignKey(Wordsense,default='abc')
    synon = models.CharField(max_length=100)
    def __str__(self):
        return self.synon


class Hypernym(models.Model):
    word_id4=models.ForeignKey(Wordsense,default='xyz')
    hyper=models.CharField(max_length=200)
    def __str__(self):
        return self.hyper
    
