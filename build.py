#!/usr/bin/env python3
"""Genera la web de Paz en Su Presencia — diseño celestial (noche + cielo + oro).
Editar aquí y ejecutar:  python build.py
"""
import json
from textos import ORACIONES, SOBRE, AVISO, PRIV, COOK, IA

DOM = "https://pazensupresencia.com"
ML_URL = "https://assets.mailerlite.com/jsonp/2819117/forms/205228704711837491/subscribe"
CDN = "https://payhip.com/cdn-cgi/image/format=auto,width=600/https://pe56d.s3.amazonaws.com/"
YT = "https://www.youtube.com/@PazEnSuPresenciaOficial"
YT_SUB = YT + "?sub_confirmation=1"
YT_JOIN = "https://www.youtube.com/channel/UC7rshDFrKsfQ3rR3VX9ui_A/join"
SPOTIFY = "https://open.spotify.com/intl-es/artist/4fGFrnjkPyAhubtV4lOs6Q"
TIENDA = "https://payhip.com/PazenSuPresencia"
REDES = json.load(open("redes.json"))
STRIPE = {
    "3": "https://buy.stripe.com/4gMaEWfn03HR5ty7QLdjO01",
    "5": "https://buy.stripe.com/9B6fZg1wa3HRcW01sndjO02",
    "10": "https://buy.stripe.com/9B65kC4Imdir09eb2XdjO03",
    "una": "https://buy.stripe.com/8x2cN42Ae2DN09e5IDdjO00",
    "portal": "https://billing.stripe.com/p/login/8x2cN42Ae2DN09e5IDdjO00",
}
EXT = 'target="_blank" rel="noopener"'

def red_svg(k):
    return f'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{REDES[k][1]}</svg>'

# ---------------- Productos ----------------
# clave: (etiqueta, título, texto, precio, url, imagen, grupo)
P = {
 "cancionero": ("Nuevo", "Cancionero de Villancicos", "14 villancicos de siempre con su letra, ilustrados, para cantar juntos en Nochebuena.", "4,99", "https://payhip.com/b/fGOsv", "/img/cancionero.webp", "Navidad"),
 "adviento": ("", "Adviento en Familia 2026", "Para rezar en casa las cuatro semanas de Adviento, con la corona.", "4,99", "https://payhip.com/b/OIwTy", CDN+"o_1k84dap6qk18q5j1jmr1ci73f81a.png", "Navidad"),
 "posadas": ("", "Las Posadas en Familia", "Nueve noches para vivirlas en casa, del 16 al 24 de diciembre.", "4,99", "https://payhip.com/b/oTbJD", CDN+"o_1k87d9chf7ec1g8k1t1v182d24d1p.png", "Navidad"),
 "reyes": ("", "Kit del Día de Reyes", "Bendición de la casa, carta a los Reyes y coronas para recortar.", "3,99", "https://payhip.com/b/1739n", CDN+"o_1k8bijrvir54kalk7ut6212f21k.png", "Navidad"),
 "calendario": ("", "Calendario Litúrgico 2027", "Fiestas, santos y tiempos de la Iglesia mes a mes. A4 y carta.", "5,99", "https://payhip.com/b/cb4JT", CDN+"o_1k853asshmm9ak177ha0t2jj1n.png", "Oración"),
 "rosario": ("", "Guía del Santo Rosario", "Los 20 misterios ilustrados, paso a paso, para rezar en familia.", "3,99", "https://payhip.com/b/hgU9H", CDN+"o_1k8cht1va6ob1vut1surqlfcr71a.png", "Oración"),
 "navidad": ("", "La Navidad de Jesús", "30 dibujos para colorear la historia de Belén.", "3,99", "https://payhip.com/b/Hcn9z", CDN+"o_1k87bh3641f4r56v1pnq1buf3551q.png", "Colorear"),
 "arca": ("", "Los animales del Arca de Noé", "30 dibujos para colorear en familia.", "3,99", "https://payhip.com/b/JEQ9q", CDN+"o_1k87h3hdu138r10ee1g2f15o3rac1q.png", "Colorear"),
 "mandalas": ("", "Mandalas de Paz", "30 mandalas cristianos con salmos, para momentos de calma.", "4,99", "https://payhip.com/b/aQ9t5", CDN+"o_1k894ahvd8dm1smc1ommqdb1cs21o.png", "Colorear"),
 "packcol": ("Pack", "Pack Colorear en Familia", "La Navidad de Jesús + Los animales del Arca de Noé: 60 dibujos.", "5,99", "https://payhip.com/b/qiPbU", CDN+"o_1k8ag6tolf101o6thl62mu14p67.png", "Packs"),
}
PACK_NAV = ("https://payhip.com/b/LHAio", CDN+"o_1k8ag4v861ah81k5e18qeku51k737.png")

