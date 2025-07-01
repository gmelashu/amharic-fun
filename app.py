import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

st.set_page_config(page_title="Learn ፊደል", layout="wide")

# 🏫 App Title
st.markdown("<h1 style='font-size: 3rem; margin-bottom: 0.5rem;'>🏫 Jimmy Academy</h1>", unsafe_allow_html=True)

# 🎨 Style letter buttons
st.markdown("""
<style>
button[kind="secondary"] {
    font-size: 1.8rem !important;
    font-weight: bold !important;
    height: 50px !important;
    border-radius: 6px !important;
    padding: 4px 6px !important;
}
</style>
""", unsafe_allow_html=True)

# Layout split
left, right = st.columns([2.3, 1], gap="small")

# ----------------------------------
# 🎯 LEFT: Soundboard
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

    def get_base64_audio(letter):
        path = f"audio/{letter}.mp3"
        if not Path(path).exists():
            return None
        return base64.b64encode(Path(path).read_bytes()).decode()

    for row in letter_rows:
        cols = st.columns(len(row))
        for i, letter in enumerate(row):
            if cols[i].button(letter, use_container_width=True):
                audio_b64 = get_base64_audio(letter)
                if audio_b64:
                    st.session_state["trace_letter"] = letter
                    components.html(f"""
                        <script>
                        var audio = new Audio('data:audio/mp3;base64,{audio_b64}');
                        audio.play();
                        </script>
                    """, height=0)

# ----------------------------------
# ✍️ RIGHT: Drawing Canvas
# ----------------------------------
with right:
    st.subheader("✍️ ፊደል Writing Practice")
    trace_letter = st.session_state.get("trace_letter", "ሀ")

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
    <button onclick="clearDraw()" style="margin:4px; padding:6px 12px; border-radius:4px;">🧼 Clear Writing</button>
    <button onclick="clearTrace()" style="margin:4px; padding:6px 12px; border-radius:4px;">🗑️ Clear Tracing</button>

    <script>
      // Draw trace letter
      const trace = document.getElementById('trace');
      const traceCtx = trace.getContext('2d');
      traceCtx.clearRect(0, 0, trace.width, trace.height);
      traceCtx.font = '260px Noto Sans Ethiopic';
      traceCtx.fillStyle = 'rgba(150,150,150,0.2)';
      traceCtx.textAlign = 'center';
      traceCtx.textBaseline = 'middle';
      traceCtx.fillText("{trace_letter}", 200, 200);

      // Draw layer
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

      function clearDraw() {{
        ctx.clearRect(0, 0, draw.width, draw.height);
      }}

      function clearTrace() {{
        traceCtx.clearRect(0, 0, trace.width, trace.height);
      }}
    </script>
    """

    components.html(canvas_html, height=480)