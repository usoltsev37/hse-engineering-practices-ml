"""Pipline module."""
import os

import torch
from model.my_model import Model
from preprocessing.my_dataloader import DataLoader


class Pipeline:
    """Pipeline Model."""

    @staticmethod
    def start(num_epochs, lr):
        """Start method."""
        dataloader = DataLoader(batch_size=16, shuffle=True)
        model = Model()
        model.train(
            train_dl=dataloader.dl_train,
            val_dl=dataloader.dl_val,
            num_epochs=num_epochs,
            lr=lr,
        )
        model.inference(dl=dataloader.dl_test)
        torch.save(model.state_dict(), os.getcwd() + "/cnn_model")


if __name__ == "__main__":
    Pipeline.start(num_epochs=3, lr=0.001)
