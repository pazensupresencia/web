# Textos fijos de la web (oraciones, quiénes somos, páginas legales)
ORACIONES = [
    ("Para empezar el día", "Señor, gracias por este nuevo día.\nPongo en tus manos lo que voy a hacer,\nlas personas que voy a encontrar\ny lo que me preocupa.\nQue hoy sepa reconocerte en lo pequeño.\nAmén."),
    ("Por la familia", "Jesús, que creciste en una casa sencilla de Nazaret,\nbendice nuestro hogar.\nDanos paciencia para escucharnos,\nhumildad para pedir perdón\ny alegría para estar juntos.\nAmén."),
    ("En la preocupación", "Padre bueno, hoy me pesa el corazón.\nNo sé bien qué pedirte,\npero sé que Tú me conoces.\nDame tu paz, la que no depende de que todo salga bien.\nDescanso en Ti.\nAmén."),
    ("A la Virgen María", "Madre mía, Virgen de Guadalupe,\ntú que dijiste a Juan Diego que no se preocupara,\nponme también a mí bajo tu manto.\nLlévame de la mano hasta tu Hijo.\nAmén."),
    ("Para dar gracias", "Señor, hoy no te pido nada:\nsolo quiero darte gracias\npor la vida, por los míos,\npor el pan de cada día\ny por tantas cosas buenas que no merezco.\nAmén."),
    ("Por los que sufren", "Jesús, te presento a todos los que hoy sufren:\nlos enfermos, los que están solos,\nlos que han perdido a alguien querido.\nQue sientan tu cercanía\ny que nosotros sepamos acompañarlos.\nAmén."),
    ("Para terminar el día", "Señor, termina este día.\nGracias por lo bueno que me has dado;\nperdona lo que no hice bien.\nCuida esta noche de mi casa y de los que quiero.\nEn tus manos descanso.\nAmén."),
]


SOBRE = '''<section class="pagina cielo"><div class="w estrecho">
 <h1>Quiénes somos</h1>
 <p>Paz en Su Presencia nació en España con una idea sencilla: que rezar en casa sea fácil, bonito y para todos. Es un proyecto pequeño e independiente que quiere poner su granito de arena para que la oración vuelva a la mesa, al salón y a la habitación de los niños.</p>
 <p>En nuestro canal de YouTube publicamos música cristiana original —rancheras, flamenco, villancicos, alabanza— y oraciones para la mañana y la noche. En esta web preparamos materiales para imprimir: novenas, Adviento, Posadas, el Rosario, calendarios y libros para colorear.</p>
 <h2>Cómo trabajamos</h2>
 <ul>
  <li>Los textos los escribimos y revisamos nosotros. Las citas bíblicas aparecen parafraseadas.</li>
  <li>Usamos herramientas de inteligencia artificial para las ilustraciones y parte de la música, y lo decimos con claridad. <a href="/uso-de-ia.html">Más información</a>.</li>
  <li>Rezamos por todos por igual. Las peticiones de oración son siempre gratis y nunca dependen de una compra o una aportación.</li>
 </ul>
 <h2>Escríbenos</h2>
 <p>Nos encanta leer cómo usáis los materiales en casa o en la parroquia: <a href="mailto:hola@pazensupresencia.com">hola@pazensupresencia.com</a>.</p>
</div></section>'''

TITULAR = '''<ul>
 <li><strong>Titular:</strong> Sergio Samblás García</li>
 <li><strong>NIF:</strong> 75264166R</li>
 <li><strong>Domicilio:</strong> Plaza de Luarca, 04740 Roquetas de Mar (Almería), España</li>
 <li><strong>Correo:</strong> <a href="mailto:hola@pazensupresencia.com">hola@pazensupresencia.com</a></li>
 <li><strong>Sitio web:</strong> pazensupresencia.com</li>
</ul>'''

AVISO = f'''<section class="pagina cielo"><div class="w estrecho">
 <h1>Aviso legal</h1>
 <p>En cumplimiento del artículo 10 de la Ley 34/2002, de Servicios de la Sociedad de la Información y de Comercio Electrónico (LSSI-CE), se informa de los datos del titular de este sitio web:</p>
 {TITULAR}
 <h2>Objeto</h2>
 <p>Este sitio difunde contenidos de oración, música cristiana y recursos católicos, y enlaza a plataformas externas donde se venden productos digitales (Payhip) y se gestionan aportaciones voluntarias (Stripe).</p>
 <h2>Compras y aportaciones</h2>
 <p>Las compras de productos digitales se realizan en Payhip, que actúa como plataforma de venta y gestiona el pago y, en su caso, el IVA aplicable. Al tratarse de contenido digital que se entrega de inmediato, al comprar se solicita tu consentimiento expreso y la renuncia al derecho de desistimiento, conforme al artículo 103.m) del Real Decreto Legislativo 1/2007. Las aportaciones del Círculo de Paz se gestionan con Stripe; son voluntarias, no constituyen donativos fiscalmente deducibles y pueden cancelarse en cualquier momento.</p>
 <h2>Propiedad intelectual</h2>
 <p>Los textos, la música, las imágenes y el diseño de este sitio pertenecen a Paz en Su Presencia, salvo los textos tradicionales de dominio público. Los recursos comprados son para uso personal, familiar o parroquial sin ánimo de lucro; no está permitida su reventa ni su redistribución.</p>
 <h2>Responsabilidad</h2>
 <p>El titular no se responsabiliza del contenido de los sitios externos enlazados. Los contenidos de esta web tienen finalidad devocional y no sustituyen el acompañamiento de tu parroquia ni el consejo de profesionales.</p>
 <h2>Legislación aplicable</h2>
 <p>Este sitio se rige por la legislación española. Para cualquier controversia serán competentes los juzgados y tribunales que correspondan conforme a la normativa de consumidores y usuarios.</p>
 <p class="pequeno">Última actualización: noviembre de 2026.</p>
</div></section>'''

