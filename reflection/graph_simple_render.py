from graph_simple import create_reflection_graph

# Generate a Mermaid PNG of the reflection graph
graph = create_reflection_graph().compile()
png_bytes = graph.get_graph().draw_mermaid_png()  #sym:draw_mermaid_png
with open("reflection_graph.png", "wb") as f:
    f.write(png_bytes)