from comfy_vhs.videohelpersuite.nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
import folder_paths
from comfy_vhs.videohelpersuite.server import server
from comfy_vhs.videohelpersuite import documentation
from comfy_vhs.videohelpersuite import latent_preview

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
documentation.format_descriptions(NODE_CLASS_MAPPINGS)
