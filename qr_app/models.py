from django.db import models
import qrcode
# Create your models here.

from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class QR(models.Model):
    name = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to='qr_codes',blank=True)



    def __str__(self):
        return str(self.name)
    

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB',(300,300),'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)


        frame = f'qr_code-{self.name}'+'.png'

        buffer = BytesIO()
        canvas.save(buffer,'PNG')

        self.qr_code.save(frame,File(buffer), save=False)

        canvas.close()
        super().save(*args,**kwargs)