import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="Learn ፊደል", layout="wide")

# Initialize session state
if "trace_letter" not in st.session_state:
    st.session_state["trace_letter"] = "ሀ"
if "points" not in st.session_state:
    st.session_state["points"] = 0
if "clear_count" not in st.session_state:
    st.session_state["clear_count"] = 0

# Title and points display
st.markdown("<h1 style='font-size: 3rem; margin-bottom: 0.5rem;'>🏫 Jimmy Academy</h1>", unsafe_allow_html=True)
st.markdown(f"<div style='text-align:right; font-size:1.2rem;'>⭐ Points: <strong>{st.session_state['points']}</strong></div>", unsafe_allow_html=True)

# Style
st.markdown("""
<style>
button[kind="secondary"] {
    font-size: 1.8rem !important;
    font-weight: bold !important;
    height: 50px !important;
    border-radius: 6px !important;
    padding: 4px 6px !important;
}
audio {
    display: none;
}
</style>
""", unsafe_allow_html=True)

left, right = st.columns([2.3, 1], gap="small")

# ----------------------------------
# 🎯 LEFT: Soundboard + Points
# ----------------------------------
with left:
    st.subheader("🎓 አማርኛ ፊደል Soundboard")

    letter_rows = [
        ['ሀ','ሁ','ሂ','ሃ','ሄ','ህ','ሆ'],
        ['ለ','ሉ','ሊ','ላ','ሌ','ል','ሎ'],
        ['ሐ','ሑ','ሒ','ሓ','ሔ','ሕ','ሖ'],
        ['መ','ሙ','ሚ','ማ','ሜ','ም','ሞ'],
        ['ሠ','ሡ','ሢ','ሣ','ሤ','ሥ','ሦ'],
        ['ረ','ሩ','ሪ','ራ','ሬ','ር','ሮ'],
        ['ሰ','ሱ','ሲ','ሳ','ሴ','ስ','ሶ'],
        ['ሸ','ሹ','ሺ','ሻ','ሼ','ሽ','ሾ'],
        ['ቀ','ቁ','ቂ','ቃ','ቄ','ቅ','ቆ'],
        ['በ','ቡ','ቢ','ባ','ቤ','ብ','ቦ'],
        ['ቨ','ቩ','ቪ','ቫ','ቬ','ቭ','ቮ'],
        ['ተ','ቱ','ቲ','ታ','ቴ','ት','ቶ'],
        ['ቸ','ቹ','ቺ','ቻ','ቼ','ች','ቾ'],
        ['ነ','ኑ','ኒ','ና','ኔ','ን','ኖ'],
        ['ኘ','ኙ','ኚ','ኛ','ኜ','ኝ','ኞ'],
        ['አ','ኡ','ኢ','ኣ','ኤ','እ','ኦ'],
        ['ከ','ኩ','ኪ','ካ','ኬ','ክ','ኮ'],
        ['ወ','ዉ','ዊ','ዋ','ዌ','ው','ዎ'],
        ['ዘ','ዙ','ዚ','ዛ','ዜ','ዝ','ዞ'],
        ['ዠ','ዡ','ዢ','ዣ','ዤ','ዥ','ዦ'],
        ['የ','ዩ','ዪ','ያ','ዬ','ይ','ዮ'],
        ['ደ','ዱ','ዲ','ዳ','ዴ','ድ','ዶ'],
        ['ጀ','ጁ','ጂ','ጃ','ጄ','ጅ','ጆ'],
        ['ገ','ጉ','ጊ','ጋ','ጌ','ግ','ጎ'],
        ['ጠ','ጡ','ጢ','ጣ','ጤ','ጥ','ጦ'],
        ['ጨ','ጩ','ጪ','ጫ','ጬ','ጭ','ጮ'],
        ['ጰ','ጱ','ጲ','ጳ','ጴ','ጵ','ጶ'],
        ['ፀ','ፁ','ፂ','ፃ','ፄ','ፅ','ፆ'],
        ['ፈ','ፉ','ፊ','ፋ','ፌ','ፍ','ፎ'],
        ['ፐ','ፑ','ፒ','ፓ','ፔ','ፕ','ፖ']
    ]

    for row in letter_rows:
        cols = st.columns(len(row))
        for i, letter in enumerate(row):
            if cols[i].button(letter, use_container_width=True):
                st.session_state["trace_letter"] = letter
                st.session_state["points"] += 1
                audio_path = f"audio/{letter}.mp3"
                if Path(audio_path).exists():
                    audio_b64 = base64.b64encode(Path(audio_path).read_bytes()).decode("utf-8")
                    st.components.v1.html(f"""
                        <audio autoplay>
                          <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
                        </audio>
                    """, height=0)

    # 🎉 Celebration every 5 points
    if st.session_state["points"] > 0 and st.session_state["points"] % 5 == 0:
        st.success("🎉 Great job! You’ve earned more stars!")

