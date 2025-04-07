from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import healpy as hp

# Open the FITS file
hdul = fits.open('./test.fits.gz')

# Access the BinTableHDU
bintable = hdul[1]  # Assuming it's the first extension

# Extract the LIMMAG data
# Based on your header, LIMMAG is stored as 1024D arrays, 192 of them
# We need to reshape this properly
limmag_data = bintable.data['LIMMAG']

# Since NSIDE=128, the total number of pixels should be 12*NSIDE²=196608
# Let's reshape and flatten the data properly
limmag_map = limmag_data.flatten()

# Verify the length matches what we expect from the header
# The header says LASTPIX=196607 (0-based, so actual count is 196608)
print(f"Map length: {len(limmag_map)}, Expected: {12*128*128}")

# Plot the HEALPix map
plt.figure(figsize=(10, 8))
hp.mollview(
    limmag_map, 
    title="Limiting Magnitude Sky Map", 
    unit="mag",
    coord=['C'],  # Celestial/Equatorial coordinates (as per COORDSYS='C')
    nest=True     # Important: use nested ordering as specified in the header
)
hp.graticule()
plt.show()

# To convert to a different coordinate system (e.g., from Equatorial to Galactic)
limmag_map_gal = hp.rotator.Rotator(coord=['C', 'G'])(limmag_map)
plt.figure(figsize=(10, 8))
hp.mollview(
    limmag_map_gal,
    title="Limiting Magnitude (Galactic Coordinates)",
    unit="mag",
    coord=['G'],
    nest=True
)
hp.graticule()
plt.show()

# Close the file
hdul.close()
