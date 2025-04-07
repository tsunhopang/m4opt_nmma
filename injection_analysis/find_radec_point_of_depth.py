from astropy.io import fits
import numpy as np
import healpy as hp

def find_closest_limitmag_coords(fits_file, target_value):
    """
    Find the RA, Dec coordinates where the limiting magnitude 
    is closest to the specified target value.
    
    Parameters:
    -----------
    fits_file : str
        Path to the FITS file containing the HEALPix map
    target_value : float
        The target limiting magnitude value to find
        
    Returns:
    --------
    tuple
        (ra, dec, actual_value) in degrees and magnitudes
    """
    # Open the FITS file
    hdul = fits.open(fits_file)
    
    # Get the BinTableHDU containing the HEALPix data
    bintable = hdul[1]  # Assuming it's the first extension
    
    # Extract and flatten the LIMMAG data
    limmag_data = bintable.data['LIMMAG']
    limmag_map = limmag_data.flatten()
    
    # Get NSIDE from the header
    nside = bintable.header['NSIDE']
    
    # Calculate the difference between each value and the target
    diff = np.abs(limmag_map - target_value)
    
    # Find the index of the minimum difference
    closest_idx = np.argmin(diff)
    closest_value = limmag_map[closest_idx]
    
    # Convert the pixel index back to sky coordinates (RA, Dec)
    # Using nested ordering as specified in your header
    theta, phi = hp.pix2ang(nside, closest_idx, nest=True)
    
    # Convert from HEALPix angular coordinates to RA, Dec
    ra = np.degrees(phi)
    dec = 90.0 - np.degrees(theta)  # Convert co-latitude to declination
    
    # Close the file
    hdul.close()
    
    return ra, dec, closest_value
