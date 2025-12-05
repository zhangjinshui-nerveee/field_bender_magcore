import cadquery as cq

# A plate with a centered hole
model = (
    cq.Workplane("XY")
    .box(50, 50, 5)
    .faces(">Z")
    .workplane()
    .hole(10)
)

# [ ] s shape plate
# [ ] squares on the ends of s shape
# [ ] s shape plate rotated

# Export as STEP
cq.exporters.export(model, "plate.step")

# Export as STL
cq.exporters.export(model, "plate.stl")
