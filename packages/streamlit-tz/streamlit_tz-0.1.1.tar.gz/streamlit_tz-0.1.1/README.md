# streamlit-tz

Streamlit component that returns the user browser IANA timezone

## Installation instructions

```sh
pip install streamlit-tz
```

## Usage instructions

```python
from datetime import datetime, UTC
from zoneinfo import ZoneInfo

import streamlit as st
from streamlit_tz import streamlit_tz


tz = streamlit_tz()
now = datetime.now(UTC)
st.write(f"Time UTC: {now}")
st.write(f"Time in {tz}: {now.astimezone(ZoneInfo(tz))}")
```