def tarjeta(k):
    et, ti, tx, pr, url, img, _ = P[k]
    etq = f'<span class="etq">{et}</span>' if et else ""
    return f'''<a class="prod" href="{url}" {EXT}>
 <div class="img">{etq}<span class="precio">US$ {pr}</span><img src="{img}" alt="{ti}" loading="lazy" width="600" height="600"></div>
 <div class="cuerpo"><h3>{ti}</h3><p>{tx}</p><span class="comprar">Lo quiero →</span></div>
</a>'''

PACK = f'''<div class="pack">
 <a href="{PACK_NAV[0]}" {EXT}><img src="{PACK_NAV[1]}" alt="Pack Navidad en Familia" loading="lazy" width="600" height="600"></a>
 <div>
  <span class="ahorro">Ahorras US$ 5,98</span>
  <h3 style="font-size:clamp(1.6rem,3.4vw,2.2rem)">Pack Navidad en Familia</h3>
  <p style="color:#C9D2E8">Adviento + Posadas + Calendario Litúrgico 2027: todo lo que necesitas para vivir el Adviento y la Navidad en casa, en un solo pack.</p>
  <p style="font-size:1.6rem;font-weight:700;color:var(--oro2);margin-bottom:18px">US$ 9,99 <span class="tachado">US$ 15,97</span></p>
  <a class="btn b-oro" href="{PACK_NAV[0]}" {EXT}>Quiero el pack completo</a>
 </div>
</div>'''

CONFIANZA = '<div class="confianza"><span>Descarga inmediata en PDF</span><span>Imprime las veces que quieras</span><span>Pago seguro con tarjeta, Apple Pay o Google Pay</span><span>A4 y carta (EE. UU.)</span></div>'

# ---------------- Piezas comunes ----------------
MENU = [("/rezar-hoy.html", "Rezar hoy"), ("/#novena", "Novena gratis"), ("/tienda.html", "Tienda"),
        ("/#musica", "Música"), ("/sobre-nosotros.html", "Nosotros")]

def cabecera():
    items = "".join(f'<li><a href="{u}">{t}</a></li>' for u, t in MENU)
    return f'''<div class="aviso">🕯️ La Novena a la Virgen de Guadalupe empieza el jueves 3 de diciembre · <a href="/#novena">Recíbela gratis →</a></div>
<header class="cab"><div class="w">
 <a class="logo" href="/"><img src="/img/logo-96.webp" alt="" width="46" height="46">Paz en Su Presencia</a>
 <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menú</button>
 <nav class="nav" id="nav" aria-label="Principal"><ul>{items}<li><a class="btn b-oro" href="/#circulo">Colabora</a></li></ul></nav>
</div></header>'''

