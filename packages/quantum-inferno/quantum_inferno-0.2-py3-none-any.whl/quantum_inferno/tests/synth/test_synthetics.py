import unittest

import numpy as np

import quantum_inferno.synth.synthetics_NEW as synth


class TestSynthetics(unittest.TestCase):
    def test_gabor_grain_frequencies(self):
        center, start, end = synth.gabor_grain_frequencies(3, .01, 100, 1)
        self.assertAlmostEqual(center[0], 0.4, 2)
        self.assertAlmostEqual(center[-1], 0.01, 2)
        self.assertAlmostEqual(start[0], 0.35, 2)
        self.assertAlmostEqual(start[-1], 0.01, 2)
        self.assertAlmostEqual(end[0], 0.45, 2)
        self.assertAlmostEqual(end[-1], 0.01, 2)

    def test_chirp_noise_16bit(self):
        sig = synth.chirp_noise_16bit()
        self.assertTrue(np.min(sig) < -1.0)
        self.assertTrue(np.max(sig) > 1.0)
        self.assertEqual(sig.size, 2**12)

    def test_sawtooth_noise_16bit(self):
        sig = synth.sawtooth_noise_16bit()
        self.assertTrue(np.min(sig) < -1.0)
        self.assertTrue(np.max(sig) > 1.0)
        self.assertEqual(sig.size, 2**12)

    def test_sawtooth_doppler_noise_16bit(self):
        phase = np.array([(n % 5) / 4 * np.pi for n in range(2**12)])
        sig = synth.sawtooth_doppler_noise_16bit(phase)
        self.assertTrue(np.min(sig) < -0.01)
        self.assertTrue(np.max(sig) > 0.01)
        self.assertEqual(sig.size, 2**12)

    def test_chirp_linear_in_noise(self):
        sig, time = synth.chirp_linear_in_noise(8, 800, 3, 0, 0, 1, 1)
        self.assertEqual(sig.size, time.size)
        self.assertEqual(sig.size, 4000)
        self.assertEqual(time[0], 0)
        self.assertEqual(time[-1], 4.99875)

    def test_white_noise_fbits(self):
        sig = synth.white_noise_fbits(np.array(range(100)), 8)
        self.assertEqual(sig.size, 100)

    def test_taper_tukey(self):
        sig = synth.taper_tukey(np.array(range(100)), 0)
        self.assertEqual(sig.size, 100)
        self.assertEqual(sig[0], sig[-1])
        self.assertEqual(sig[50], 1)
        sig = synth.taper_tukey(np.array(range(200)), 1)
        self.assertEqual(sig.size, 200)
        self.assertEqual(sig[0], sig[-1])
        self.assertAlmostEqual(sig[100], 1, 2)
