## Script to add two half maps and save the result as a mrc file if the output filename is specified

def average_half_maps(halfmap_1_path, halfmap_2_path, output_filename, return_map=False, fsc_filter=True):
    '''
    Function to add two half maps

    Parameters
    ----------
    halfmap_1_path : str 
        Path to halfmap 1
        
    halfmap_2_path : str 
        Path to halfmap 2
        

    Returns
    -------
    output_filename : str
        Path to output file
    


    '''
    from emmer.ndimage.map_utils import save_as_mrc, load_map
    from emmer.ndimage.filter.apply_fsc_filter import apply_fsc_filter
    halfmap1, apix = load_map(halfmap_1_path)
    halfmap2, _ = load_map(halfmap_2_path)
    
    assert halfmap1.shape == halfmap2.shape
    
    full_map = (halfmap1 + halfmap2) / 2

    # Apply FSC filter if specified
    if fsc_filter:
        full_map = apply_fsc_filter(full_map, apix, halfmap_1=halfmap1, halfmap_2=halfmap2)

    if output_filename is not None:
        save_as_mrc(full_map, output_filename, apix, verbose=True)
    
    if return_map:
        return full_map
    else:   
        return output_filename
    
