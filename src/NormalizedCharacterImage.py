from copy import deepcopy
from GrayscaleImage import GrayscaleImage
from GaussianFilter import GaussianFilter

class NormalizedCharacterImage(GrayscaleImage):

    def __init__(self, image=None, data=None, height=None, blur=1.1):
        if image != None:
            GrayscaleImage.__init__(self, data=deepcopy(image.data))
        elif data != None:
            GrayscaleImage.__init__(self, data=deepcopy(data))

        self.blur = blur
        self.gaussian_filter()

        #self.increase_contrast()

        self.height = height
        self.resize()

#    def increase_contrast(self):
#        """Increase the contrast by performing a grayscale mapping from the 
#        current maximum and minimum to a range between 0 and 1."""
#        self.data -= self.data.min()
#        self.data = self.data.astype(float) / self.data.max()

    def gaussian_filter(self):
        GaussianFilter(self.blur).filter(self)

    def resize(self):
        """Resize the image to a fixed height."""
        if self.height == None:
            return

        h, w = self.data.shape
        GrayscaleImage.resize(self, (self.height, self.height * w / h))
