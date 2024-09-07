import pytest
import os
from payments.pix import Pix

def test_pix_create_payment():
    pix = Pix()
    payment = pix.create_payment("12345678901", 100.0)
    assert payment == "Payment created"