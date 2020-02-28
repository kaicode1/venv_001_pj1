from fastai.datasets import untar_data, URLs
from fastai.metrics import accuracy
from fastai.vision import ImageDataBunch, cnn_learner, models
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

path = untar_data(URLs.MNIST_TINY)
print(path)
data = ImageDataBunch.from_folder(path)

#learn = cnn_learner(data, models.resnet18, metrics=accuracy)
#learn.fit(3)

'''
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1076)


'''