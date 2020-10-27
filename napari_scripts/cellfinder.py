import napari


with napari.gui_qt():
    viewer = napari.Viewer()

    # open raw data
    viewer.open("/home/adam/Desktop/ch00")

    # open cellfinder results
    viewer.open("/home/adam/Desktop/cellfinder_25um")