def pie():
    return f'''<footer class="pie"><div class="w">
 <div class="cols">
  <div><a class="logo" href="/"><img src="/img/logo-96.webp" alt="" width="46" height="46">Paz en Su Presencia</a>
   <p style="margin-top:14px">Música cristiana original, oración y recursos católicos para rezar en familia. Hecho en España para todo el mundo hispano.</p></div>
  <div><h3>Explora</h3><ul><li><a href="/#novena">Novena gratis</a></li><li><a href="/tienda.html">Tienda</a></li><li><a href="/rezar-hoy.html">La oración de hoy</a></li><li><a href="/#musica">Música</a></li><li><a href="/#circulo">Círculo de Paz</a></li><li><a href="/sobre-nosotros.html">Nosotros</a></li></ul></div>
  <div><h3>Síguenos</h3><ul><li><a href="{YT_SUB}" {EXT}>YouTube</a></li><li><a href="{SPOTIFY}" {EXT}>Spotify</a></li><li><a href="{REDES['ig'][0]}" {EXT}>Instagram</a></li><li><a href="{REDES['fb'][0]}" {EXT}>Facebook</a></li><li><a href="{REDES['tt'][0]}" {EXT}>TikTok</a></li><li><a href="{REDES['pi'][0]}" {EXT}>Pinterest</a></li><li><a href="mailto:hola@pazensupresencia.com">hola@pazensupresencia.com</a></li></ul></div>
 </div>
 <div class="legal"><span>© 2026 Paz en Su Presencia</span><span><a href="/aviso-legal.html">Aviso legal</a> · <a href="/privacidad.html">Privacidad</a> · <a href="/cookies.html">Cookies</a> · <a href="/uso-de-ia.html">Uso de IA</a></span></div>
</div></footer>
<div class="barra-movil"><a class="btn b-oro" href="/#novena">🎁 Novena gratis</a><a class="btn b-linea" href="/tienda.html">🛍️ Tienda</a></div>
<script>
(function(){{
 var b=document.querySelector('.menu-btn'),n=document.getElementById('nav');
 function cerrar(){{n.classList.remove('abierto');b.setAttribute('aria-expanded','false');b.textContent='Menú';}}
 b.addEventListener('click',function(){{var a=n.classList.toggle('abierto');b.setAttribute('aria-expanded',a);b.textContent=a?'Cerrar':'Menú';}});
 n.querySelectorAll('a').forEach(function(a){{a.addEventListener('click',cerrar);}});
 document.querySelectorAll('.onda').forEach(function(e){{var n=+e.dataset.n||60,h=+e.dataset.h||30,s='';for(var i=0;i<n;i++){{var v=Math.abs(Math.sin(i*1.7)*Math.cos(i*.45));s+='<i style="height:'+Math.round(4+v*h)+'px"></i>';}}e.innerHTML=s;}});
 document.querySelectorAll('form.ml').forEach(function(f){{
  f.addEventListener('submit',function(e){{
   e.preventDefault();
   if(f.querySelector('[name=web]').value)return;
   var em=f.querySelector('[type=email]'),ck=f.querySelector('[type=checkbox]');
   if(!em.value||em.value.indexOf('@')<1){{em.focus();return;}}
   if(!ck.checked){{ck.focus();ck.parentNode.style.color='#9B2C45';return;}}
   var d=new FormData(f);d.delete('web');d.append('ml-submit','1');d.append('anticsrf','true');
   var btn=f.querySelector('button');btn.disabled=true;btn.textContent='Enviando…';
   function ok(){{f.parentNode.classList.add('enviado');}}
   function mal(t){{btn.disabled=false;btn.textContent=t;em.focus();}}
   fetch('{ML_URL}',{{method:'POST',body:d}})
   .then(function(r){{return r.json();}})
   .then(function(j){{if(j&&j.success){{ok();}}else{{mal('Revisa tu correo e inténtalo de nuevo');}}}})
   .catch(function(){{fetch('{ML_URL}',{{method:'POST',body:d,mode:'no-cors'}}).then(ok).catch(function(){{mal('Inténtalo de nuevo');}});}});
  }});
 }});
}})();
</script>
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "a708560c8d5b40fc872ec908e790fb5d"}}'></script><!-- End Cloudflare Web Analytics -->'''

