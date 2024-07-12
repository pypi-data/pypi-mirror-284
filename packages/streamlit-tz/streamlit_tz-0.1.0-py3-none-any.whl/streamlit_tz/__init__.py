from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called streamlit_tz,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component("streamlit_tz", path=str(frontend_dir))


def streamlit_tz(key: Optional[str] = None):
    """Creates a new instance of the streamlit_tz component."""
    component_value = _component_func(key=key)
    return component_value


def example():
    """Shows an example of the streamlit_tz component."""
    from datetime import datetime, UTC
    from zoneinfo import ZoneInfo

    import streamlit as st

    tz = streamlit_tz()
    now = datetime.now(UTC)
    st.write(f"Time in UTC: {now}")
    st.write(f"Time in {tz}: {now.astimezone(ZoneInfo(tz))}")


if __name__ == "__main__":
    example()
