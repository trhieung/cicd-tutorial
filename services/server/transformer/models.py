from django.db import models

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.
class HuggingFaceModel(models.Model):
    pub_path = models.CharField(max_length=200)
    upd_date = models.DateTimeField("date updated")

    def __str__(self):
        return self.pub_path

class ModelInfor(models.Model):
    model_path = models.ForeignKey(HuggingFaceModel, on_delete=models.CASCADE)
    
    train_los = models.DecimalField(max_digits=15, decimal_places=12)
    train_acc = models.DecimalField(max_digits=15, decimal_places=12)

    val_los = models.DecimalField(max_digits=15, decimal_places=12)
    val_acc = models.DecimalField(max_digits=15, decimal_places=12)

    test_los = models.DecimalField(max_digits=15, decimal_places=12)
    test_acc = models.DecimalField(max_digits=15, decimal_places=12)

    def __str__(self):
        return self.test_acc
    
class AmazonLabels(models.Model):
    """
    {
        "label"=1,
        "cat_name"="haha",
    }
    """

    label = models.IntegerField(default=0)
    cat_name = models.CharField(max_length=64)
    svg_str = models.CharField(max_length=300, default="nothing")
    
    owner = models.ForeignKey('auth.User', related_name='amazonlabels', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def __str__(self):
        return str(self.label)
    
    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """

        # Assuming you want to highlight some code, not label which is an integer
        code_to_highlight = self.cat_name  # Replace this with the actual code/text to highlight
        lexer = get_lexer_by_name('python')  # Assuming Python syntax for highlighting
        formatter = HtmlFormatter(style='friendly', linenos=True, full=True)
        self.highlighted = highlight(code_to_highlight, lexer, formatter)
        super().save(*args, **kwargs)
    
class AmazonProductReviews(models.Model):
    label = models.ForeignKey(AmazonLabels, on_delete=models.CASCADE)
    reviewText = models.CharField(max_length=1500)

    def __str__(self):
        return self.reviewText