# ----------------------------------
# ✍️ RIGHT: Drawing Canvas + Clear Bonus
# ----------------------------------
with right:
    st.subheader("✍️ ፊደል Writing Practice")
    trace_letter = st.session_state["trace_letter"]

    canvas_html = f"""
    <style>
      .canvas-wrapper {{
        position: relative;
        width: 400px;
        height: 400px;
      }}
      .canvas-wrapper canvas {{
        position: absolute;
        top: 0;
        left: 0;
      }}
    </style>

    <div class="canvas-wrapper">
      <canvas id="trace" width="400" height="400"
        style="z-index: 0; pointer-events: none;">
      </canvas>
      <canvas id="draw" width="400" height="400"
        style="z-index: 1; border:1px solid #ccc; border-radius:8px; background:transparent;">
      </canvas>
    </div>
    <br/>
    <button onclick="clearDrawAndReward()" style="margin:4px; padding:6px 12px; border-radius:4px;">🧼 Clear Writing</button>
    <button onclick="clearTrace()" style="margin:4px; padding:6px 12px; border-radius:4px;">🗑️ Clear Tracing</button>

    <script>
      const trace = document.getElementById('trace');
      const traceCtx = trace.getContext('2d');
      traceCtx.clearRect(0, 0, trace.width, trace.height);
      traceCtx.font = '260px Noto Sans Ethiopic';
      traceCtx.fillStyle = 'rgba(150,150,150,0.2)';
      traceCtx.textAlign = 'center';
      traceCtx.textBaseline = 'middle';
      traceCtx.fillText("{trace_letter}", 200, 200);

      const draw = document.getElementById('draw');
      const ctx = draw.getContext('2d');
      let drawing = false;

      function getPos(e) {{
        const rect = draw.getBoundingClientRect();
        return {{
          x: (e.clientX || (e.touches?.[0]?.clientX)) - rect.left,
          y: (e.clientY || (e.touches?.[0]?.clientY)) - rect.top
        }};
      }}

      function drawLine(e) {{
        if (!drawing) return;
        const pos = getPos(e);
        ctx.lineWidth = 4;
        ctx.lineCap = 'round';
        ctx.strokeStyle = '#222';
        ctx.lineTo(pos.x, pos.y);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(pos.x, pos.y);
      }}

      draw.addEventListener('mousedown', e => {{ drawing = true; drawLine(e); }});
      draw.addEventListener('mousemove', drawLine);
      draw.addEventListener('mouseup', () => {{ drawing = false; ctx.beginPath(); }});
      draw.addEventListener('mouseleave', () => {{ drawing = false; ctx.beginPath(); }});

      draw.addEventListener('touchstart', e => {{ drawing = true; drawLine(e); }});
      draw.addEventListener('touchmove', e => {{ drawLine(e); e.preventDefault(); }}, {{ passive: false }});
      draw.addEventListener('touchend', () => {{ drawing = false; ctx.beginPath(); }});

      function clearDrawAndReward() {{
        fetch('/?clear=true');
        ctx.clearRect(0, 0, draw.width, draw.height);
      }}

      function clearTrace() {{
        traceCtx.clearRect(0, 0, trace.width, trace.height);
      }}
    </script>
    """

    st.components.v1.html(canvas_html, height=480)

# Reward point on clear (once per session * 5 times)
if "clear" in st.query_params:
    if st.session_state["clear_count"] < 5:
        st.session_state["points"] += 1
        st.session_state["clear_count"] += 1
    st.query_params.clear()  # Remove ?clear=true from URL
