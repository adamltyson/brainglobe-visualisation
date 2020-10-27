from brainrender.scene import Scene
from brainrender.animation.video import BasicVideoMaker as VideoMaker

scene = Scene()

rsp = scene.add_brain_regions("RSP", alpha=0.2)
visp = scene.add_brain_regions("VISp", alpha=0.2)


# load a cellfinder output file, set the color and the opacity
cells = scene.add_cells_from_file(
    "../data/cells/cell-detect-paper-cells.h5",
    color="salmon",
    alpha=0.8,
)

# Create an instance of VideoMaker with our scene
vm = VideoMaker(scene, niters=60)

# specify how the scene rotates at each frame
vm.make_video(azimuth=6)
