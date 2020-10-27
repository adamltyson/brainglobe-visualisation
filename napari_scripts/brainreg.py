import napari


with napari.gui_qt():
    viewer = napari.Viewer()

    # open brainreg results
    viewer.open("/home/adam/Desktop/cellfinder_25um/registration")
    viewer.open(
        "/home/adam/Desktop/cellfinder_25um/figures/heatmap.tiff",
        contrast_limits=[0, 15000],
        colormap="inferno",
        blending="additive",
    )
