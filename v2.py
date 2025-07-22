import streamlit as st
import streamlit.components.v1 as components

# Carrega o HTML base
with open("AssinaturaPrivacy.html", "r", encoding="utf-8") as file:
    html_template = file.read()

# Inputs do usuário
name = st.text_input("Nome:")
position = st.text_input("Cargo:")
email = st.text_input("E-mail:")

# Substitui os dados no HTML
assinatura_html = (
    html_template
    .replace("nomeCompleto", name)
    .replace("carcoCompleto", position)
    .replace("emailCompleto", email)
    .replace("eprivacy", "mailto:"+email)
)

# Exibe a assinatura com botão de copiar visual
st.markdown("### Pré-visualização da Assinatura")

# HTML com botão que copia visualmente a assinatura
html_with_copy_button = f"""
<div>
  <div id="assinatura-container" style="display:inline-block;padding:10px;">
    {assinatura_html}
  </div>
  <br><br>
  <button onclick="copySignature()" style="
         padding:8px 12px;
         background-color:#F28C3F;
         color:white;
         border:none;
         border-radius:4px;
         cursor:pointer;">
    Copiar Assinatura Privacy
  </button>
</div>

<script>
function copySignature() {{
    const range = document.createRange();
    const node = document.getElementById('assinatura-container');
    range.selectNode(node);
    const selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    document.execCommand('copy');
    selection.removeAllRanges();
    alert("Assinatura Privacy copiada! 🎉");
}}
</script>
"""

components.html(html_with_copy_button, height=400)
