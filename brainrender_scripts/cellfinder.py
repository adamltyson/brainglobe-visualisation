import brainrender
from brainrender.scene import Scene

brainrender.SHADER_STYLE = "cartoon"

cam = {
    "position": (-6487.273965131618, -5550.562514137312, 28272.495556587404),
    "focal": (6537.351933588274, 3412.5802771013628, -5709.021459594369),
    "viewup": (0.09260324765660453, -0.9709559490391483, -0.2206109325236095),
    "distance": 37479.62522783266,
    "clipping": (20229.508010577032, 59284.37187623414),
    "orientation": (
        -13.836205590080267,
        20.971108505105253,
        179.56951672841427,
    ),
}

cam2 = {
    "position": (-1699.2344629010634, -2206.284920856014, 30457.550826086375),
    "focal": (6537.351149583963, 3392.5641359001806, -5709.023027613759),
    "viewup": (0.04809531342854623, -0.9886828825007732, -0.1421020713296328),
    "distance": 37512.79138676941,
    "clipping": (22041.130361549902, 57078.9081037701),
    "orientation": (
        -8.583565787826364,
        12.829736466025748,
        179.12103892366972,
    ),
}

scene = Scene(
    camera=cam, display_inset=False, screenshot_kwargs={"folder": "figures"},
)

import pandas as pd
pd.read_hdf("../data/cell-detect-paper-cells.h5")
cells = scene.add_cells_from_file(
    "../data/cell-detect-paper-cells.h5", color="salmon", alpha=0.8
)

r = scene.add_brain_regions("RSP", alpha=0.2)
t = scene.add_brain_regions("TH", alpha=0.2, color=[0.2, 0.2, 0.2])


filepaths, data = scene.atlas.download_streamlines_for_region("RSP")
s = scene.add_streamlines(
    data[3:7], color="steelblue", show_injection_site=False, alpha=0.6,
)

# for stream in s:
#     stream.mesh.mirror("z").addPos(dp_x=(0, 0, 11250))

scene.add_silhouette(r, t, scene.root)
# scene.add_silhouette(cells, lw=0.1)
scene.render()
# scene.render(interactive=False, zoom=1.75)
# scene.take_screenshot(screenshot_name="cellfinder_cells")
#
# scene.render(interactive=False, camera=cam2, zoom=1.3)
# scene.take_screenshot(screenshot_name="cellfinder_cells_2")
#
# scene.cut_actors_with_plane("frontal")
# scene.add_silhouette(r, t, scene.root)
#
# scene.render(interactive=False, camera="coronal", zoom=1.5)
# scene.take_screenshot(screenshot_name="cellfinder_cells_3")
# scene.close()
