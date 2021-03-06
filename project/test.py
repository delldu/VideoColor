"""Model test."""
# coding=utf-8
#
# /************************************************************************************
# ***
# ***    Copyright Dell 2020, All Rights Reserved.
# ***
# ***    File Author: Dell, 2020年 11月 02日 星期一 17:52:14 CST
# ***
# ************************************************************************************/
#
import argparse
import os

import torch

from data import get_data
from model import enable_amp, get_model, model_device, model_load, valid_epoch

if __name__ == "__main__":
    """Test model."""

    parser = argparse.ArgumentParser()
    parser.add_argument('--checkpoint', type=str,
                        default="models/VideoColor.pth", help="checkpoint file")
    parser.add_argument('--bs', type=int, default=2, help="batch size")
    args = parser.parse_args()

    # get model
    model_r = get_model("modelR")
    model_load(model_r, "modelR", args.checkpoint)
    device = model_device()
    model_r.to(device)

    model_c = get_model("modelC")
    model_load(model_c, "modelC", args.checkpoint)
    model_c.to(device)

    enable_amp(model_r)
    enable_amp(model_c)

    print("Start testing ...")
    test_dl = get_data(trainning=False, bs=args.bs)
    valid_epoch(test_dl, model_r, device, tag='test')
