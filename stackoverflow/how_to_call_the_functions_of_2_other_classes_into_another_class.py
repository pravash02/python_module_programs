import numpy as np
from numpy import log10 as log10


def lin2db(lin):
    return 10 * log10(lin)


class ADC():
    n_bit = np.array([2, 3, 4, 6, 8, 10, 12, 14, 16], dtype=np.int64)

    def __init__(self):
        self.n_bit = self.n_bit

    @property
    def snr(self):
        n_bit = self.n_bit
        M = 2 ** n_bit
        snr_lin = M ** 2
        return snr_lin

    @property
    def snr_db(self):
        snr_lin = self.snr
        snr_db = lin2db(snr_lin)
        return snr_db

    @property
    def m(self):
        M = 2 ** ADC.n_bit
        return M


class BSC():
    fs_step = 2.75625e3
    error_probability = np.arange(1e-12, fs_step, 1)
    n_bit = np.array([2, 3, 4, 6, 8, 10, 12, 14, 16], dtype=np.int64)

    def __init__(self):
        error_probability = self.error_probability
        n_bit = self.n_bit

    @property
    def snr_BSC(self):
        n_bit = self.n_bit
        M = 2 ** n_bit
        snr_lin_BSC = 1 / (4 * self.error_probability)
        return snr_lin_BSC

    @property
    def snr_db(self):
        snr_lin_BSC = self.snr_BSC
        snr_db = lin2db(snr_lin_BSC)
        return snr_db


class PCM(ADC, BSC):
    def __init__(self, class_a, class_b):
        super().__init__()
        self.analog_bandwith = 0
        self.class_a_snr = class_a.snr
        self.class_b_snr_BSC = class_b.snr_BSC

    def snr_TOT(self):
        snr_tot = (1 / self.class_a_snr + 1 / self.class_b_snr_BSC) ** (-1)
        return snr_tot

    def Critical_Pe(self):
        P_e = 1 / (4 * (self.m ** 2 - 1))


adc_obj = ADC()
bsc_obj = BSC()
pcm_obj = PCM(adc_obj, bsc_obj)
print(pcm_obj.snr_TOT())
