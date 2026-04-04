import torch
import torchvision.models as models
import torchvision.transforms as transforms
import numpy as np

from PIL import Image


class ResNet50Embedder:

    def __init__(self):

        self.model = models.resnet50(
            weights=models.ResNet50_Weights.DEFAULT
        )

        # remove classification layer
        self.model = torch.nn.Sequential(*list(self.model.children())[:-1])

        self.model.eval()

        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

    def embed(self, image: Image.Image):

        img = self.transform(image).unsqueeze(0)

        with torch.no_grad():
            embedding = self.model(img)

        embedding = embedding.squeeze().numpy()

        return embedding.astype("float32")


# Global embedder instance (avoids reloading model)
embedder = ResNet50Embedder()


def get_embedding(image: Image.Image):

    return embedder.embed(image)