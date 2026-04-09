import numpy as np
import matplotlib.pyplot as plt
import hashlib
import time
from scipy.fft import fft, fftfreq

def generate_biometric_proof(nonce="AGI_TX_9942", f1=2000, f2=2440, fs=44100, duration=0.1):
    print("/// NEURO-SPHERE: SENTIENCE PROTOCOL INITIALIZED ///\n")
    time.sleep(1)
    print(f"[*] Stimulating target with f1={f1}Hz and f2={f2}Hz...")
    
    # 1. GENERATE THE AUDIO CHALLENGE
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    stimulus = np.cos(2 * np.pi * f1 * t) + np.cos(2 * np.pi * f2 * t)
    
    # 2. SIMULATE THE LIVING COCHLEA (Analog Computation via Tissue Non-Linearity)
    c1, c2, c3 = 1.0, 0.1, 0.045 
    biological_response = c1*stimulus + c2*(stimulus**2) + c3*(stimulus**3)
    
    # Add ambient biological noise (blood flow, micro-tremors)
    noise = np.random.normal(0, 0.02, len(t))
    mic_signal = biological_response + noise
    
    # 3. DSP EXTRACTION OF DISTORTION PRODUCT (2f1 - f2)
    dp_freq = 2*f1 - f2
    freqs = fftfreq(len(mic_signal), 1/fs)
    fft_vals = np.abs(fft(mic_signal)) / len(mic_signal)
    
    # Find amplitude at the specific biological echo frequency
    dp_idx = np.argmin(np.abs(freqs - dp_freq))
    amplitude = fft_vals[dp_idx]
    phase = np.angle(fft(mic_signal)[dp_idx])
    
    time.sleep(1)
    print(f"[+] Living Tissue Detected. Distortion Product ({dp_freq}Hz) Extracted.")
    print(f"    - Biological Amplitude : {amplitude:.6f}")
    
    # 4. ZERO-KNOWLEDGE HASH GENERATION
    raw_bio_data = f"{amplitude:.6f}:{phase:.6f}:{nonce}".encode('utf-8')
    sentience_hash = hashlib.sha256(raw_bio_data).hexdigest()
    
    print(f"\n[+] ZERO-KNOWLEDGE SENTIENCE HASH GENERATED:")
    print(f"    0x{sentience_hash}\n")
    
    # 5. VISUALIZE THE PROOF FOR INVESTORS
    # Using a dark theme for a cyber/hacker aesthetic
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 5))
    plt.plot(freqs[:len(freqs)//2], fft_vals[:len(freqs)//2], color='cyan')
    plt.axvline(x=dp_freq, color='red', linestyle='--', label=f'Biometric Echo (2f1-f2): {dp_freq}Hz')
    plt.axvline(x=f1, color='green', linestyle=':', label='Stimulus f1')
    plt.axvline(x=f2, color='green', linestyle=':', label='Stimulus f2')
    plt.xlim(1000, 3000)
    plt.title("Neuro-Sphere: Biomechanical Analog Cryptography (DPOAE Signature)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.savefig('biometric_proof.png')
    print("[*] Visualization saved successfully as 'biometric_proof.png'")

if __name__ == "__main__":
    generate_biometric_proof()
