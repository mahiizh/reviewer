import json

import streamlit as st
import streamlit.components.v1 as components

import config
from reviews import random_review


def copy_and_continue_button(text: str, url: str) -> None:
    safe_text = json.dumps(text)
    safe_url = json.dumps(url)
    components.html(
        f"""
        <button id="copyGoBtn" style="
            width:100%; padding:0.7em 1em; font-size:1rem; font-weight:600;
            border-radius:0.5em; border:none;
            background:#B0BC79; color:#FAF7ED; cursor:pointer;
            transition: background 0.15s ease;">
            Copy & Open Review box
        </button>
        <script>
        const btn = document.getElementById('copyGoBtn');
        btn.addEventListener('mouseenter', () => {{
            btn.style.background = '#9FAB68';
        }});
        btn.addEventListener('mouseleave', () => {{
            btn.style.background = '#B0BC79';
        }});
        btn.addEventListener('click', () => {{
            navigator.clipboard.writeText({safe_text});
            window.open({safe_url}, '_blank');
            btn.innerText = 'Copied! Opening Google...';
        }});
        </script>
        """,
        height=55,
    )


# --- Resolve which store this visitor belongs to, from ?store=<slug> ---
store_slug = st.query_params.get("store", config.DEFAULT_STORE)
store = config.STORE_CONFIG.get(store_slug)

st.set_page_config(
    page_title=f"Review {config.COMPANY_NAME}",
    page_icon="⭐",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items=None,
)

st.markdown(
    """
    <style>
    #MainMenu { visibility: hidden; }
    header { visibility: hidden; }
    footer { visibility: hidden; }
    [data-testid="stToolbar"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

if store is None:
    st.error(
        f"Unknown store link ('{store_slug}'). Please rescan the QR code at "
        "the counter, or ask staff for the correct review link."
    )
    st.stop()

# Reset the suggested review whenever the visitor lands on a different
# store than the one already in this session (e.g. a stale tab reused
# across visits).
if st.session_state.get("current_store") != store_slug:
    st.session_state.current_store = store_slug
    st.session_state.review_text = random_review(store["short_name"])

st.title(f"Thanks for visiting {store['name']}! ⭐")
st.caption(store["address"])
st.write(
    "We'd love a Google review. Here's a suggestion to get you started — "
    "edit it below to make it your own, then redirect to Google."
)

def shuffle_review() -> None:
    st.session_state.review_text = random_review(
        store["short_name"], exclude=st.session_state.review_text
    )


st.text_area("Your review", key="review_text", height=160, label_visibility="collapsed")

st.button("Another Suggestion", use_container_width=True, on_click=shuffle_review)

st.divider()
copy_and_continue_button(st.session_state.review_text, store["google_review_url"])
st.caption(
    "This copies your review and opens Google in a new tab — tap the stars for "
    "your rating, paste your review, then Submit."
)
