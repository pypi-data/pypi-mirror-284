import rmsd
import numpy

def rmsd_ref(coords,ref):
    """
    Calculate the rmsd of coords to ref, and rotate coords to minimize rmsd.
    """

    frames, atoms, _ = coords.shape
    if(ref.shape != coords[0].shape):
        raise ValueError("The shape of ref and coords should be the same.")
    
    # main loop
    for i in range(frames):
        # recenter
        coords[i] -= numpy.mean(coords[i], axis=0)

        # calculate the rotation matrix
        R = rmsd.kabsch(coords[i], ref)
        # rotate the coords
        coords[i] = numpy.dot(coords[i], R)

    return coords