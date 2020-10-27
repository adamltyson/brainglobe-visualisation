import brainrender
from brainrender.scene import Scene

# Show axes in 3D
# brainrender.SHOW_AXES = True

# Swap from the "plastic" shader style to cartoon
# brainrender.SHADER_STYLE = "cartoon"

# Initialise the brainrender scene, default is the ARA
scene = Scene()

# Visualise brain regions, and set opacity.
# Assign to variable to manipulate later
rsp = scene.add_brain_regions("RSP", alpha=0.2)
visp = scene.add_brain_regions("VISp", alpha=0.2)


# load a cellfinder output file, set the color and the opacity
cells = scene.add_cells_from_file(
    "../data/cells/cell-detect-paper-cells.h5",
    color="salmon",
    alpha=0.8,
)

# get data from allen
filepaths, data = scene.atlas.download_streamlines_for_region("RSP")
s = scene.add_streamlines(
    data[3:7], color="steelblue", show_injection_site=False, alpha=0.6,
)


# Add an outline to regions
# scene.add_silhouette(rsp, visp, scene.root)

# Slice the brain in half
# scene.cut_actors_with_plane("frontal")

# Display the region
scene.render()


# scene.render(interactive=False, zoom=1.75)
# scene.take_screenshot()
# scene.close()
