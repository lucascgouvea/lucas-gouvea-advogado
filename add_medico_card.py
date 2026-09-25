import re

with open("index.html", "r") as f:
    html = f.read()

# I will find the end of the Direito Cível card.
# Looking for `<div class="service-card" data-aos="fade-up" data-aos-delay="300">` and its closing `</div>`.
start_idx = html.find('<!-- Direito Cível -->')
if start_idx == -1:
    print("Could not find Direito Cível")
    exit(1)

# we know the structure is inside <div class="services-grid">
# the next tag after the Cível card is `</div>` closing the services-grid.
# Let's search for "<!-- Por que nos escolher -->" or similar section
end_card_idx = html.find('<!-- /Direito Cível -->') # we don't have this comment, let's search for the next section

lucide_heart = """<!-- @license lucide-static v1.47.0 - ISC -->
<svg class="lucide lucide-heart-pulse" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>
  <path d="M3.22 12H9.5l.5-1 2 4.5 2-7 1.5 3.5h5.27"/>
</svg>"""

lucide_check = """<!-- @license lucide-static v1.47.0 - ISC -->
<svg class="lucide lucide-check" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5" /></svg>"""

medico_card = f"""
                    <!-- Direito Médico -->
                    <div class="service-card" data-aos="fade-up" data-aos-delay="400">
                        <div class="service-card-decor"></div>
                        <div class="service-icon-box">
                            {lucide_heart}
                        </div>
                        <h3 class="service-title">Direito Médico</h3>
                        <p class="service-description">Atuação focada na defesa de pacientes vítimas de erro médico, negativas de cobertura por planos de saúde, reajustes abusivos e fornecimento de medicamentos.</p>
                        <ul class="service-bullets">
                            <li>{lucide_check} Reparação por Erro Médico e Odontológico</li>
                            <li>{lucide_check} Negativas de Tratamento e Cirurgia</li>
                            <li>{lucide_check} Liminares contra Planos de Saúde</li>
                        </ul>
                    </div>
"""

# I need to insert this right before the closing </div> of <div class="services-grid">
grid_start = html.find('<div class="services-grid">')
# the grid ends before:
#                </div>
#            </div>
#        </section>
#        <!-- Por que escolher -->

# We can find the closing div of the Cível card. Let's find the closing ul:
ul_close = html.find('</ul>', start_idx)
div_close = html.find('</div>', ul_close)

# Wait, Cível doesn't have a `</a>` it has `</div>`. So right after `</div>` of Cível.
insert_pos = div_close + len('</div>')

html = html[:insert_pos] + "\n" + medico_card + html[insert_pos:]

with open("index.html", "w") as f:
    f.write(html)