PRIV = f'''<section class="pagina cielo"><div class="w estrecho">
 <h1>Política de privacidad</h1>
 <h2>Responsable del tratamiento</h2>
 {TITULAR}
 <h2>Qué datos tratamos y para qué</h2>
 <ul>
  <li><strong>Formulario de la novena y boletín:</strong> tu nombre (opcional) y tu correo, para enviarte la novena y, después, otros correos de oración, novedades y recursos de Paz en Su Presencia.</li>
  <li><strong>Correos que nos escribes:</strong> los datos que nos envíes, solo para responderte.</li>
  <li><strong>Compras y aportaciones:</strong> las gestionan Payhip y Stripe como responsables de su propio tratamiento; nosotros recibimos tu nombre, tu correo y los datos del pedido para entregar el producto y atenderte.</li>
 </ul>
 <h2>Base legal</h2>
 <p>Tu consentimiento, que das al marcar la casilla del formulario y confirmar tu correo (doble confirmación). Puedes retirarlo en cualquier momento con el enlace «darse de baja» que llevan todos los correos. Para las compras, la ejecución del contrato.</p>
 <h2>Cuánto tiempo los guardamos</h2>
 <p>Hasta que te des de baja o nos pidas que los borremos. Los datos de compras, el tiempo que exijan las obligaciones legales y fiscales.</p>
 <h2>Con quién se comparten</h2>
 <p>Con los proveedores que nos ayudan a prestar el servicio, con contratos que garantizan la protección de tus datos: MailerLite (envío de correos, UAB MailerLite, Lituania, UE), Payhip (venta de productos digitales), Stripe (pagos), Netlify (alojamiento web) y Cloudflare Web Analytics (estadísticas de visitas sin cookies ni datos personales, Cloudflare Inc.). Algunos pueden tratar datos fuera del Espacio Económico Europeo con las garantías previstas en el RGPD (cláusulas contractuales tipo o marco de privacidad UE-EE. UU.). No vendemos ni cedemos tus datos a nadie.</p>
 <h2>Tus derechos</h2>
 <p>Puedes pedir el acceso, la rectificación, la supresión, la oposición, la limitación o la portabilidad de tus datos escribiendo a <a href="mailto:hola@pazensupresencia.com">hola@pazensupresencia.com</a>. Si crees que no hemos atendido bien tu petición, puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>
 <p class="pequeno">Última actualización: noviembre de 2026.</p>
</div></section>'''

COOK = '''<section class="pagina cielo"><div class="w estrecho">
 <h1>Política de cookies</h1>
 <p>Esta web <strong>no usa cookies propias ni de terceros</strong> con fines de análisis o publicidad, por eso no te mostramos ningún aviso para aceptarlas.</p>
 <ul>
  <li>Las tipografías están alojadas en nuestro propio servidor.</li>
  <li>Las estadísticas de visitas se hacen con Cloudflare Web Analytics, que no usa cookies ni guarda datos personales.</li>
  <li>Los vídeos y la música no se reproducen dentro de la web: al pulsarlos se abre YouTube o Spotify, que tienen sus propias políticas.</li>
 </ul>
 <p>Si sales a otras webs desde aquí (Payhip, Stripe, YouTube, Spotify o redes sociales), esas webs pueden usar sus propias cookies, según sus políticas.</p>
 <p class="pequeno">Última actualización: noviembre de 2026.</p>
</div></section>'''

IA = '''<section class="pagina cielo"><div class="w estrecho">
 <h1>Cómo usamos la inteligencia artificial</h1>
 <p>Queremos ser transparentes contigo. En Paz en Su Presencia usamos herramientas de inteligencia artificial como ayuda en parte de nuestro trabajo:</p>
 <ul>
  <li><strong>Ilustraciones:</strong> las imágenes de nuestros vídeos y de los recursos imprimibles se crean con ayuda de IA y las revisamos una por una.</li>
  <li><strong>Música:</strong> parte de las canciones se producen con herramientas de IA a partir de letras y temas elegidos por nosotros.</li>
  <li><strong>Textos:</strong> las oraciones y los materiales los escribimos y revisamos nosotros. Los pasajes bíblicos aparecen parafraseados; para el texto exacto, consulta una Biblia aprobada por la Iglesia.</li>
 </ul>
 <p>En YouTube marcamos el contenido generado o alterado con IA cuando corresponde. La IA es una herramienta: la fe, la intención y el cuidado los ponemos nosotros.</p>
</div></section>'''

