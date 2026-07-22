import json

import streamlit as st
import streamlit.components.v1 as components

import config
from reviews import random_review


def copy_button(text: str) -> None:
    safe_text = json.dumps(text)
    components.html(
        f"""
        <button id="copyBtn" style="
            width:100%; padding:0.5em 1em; font-size:1rem;
            border-radius:0.5em; border:1px solid #A99E97;
            background:#EAE9E3; color:#332F2D; cursor:pointer;
            transition: background 0.15s ease, border-color 0.15s ease;">
            Copy Review
        </button>
        <script>
        const btn = document.getElementById('copyBtn');
        btn.addEventListener('mouseenter', () => {{
            btn.style.background = '#D0D7B3';
            btn.style.borderColor = '#B0BC79';
        }});
        btn.addEventListener('mouseleave', () => {{
            btn.style.background = '#EAE9E3';
            btn.style.borderColor = '#A99E97';
        }});
        btn.addEventListener('click', () => {{
            navigator.clipboard.writeText({safe_text});
            btn.innerText = 'Copied!';
            btn.style.background = '#B0BC79';
            btn.style.color = '#FAF7ED';
            setTimeout(() => {{
                btn.innerText = 'Copy Review';
                btn.style.background = '#EAE9E3';
                btn.style.color = '#332F2D';
            }}, 1500);
        }});
        </script>
        """,
        height=50,
    )


# --- Resolve which store this visitor belongs to, from ?store=<slug> ---
store_slug = st.query_params.get("store", config.DEFAULT_STORE)
store = config.STORE_CONFIG.get(store_slug)

st.set_page_config(page_title=f"Review {config.COMPANY_NAME}", page_icon="⭐", layout="centered")

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

col1, col2 = st.columns(2)
with col1:
    st.button("Another Suggestion", use_container_width=True, on_click=shuffle_review)
with col2:
    copy_button(st.session_state.review_text)

st.divider()
st.link_button(
    "Continue to Google ➡️",
    store["google_review_url"],
    use_container_width=True,
    type="primary",
)
st.caption(
    "On the Google page: tap the stars for your rating, paste your review, then Submit."
)
