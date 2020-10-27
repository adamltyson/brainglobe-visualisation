from brainrender.scene import Scene


# Initialise the brainrender scene, default is the ARA
scene = Scene()

# Visualise brain regions, and set opacity.
# Assign to variable to manipulate later
rsp = scene.add_brain_regions("RSP", alpha=0.2)


# load probe tracks from brainreg_segment
V1 = scene.add_from_file(("../data/regions/V1.obj"), color="cyan")
thalamus = scene.add_from_file(("../data/regions/thalamus.obj"), color="coral")

# change shading interpolation method
V1.mesh.GetProperty().SetInterpolationToFlat()
thalamus.mesh.GetProperty().SetInterpolationToFlat()

# Display the region
scene.render()