def pagina(nombre, titulo, descripcion, cuerpo, ruta=None, extra=""):
    ruta = ruta if ruta is not None else ("/" if nombre == "index.html" else "/" + nombre)
    open(nombre, "w").write(f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<link rel="canonical" href="{DOM}{ruta}">
<meta name="theme-color" content="#07101F">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/fonts/outfit-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/outfit-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/estilo.css">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="Paz en Su Presencia">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descripcion}">
<meta property="og:url" content="{DOM}{ruta}">
<meta property="og:image" content="{DOM}/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
{extra}
</head>
<body>
{cabecera()}
<main id="contenido">
{cuerpo}
</main>
{pie()}
</body>
</html>
''')

def formulario(id_, boton="Quiero recibir la novena gratis", titulo=""):
    t = f"<h3>{titulo}</h3>" if titulo else ""
    return f'''<div class="cristal" id="{id_}">{t}
 <form class="ml" novalidate>
  <label for="{id_}-n">Tu nombre</label>
  <input id="{id_}-n" type="text" name="fields[name]" autocomplete="given-name" placeholder="Ej.: María">
  <label for="{id_}-e">Tu correo electrónico</label>
  <input id="{id_}-e" type="email" name="fields[email]" autocomplete="email" required placeholder="tucorreo@ejemplo.com">
  <input type="text" name="web" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
  <label class="casilla"><input type="checkbox" required><span>Acepto recibir los correos de la novena y otros de Paz en Su Presencia. He leído la <a href="/privacidad.html">política de privacidad</a>.</span></label>
  <button class="btn b-osc b-ancho" type="submit">{boton}</button>
  <p class="micro">Gratis · Sin spam · Te das de baja con un clic</p>
 </form>
 <div class="ok" role="status"><strong>¡Ya casi está!</strong> Te hemos enviado un correo para confirmar tu dirección. Ábrelo y pulsa «Confirmar»: así te llegará la novena cada mañana del 3 al 11 de diciembre. Si no lo ves, mira en «Promociones» o «Spam».</div>
</div>'''

# ---------------- Oración del día ----------------
OR_JS = "var OR=" + json.dumps(ORACIONES, ensure_ascii=False) + ";" + r'''
(function(){
 var d=new Date(),i=Math.floor(Date.UTC(d.getFullYear(),d.getMonth(),d.getDate())/864e5)%OR.length,o=OR[i];
 var t=document.getElementById('or-tit'),x=document.getElementById('or-txt'),w=document.getElementById('or-wa'),c=document.getElementById('or-cp');
 if(!t)return;t.textContent=o[0];x.textContent=o[1];
 var msg='🕊️ '+o[0]+'\n\n'+o[1]+'\n\nOración de hoy · pazensupresencia.com/rezar-hoy';
 w.href='https://wa.me/?text='+encodeURIComponent(msg);
 c.addEventListener('click',function(){try{navigator.clipboard.writeText(msg).then(function(){c.textContent='¡Copiada!';});}catch(e){}});
})();'''

def bloque_oracion():
    return f'''<div class="oracion">
 <div class="halo">🕯️</div>
 <span class="eyebrow">La oración de hoy</span>
 <h2 id="or-tit">{ORACIONES[0][0]}</h2>
 <p class="texto" id="or-txt">{ORACIONES[0][1]}</p>
 <div class="botones"><a class="btn b-wa" id="or-wa" href="https://wa.me/" {EXT}>Enviar por WhatsApp</a><button class="btn b-lin-osc" id="or-cp" type="button">Copiar</button></div>
 <p class="micro" style="margin-top:16px">Cambia cada día. Compártela con quien la necesite.</p>
</div>
<script>{OR_JS}</script>'''

# ---------------- Música ----------------
VIDEOS = [("CsQpKkbjIaw", "Virgen de Guadalupe", "Ranchera"),
          ("8BWvtROh5YU", "Noche de Paz", "Villancico"),
          ("mX97jxPs9pc", "Villancicos flamencos", "Álbum completo")]
GENEROS = [("Rumba", "rumba cristiana", "g1"), ("Tango", "tango cristiano", "g2"), ("Jazz", "jazz cristiano", "g3"),
           ("Samba", "samba cristiana", "g4"), ("Reggae", "reggae cristiano", "g5"), ("Flamenco", "flamenco cristiano", "g6")]

MUSICA = f'''<section class="sec noche tech" id="musica"><div class="w">
 <div class="cab-sec"><div><span class="eyebrow">Nuestra música</span><h2>Suena en Spotify y YouTube</h2>
  <p class="lead">Canciones originales para alabar, rezar y descansar en Dios, en todos los estilos.</p></div>
  <div class="botones"><a class="btn b-oro" href="{SPOTIFY}" {EXT}>Seguir en Spotify</a><a class="btn b-linea" href="{YT_SUB}" {EXT}>Suscribirse en YouTube</a></div></div>
 <div class="musica">
  <a class="reproductor" href="{SPOTIFY}" {EXT}>
   <div class="portada-rep"><img src="/img/logo-320.webp" alt="" width="320" height="320" loading="lazy"></div>
   <h3>Paz en Su Presencia</h3><div class="art">Música cristiana original · Spotify</div>
   <div class="barra"><i></i></div>
   <div class="controles"><span class="play"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span><span>Escuchar en Spotify</span></div>
  </a>
  <div>
   <div class="lista">{"".join(f'<a class="fila" href="https://www.youtube.com/watch?v={v}" {EXT}><span class="n">{i+1}</span><img src="https://i.ytimg.com/vi/{v}/mqdefault.jpg" alt="" loading="lazy" width="320" height="180"><span class="nm">{t}<small>{g}</small></span><span class="ver">▶ Ver</span></a>' for i,(v,t,g) in enumerate(VIDEOS))}</div>
   <div class="generos">{"".join(f'<a class="gen {c}" href="{YT}/search?query={q.replace(" ","+")}" {EXT}><span><small>ESTILO</small>{n}</span></a>' for n,q,c in GENEROS)}</div>
  </div>
 </div>
</div></section>'''

CIRCULO = f'''<section class="sec cielo" id="circulo"><div class="w circulo">
 <div class="anillo"><img src="/img/jesus_circulo.webp" alt="" width="340" height="340" loading="lazy"></div>
 <div>
  <span class="eyebrow">Círculo de Paz</span>
  <h2>Ayúdanos a llevar oración a muchas casas</h2>
  <p class="lead">Paz en Su Presencia es un proyecto pequeño e independiente. Grabar cada canción y preparar cada vídeo tiene un coste. Si este canal te acompaña, puedes sostenerlo con una aportación voluntaria.</p>
  <div class="niveles">
   <a class="nivel" href="{STRIPE['3']}" {EXT}>US$ 3/mes<small>Amigo</small></a>
   <a class="nivel" href="{STRIPE['5']}" {EXT}>US$ 5/mes<small>Compañero</small></a>
   <a class="nivel" href="{STRIPE['10']}" {EXT}>US$ 10/mes<small>Sostén</small></a>
   <a class="nivel" href="{STRIPE['una']}" {EXT}>Una vez<small>Lo que quieras</small></a>
  </div>
  <p>🎁 Cada mes, los miembros del Círculo reciben por correo un imprimible de regalo. También puedes <a href="{YT_JOIN}" {EXT}><strong>hacerte miembro en YouTube</strong></a>.</p>
  <p class="garantia">Apoyo voluntario a un proyecto creativo: no es un donativo deducible ni está ligado a ninguna oración o intención; rezamos por todos por igual. Pago seguro con Stripe. Cambia o cancela cuando quieras en el <a href="{STRIPE['portal']}" {EXT}>portal de gestión</a>.</p>
 </div>
</div></section>'''

REDES_DESC = [("yt", "YouTube", "Vídeos y oraciones"), ("sp", "Spotify", "Nuestra música"), ("ig", "Instagram", "Fe cada día"),
              ("fb", "Facebook", "Comunidad"), ("tt", "TikTok", "Momentos de paz"), ("pi", "Pinterest", "Ideas e imprimibles")]
REDES_SEC = f'''<section class="sec noche"><div class="w">
 <div class="centro" style="margin-bottom:34px"><span class="eyebrow">Caminemos juntos</span><h2>Síguenos cada día</h2><p class="lead">Música, oración y paz en tus redes favoritas.</p></div>
 <div class="redes">{"".join(f'<a class="red r-{k}" href="{YT_SUB if k=="yt" else (SPOTIFY if k=="sp" else REDES[k][0])}" {EXT}>{red_svg(k)}<b>{n}</b><small>{d}</small></a>' for k,n,d in REDES_DESC)}</div>
</div></section>'''

ORG_LD = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "Organization", "name": "Paz en Su Presencia", "url": DOM, "logo": DOM + "/img/logo.png", "email": "hola@pazensupresencia.com", "sameAs": [YT, SPOTIFY, REDES["ig"][0], REDES["fb"][0], REDES["tt"][0], REDES["pi"][0]]}, ensure_ascii=False) + "</script>"

# ---------------- PORTADA ----------------
INICIO = f'''<section class="hero">
 <div class="rayos"></div>
 <div class="jesus"><img src="/img/jesus_hero.jpg" alt="Jesús con una paloma bajo la luz del cielo" width="600" height="630" fetchpriority="high"></div>
 <div class="w"><div class="hcont">
  <span class="eyebrow">Música · Oración · Familia</span>
  <p class="marca-hero">Paz en Su Presencia</p>
  <div class="sub">Fortalece tu fe a través de la música</div>
  <p>Música cristiana original, oraciones para cada día y recursos católicos para rezar en casa.</p>
  <div class="chips">{"".join(f'<a href="{YT}/search?query={q.replace(" ","+")}" {EXT}>{n}</a>' for n,q in [("Rancheras","ranchera"),("Flamenco","flamenco"),("Tango","tango"),("Jazz","jazz"),("Rumba","rumba"),("Villancicos","villancicos")])}</div>
  <div class="botones"><a class="btn b-oro" href="#novena">🎁 Novena gratis</a><a class="btn b-linea" href="/tienda.html">🛍️ Ver la tienda</a></div>
  <p class="mini-cta">o <a href="{SPOTIFY}" {EXT}>▶ escucha nuestra música</a></p>
  <div class="onda" data-n="64" data-h="30" aria-hidden="true"></div>
 </div></div>
</section>

<section class="sec cielo" id="novena"><div class="w nov">
 <div>
  <span class="eyebrow">Adviento 2026 · Gratis</span>
  <h1 class="h2">Reza la Novena a la Virgen de Guadalupe en familia</h1>
  <p class="lead">Del 3 al 11 de diciembre, cada mañana en tu correo: la oración del día, una lectura breve y un villancico para escuchar juntos. El 12, una oración especial para el día de la Virgen.</p>
  <p class="micro" style="text-align:left">¿Te apuntas con la novena ya empezada? Recibirás los días que quedan y en el correo de bienvenida tienes la novena completa en PDF para ponerte al día.</p>
  <div class="ventajas"><div><b>✉</b>Un correo cada mañana del 3 al 11, y uno especial el 12</div><div><b>✦</b>Oración y lectura en 5 minutos</div><div><b>♪</b>Música para rezar juntos</div></div>
 </div>
 {formulario("form-novena", titulo="Recíbela gratis en tu correo")}
</div></section>

<section class="sec noche tech" id="tienda"><div class="w">
 <div class="cab-sec"><div><span class="eyebrow">Recursos para imprimir</span><h2>Vive la Navidad en casa</h2>
  <p class="lead">PDF ilustrados para descargar al momento e imprimir las veces que quieras.</p></div>
  <a class="btn b-linea" href="/tienda.html">Ver los 11 recursos →</a></div>
 <div class="prods">{"".join(tarjeta(k) for k in ["cancionero","adviento","posadas","reyes","rosario","calendario"])}</div>
 {PACK}
 {CONFIANZA}
</div></section>

<section class="sec cielo"><div class="w">{bloque_oracion()}</div></section>

{MUSICA}

{CIRCULO}

{REDES_SEC}

<section class="sec cielo"><div class="w estrecho">
 <div class="centro" style="margin-bottom:26px"><span class="eyebrow">Novena gratis</span><h2>¿Rezamos juntos estos nueve días?</h2></div>
 {formulario("form-novena-2", "Sí, quiero rezar la novena")}
</div></section>'''

pagina("index.html", "Paz en Su Presencia · Música cristiana, oración y recursos católicos",
       "Recibe gratis la Novena a la Virgen de Guadalupe, la oración de cada día, música cristiana original y recursos católicos imprimibles para Adviento y Navidad.",
       INICIO, extra=ORG_LD)

# ---------------- TIENDA ----------------
grupos = [("Navidad y Adviento", ["cancionero", "adviento", "posadas", "reyes"]),
          ("Para rezar todo el año", ["rosario", "calendario"]),
          ("Para colorear en familia", ["packcol", "navidad", "arca", "mandalas"])]
AMAZON = f'''<div class="pack" style="margin-top:56px;background:linear-gradient(135deg,#1B2D57,#13234A);border-color:#ffffff26">
 <div style="font-size:4rem;text-align:center">📦</div>
 <div><span class="ahorro" style="background:#232F3E">También impreso</span>
  <h3 style="font-size:clamp(1.4rem,3vw,1.9rem)">«La Navidad de Jesús» en tapa blanda, en Amazon</h3>
  <p style="color:#C9D2E8">El libro para colorear, impreso y enviado a casa por Amazon. Ideal para regalar estas Navidades.</p>
  <div class="botones"><a class="btn b-oro" href="https://www.amazon.com/dp/B0HT1FD2N1" {EXT}>Amazon EE. UU.</a><a class="btn b-linea" href="https://www.amazon.es/dp/B0HT1FD2N1" {EXT}>Amazon España</a><a class="btn b-linea" href="https://www.amazon.co.uk/dp/B0HT1FD2N1" {EXT}>Amazon UK</a></div>
 </div>
</div>'''

TIENDA_HTML = f'''<section class="sec noche tech"><div class="w">
 <span class="eyebrow">Tienda</span>
 <h1 style="font-size:clamp(2.4rem,5.5vw,3.8rem)">Recursos católicos para rezar en familia</h1>
 <p class="lead">PDF ilustrados para descargar al momento e imprimir en casa las veces que quieras. Precios en dólares estadounidenses (US$).</p>
 {PACK}
 {"".join(f'<div class="grupo"><h3>{g}</h3><div class="prods">{"".join(tarjeta(k) for k in ks)}</div></div>' for g, ks in grupos)}
 {AMAZON}
 {CONFIANZA}
 <p class="centro" style="margin-top:30px;color:var(--secn);font-size:.92rem">Ilustraciones creadas con ayuda de inteligencia artificial y revisadas a mano. ¿Dudas? <a href="mailto:hola@pazensupresencia.com" style="color:var(--oro2)">hola@pazensupresencia.com</a> · <a href="{TIENDA}" {EXT} style="color:var(--oro2)">Tienda en Payhip</a></p>
</div></section>
{CIRCULO}'''
pagina("tienda.html", "Tienda · Recursos católicos imprimibles · Paz en Su Presencia",
       "Cancionero de villancicos, Adviento en familia, Posadas, Kit de Reyes, calendario litúrgico 2027, guía del Rosario y libros para colorear cristianos en PDF.", TIENDA_HTML)

# ---------------- REZAR HOY ----------------
REZAR = f'''<section class="sec cielo"><div class="w">{bloque_oracion()}</div></section>
<section class="sec noche"><div class="w estrecho">
 <div class="centro" style="margin-bottom:26px"><span class="eyebrow">Novena gratis</span><h2>Recibe la novena en tu correo</h2></div>
 {formulario("form-rezar")}
</div></section>'''
pagina("rezar-hoy.html", "La oración de hoy · Paz en Su Presencia",
       "Una oración católica breve para cada día, para rezar en casa y compartir por WhatsApp.", REZAR)

pagina("sobre-nosotros.html", "Quiénes somos · Paz en Su Presencia",
       "Paz en Su Presencia: música cristiana, oración y recursos católicos hechos en España para rezar en familia.", SOBRE + REDES_SEC)
pagina("aviso-legal.html", "Aviso legal · Paz en Su Presencia", "Aviso legal del sitio web Paz en Su Presencia.", AVISO)
pagina("privacidad.html", "Política de privacidad · Paz en Su Presencia", "Cómo trata Paz en Su Presencia tus datos personales.", PRIV)
pagina("cookies.html", "Política de cookies · Paz en Su Presencia", "Esta web no usa cookies de análisis ni de publicidad.", COOK)
pagina("uso-de-ia.html", "Uso de inteligencia artificial · Paz en Su Presencia", "Cómo y para qué usa Paz en Su Presencia la inteligencia artificial.", IA)
pagina("404.html", "Página no encontrada · Paz en Su Presencia", "Página no encontrada.",
       '<section class="pagina cielo"><div class="w estrecho centro"><h1>Esta página no existe</h1><p>Quizá te interese la oración de hoy o la novena gratis.</p><div class="botones" style="justify-content:center"><a class="btn b-osc" href="/">Ir al inicio</a><a class="btn b-lin-osc" href="/tienda.html">Ver la tienda</a></div></div></section>', ruta="/404.html")

paginas = ["", "tienda.html", "rezar-hoy.html", "sobre-nosotros.html", "aviso-legal.html", "privacidad.html", "cookies.html", "uso-de-ia.html"]
open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{DOM}/{p}</loc><lastmod>2026-11-27</lastmod></url>\n" for p in paginas) + "</urlset>\n")
open("robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {DOM}/sitemap.xml\n")
open("_redirects", "w").write("/novena  /#novena  302\n/colabora  /#circulo  302\n/circulo-de-paz  /#circulo  302\n/musica  /#musica  302\n/tienda  /tienda.html  301\n")
print("OK")
