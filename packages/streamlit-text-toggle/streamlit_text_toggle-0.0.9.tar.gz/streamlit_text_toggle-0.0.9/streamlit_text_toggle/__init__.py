import os
import streamlit.components.v1 as components
import json

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "toggle_button_set",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("toggle_button_set", path=build_dir)

def toggle_button_set(options_text, options_list, size="medium", use_container_width=False, scale=1, key=None):
    """Create a toggle button set component.

    Parameters:
    -----------
    options_text : list
        A list of characters to display as buttons.
    options_list : list
        A list of corresponding pronunciations for each character. Each item can be a single pronunciation or multiple pronunciations separated by '|'.
    size : str, optional
        Size of the buttons. Can be "small", "medium", or "large". Default is "medium".
    use_container_width : bool, optional
        Whether to use the full width of the container. Default is False.
    key : str, optional
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns:
    --------
    dict
        A dictionary where keys are selected characters and values are their selected pronunciations.
    """
    # Ensure all inputs are JSON serializable
    def json_serializable(obj):
        if isinstance(obj, (str, int, float, bool, type(None))):
            return obj
        elif isinstance(obj, (list, tuple)):
            return [json_serializable(item) for item in obj]
        elif isinstance(obj, dict):
            return {str(key): json_serializable(value) for key, value in obj.items()}
        else:
            return str(obj)

    component_args = {
        "options_text": json_serializable(options_text),
        "options_list": json_serializable(options_list),
        "size": json_serializable(size),
        "use_container_width": json_serializable(use_container_width),
        "key": json_serializable(key),
        "scale": json_serializable(scale)
    }

    component_value = _component_func(**component_args)

    return component_value