import brainrender
from brainrender.scene import Scene

# Show axes in 3D
# brainrender.SHOW_AXES = True

# Swap from the "plastic" shader style to cartoon
# brainrender.SHADER_STYLE = "cartoon"


PROBE_RADIUS = 40
PROBE_ALPHA = 0.2
# Initialise the brainrender scene, default is the ARA
scene = Scene()

# Visualise brain regions, and set opacity.
# Assign to variable to manipulate later
rsp = scene.add_brain_regions("RSP", alpha=0.2)
visp = scene.add_brain_regions("VISp", alpha=0.2)


# load probe tracks from brainreg_segment
cells = scene.add_cells_from_file(
    "../data/probes/track_1.h5",
    color="green",
    alpha=PROBE_ALPHA,
    radius=PROBE_RADIUS,
)
cells = scene.add_cells_from_file(
    "../data/probes/track_2.h5",
    color="cyan",
    alpha=PROBE_ALPHA,
    radius=PROBE_RADIUS,
)
cells = scene.add_cells_from_file(
    "../data/probes/track_3.h5",
    color="blue",
    alpha=PROBE_ALPHA,
    radius=PROBE_RADIUS,
)
cells = scene.add_cells_from_file(
    "../data/probes/track_4.h5",
    color="red",
    alpha=PROBE_ALPHA,
    radius=PROBE_RADIUS,
)
cells = scene.add_cells_from_file(
    "../data/probes/track_5.h5",
    color="salmon",
    alpha=PROBE_ALPHA,
    radius=PROBE_RADIUS,
)


# Add an outline to regions
# scene.add_silhouette(rsp, visp, scene.root)


# Display the region
scene.render()
