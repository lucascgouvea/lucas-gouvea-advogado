/**
 * SCRIPT.JS - LUCAS GOUVEA ADVOGADO
 * Interações dinâmicas, validação e efeitos do website jurídico premium
 */

document.addEventListener('DOMContentLoaded', () => {
    // Inicialização do Lucide Icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    // Inicialização do AOS (Animate on Scroll)
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-out-cubic',
            once: true,
            offset: 50
        });
    }

    /* ==========================================================================
       1. TEMA CLARO (FIXO)
       ========================================================================== */
    // Forçar sempre tema claro e limpar qualquer preferência salva
    document.body.classList.remove('dark-mode');
    document.body.classList.add('light-mode');
    localStorage.removeItem('theme');

    /* ==========================================================================
       2. SCROLL HEADER EFFECT
       ========================================================================== */
    const header = document.querySelector('.main-header');
    
    const handleScrollHeader = () => {
        if (!header) return;
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    };
    
    window.addEventListener('scroll', handleScrollHeader);
    handleScrollHeader(); // Executar uma vez no carregamento inicial

    /* ==========================================================================
       3. MENU RESPONSIVO (DRAWER)
       ========================================================================== */
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const mobileDrawer = document.querySelector('.mobile-drawer');
    const drawerOverlay = document.querySelector('.drawer-overlay');
    const drawerCloseBtn = document.querySelector('.drawer-close');
    const drawerLinks = document.querySelectorAll('.drawer-link');

    const openDrawer = () => {
        mobileMenuToggle.classList.add('active');
        mobileDrawer.classList.add('active');
        if (drawerOverlay) drawerOverlay.classList.add('active');
        document.body.style.overflow = 'hidden'; // Evita scroll de fundo
        mobileMenuToggle.setAttribute('aria-expanded', 'true');
    };

    const closeDrawer = () => {
        mobileMenuToggle.classList.remove('active');
        mobileDrawer.classList.remove('active');
        if (drawerOverlay) {
            drawerOverlay.classList.add('active');
            // Remover classe de fade out
            setTimeout(() => {
                drawerOverlay.classList.remove('active');
            }, 100);
        }
        document.body.style.overflow = '';
        mobileMenuToggle.setAttribute('aria-expanded', 'false');
    };

    if (mobileMenuToggle && mobileDrawer) {
        mobileMenuToggle.addEventListener('click', () => {
            if (mobileDrawer.classList.contains('active')) {
                closeDrawer();
            } else {
                openDrawer();
            }
        });

        if (drawerCloseBtn) drawerCloseBtn.addEventListener('click', closeDrawer);
        if (drawerOverlay) drawerOverlay.addEventListener('click', closeDrawer);

        // Fechar drawer ao clicar em links
        drawerLinks.forEach(link => {
            link.addEventListener('click', closeDrawer);
        });
    }

    /* ==========================================================================
       4. ANIMAR NÚMEROS (SEÇÃO DE AUTORIDADE)
       ========================================================================== */
    const statsSection = document.querySelector('.stats-section');
    const statNumbers = document.querySelectorAll('.stat-number');
    let animated = false;

    const animateCounters = () => {
        statNumbers.forEach(statNumber => {
            const target = parseInt(statNumber.getAttribute('data-target'), 10);
            let count = 0;
            const duration = 2000; // 2 segundos
            const increment = target / (duration / 16); // ~60fps

            const updateCount = () => {
                count += increment;
                if (count < target) {
                    statNumber.innerText = `+${Math.floor(count)}`;
                    requestAnimationFrame(updateCount);
                } else {
                    statNumber.innerText = `+${target.toLocaleString('pt-BR')}`;
                }
            };
            updateCount();
        });
    };

    // Usar Intersection Observer para ativar ao rolar até a seção
    if (statsSection && statNumbers.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !animated) {
                    animateCounters();
                    animated = true;
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        observer.observe(statsSection);
    }

    /* ==========================================================================
       5. ACORDEÃO DO FAQ
       ========================================================================== */
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
        const trigger = item.querySelector('.faq-trigger');
        const content = item.querySelector('.faq-content');
        if (!trigger || !content) return; // páginas com <details> nativo dispensam o acordeão

        trigger.addEventListener('click', () => {
            const isActive = item.classList.contains('active');

            // Fechar todos os outros FAQs para manter o acordeão limpo e minimalista
            faqItems.forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove('active');
                    otherItem.querySelector('.faq-content').style.maxHeight = null;
                    otherItem.querySelector('.faq-trigger').setAttribute('aria-expanded', 'false');
                }
            });

            // Toggle item clicado
            if (isActive) {
                item.classList.remove('active');
                content.style.maxHeight = null;
                trigger.setAttribute('aria-expanded', 'false');
            } else {
                item.classList.add('active');
                content.style.maxHeight = content.scrollHeight + 'px';
                trigger.setAttribute('aria-expanded', 'true');
            }
        });
    });

    /* ==========================================================================
       6. CARROSSEL DE DEPOIMENTOS
       ========================================================================== */
    const track = document.querySelector('.carousel-track');
    const slides = Array.from(document.querySelectorAll('.testimonial-slide'));
    const nextBtn = document.querySelector('.carousel-btn.next');
    const prevBtn = document.querySelector('.carousel-btn.prev');
    const dotsContainer = document.querySelector('.carousel-dots');

    if (track && slides.length > 0) {
        let currentIndex = 0;
        let autoplayTimer = null;

        // Criar os indicadores (dots) dinamicamente
        slides.forEach((_, index) => {
            const dot = document.createElement('div');
            dot.classList.add('dot');
            if (index === 0) dot.classList.add('active');
            dot.addEventListener('click', () => {
                goToSlide(index);
                resetAutoplay();
            });
            dotsContainer.appendChild(dot);
        });

        const dots = Array.from(dotsContainer.querySelectorAll('.dot'));

        const updateDots = (index) => {
            dots.forEach(dot => dot.classList.remove('active'));
            dots[index].classList.add('active');
        };

        const goToSlide = (index) => {
            currentIndex = index;
            if (currentIndex < 0) currentIndex = slides.length - 1;
            if (currentIndex >= slides.length) currentIndex = 0;

            track.style.transform = `translateX(-${currentIndex * 100}%)`;
            updateDots(currentIndex);
        };

        const startAutoplay = () => {
            autoplayTimer = setInterval(() => {
                goToSlide(currentIndex + 1);
            }, 6000); // 6 segundos por depoimento
        };

        const resetAutoplay = () => {
            clearInterval(autoplayTimer);
            startAutoplay();
        };

        nextBtn.addEventListener('click', () => {
            goToSlide(currentIndex + 1);
            resetAutoplay();
        });

        prevBtn.addEventListener('click', () => {
            goToSlide(currentIndex - 1);
            resetAutoplay();
        });

        // Iniciar Autoplay
        startAutoplay();

        // Parar autoplay quando mouse entra
        track.addEventListener('mouseenter', () => clearInterval(autoplayTimer));
        track.addEventListener('mouseleave', startAutoplay);
    }

    /* ==========================================================================
       7. BOTÃO VOLTAR AO TOPO
       ========================================================================== */
    const backToTopBtn = document.getElementById('back-to-top');

    if (backToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 400) {
                backToTopBtn.classList.add('visible');
            } else {
                backToTopBtn.classList.remove('visible');
            }
        });

        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    /* ==========================================================================
       8. VALIDAÇÃO DO FORMULÁRIO DE CONTATO
       ========================================================================== */
    const contactForm = document.getElementById('legal-contact-form');

    if (contactForm) {
        // Formatar Telefone automaticamente: (XX) XXXXX-XXXX ou (XX) XXXX-XXXX
        const phoneInput = document.getElementById('form-phone');
        
        phoneInput.addEventListener('input', (e) => {
            let x = e.target.value.replace(/\D/g, '').match(/(\d{0,2})(\d{0,5})(\d{0,4})/);
            e.target.value = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] + (x[3] ? '-' + x[3] : '');
        });

        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            let isValid = true;
            
            // Validar Nome
            const nameInput = document.getElementById('form-name');
            const nameVal = nameInput.value.trim();
            const groupName = nameInput.closest('.form-group');
            if (nameVal.length < 3) {
                groupName.classList.add('has-error');
                isValid = false;
            } else {
                groupName.classList.remove('has-error');
            }

            // Validar E-mail
            const emailInput = document.getElementById('form-email');
            const emailVal = emailInput.value.trim();
            const groupEmail = emailInput.closest('.form-group');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(emailVal)) {
                groupEmail.classList.add('has-error');
                isValid = false;
            } else {
                groupEmail.classList.remove('has-error');
            }

            // Validar Telefone
            const phoneVal = phoneInput.value.trim();
            const groupPhone = phoneInput.closest('.form-group');
            // Remove parênteses, traços e espaços para contar dígitos
            const digits = phoneVal.replace(/\D/g, '');
            if (digits.length < 10 || digits.length > 11) {
                groupPhone.classList.add('has-error');
                isValid = false;
            } else {
                groupPhone.classList.remove('has-error');
            }

            // Validar Área de Interesse
            const areaInput = document.getElementById('form-area');
            const groupArea = areaInput.closest('.form-group');
            if (areaInput.value === "") {
                groupArea.classList.add('has-error');
                isValid = false;
            } else {
                groupArea.classList.remove('has-error');
            }

            // Validar Mensagem
            const messageInput = document.getElementById('form-message');
            const messageVal = messageInput.value.trim();
            const groupMessage = messageInput.closest('.form-group');
            if (messageVal.length < 10) {
                groupMessage.classList.add('has-error');
                isValid = false;
            } else {
                groupMessage.classList.remove('has-error');
            }

            // Se for válido, enviar formulário
            if (isValid) {
                const submitBtn = contactForm.querySelector('.btn-submit');
                const submitText = submitBtn.querySelector('.submit-text');
                const successBanner = document.getElementById('form-success-banner');

                submitBtn.classList.add('loading');
                submitText.innerText = 'Verificando E-mail...';

                // Passo 1: Verificação do e-mail (ZeroBounce) pela função interna /api/validate-email,
                // que guarda a chave do serviço fora do código do site
                fetch(`/api/validate-email?email=${encodeURIComponent(emailVal)}`)
                    .then(response => response.json())
                    .then(data => {
                        // Aceitar 'valid', 'catch-all', 'unknown' (para não bloquear falsos positivos)
                        // Bloquear 'invalid', 'spamtrap', 'abuse', 'do_not_mail'
                        const blockStatuses = ['invalid', 'spamtrap', 'abuse', 'do_not_mail'];
                        
                        if (data.status && blockStatuses.includes(data.status)) {
                            // E-mail inválido
                            submitBtn.classList.remove('loading');
                            submitText.innerText = 'Enviar Mensagem';
                            groupEmail.classList.add('has-error');
                            alert("Este e-mail não parece ser válido ou está desativado. Por favor, verifique ou tente outro.");
                            return; // Interrompe o envio
                        }
                        
                        // Passo 2: Se passou pelo ZeroBounce (ou deu status incerto), enviar via Web3Forms
                        submitText.innerText = 'Enviando...';
                        const formData = new FormData(contactForm);
                        const object = Object.fromEntries(formData);
                        const json = JSON.stringify(object);

                        return fetch('https://api.web3forms.com/submit', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                'Accept': 'application/json'
                            },
                            body: json
                        })
                        .then(async (response) => {
                            let res = await response.json();
                            if (response.status == 200) {
                                // Exibir sucesso e limpar formulário
                                successBanner.style.display = 'flex';
                                contactForm.reset();
                                if (typeof gtag === 'function') {
                                    gtag('event', 'generate_lead', { method: 'formulario', page_path: location.pathname });
                                }
                                
                                // Rolar suavemente até o banner de sucesso
                                successBanner.scrollIntoView({ behavior: 'smooth', block: 'center' });

                                // Ocultar banner de sucesso após 8 segundos
                                setTimeout(() => {
                                    successBanner.style.display = 'none';
                                }, 8000);
                            } else {
                                console.log(res);
                                alert("Ocorreu um erro ao enviar sua mensagem. Por favor, tente novamente.");
                            }
                        });
                    })
                    .catch(error => {
                        console.log("Erro na validação ou envio:", error);
                        alert("Ocorreu um erro de rede. Verifique sua conexão e tente novamente.");
                    })
                    .finally(() => {
                        submitBtn.classList.remove('loading');
                        submitText.innerText = 'Enviar Mensagem';
                    });
            }
        });
    }
});

/* ==========================================================================
   9. MEDIÇÃO DE CONTATOS (GA4)
   Registra cliques em links de WhatsApp e de e-mail em qualquer página.
   ========================================================================== */
document.addEventListener('click', (e) => {
    const link = e.target.closest ? e.target.closest('a[href]') : null;
    if (!link || typeof gtag !== 'function') return;

    const href = link.getAttribute('href') || '';
    let eventName = null;
    if (/wa\.me|api\.whatsapp\.com/i.test(href)) eventName = 'whatsapp_click';
    else if (href.indexOf('mailto:') === 0) eventName = 'email_click';
    // chamadas dos artigos para a página de área ou para o formulário de contato
    else if (link.closest('.article-body') && /direito-[a-z-]+-sao-carlos\/|#contato|#como-funciona|#atuacao/.test(href)) eventName = 'cta_interno_click';
    if (!eventName) return;

    const area = link.closest('section, header, footer, nav, aside, article');
    const position = area ? (area.id || (area.className || '').toString().split(' ')[0] || area.tagName.toLowerCase()) : 'outro';
    const label = (link.textContent || '').replace(/\s+/g, ' ').trim() || link.getAttribute('aria-label') || '';

    gtag('event', eventName, {
        page_path: location.pathname,
        link_position: position,
        link_text: label.slice(0, 80),
        link_url: href.split('?')[0].slice(0, 120),
        transport_type: 'beacon'
    });
});


/* ==========================================================================
   10. CONTATO PELO WHATSAPP
   Botão flutuante que abre uma janela no estilo de chat (só quando a pessoa
   clica), com escolha de assunto, e chamada no meio dos artigos.
   O clique final é medido pelo bloco 9 (whatsapp_click) e o assunto escolhido
   pelo evento whatsapp_chat_assunto.
   ========================================================================== */
(function () {
    var NUMERO = '5516936180178';
    var ASSUNTOS = ['Consignado e bancos', 'Imóveis e aluguel', 'Plano de saúde', 'Direito do consumidor', 'Divórcio e união estável', 'Outro assunto'];
    var ICONE = '<svg class="whatsapp-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.26-.46-2.4-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.07c.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.18-1.42-.08-.12-.27-.2-.57-.35zM12.05 21.8h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.9-9.88 2.64 0 5.12 1.03 6.99 2.9a9.82 9.82 0 0 1 2.9 6.99c0 5.45-4.44 9.88-9.9 9.88zM20.52 3.45A11.82 11.82 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.68 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.17-3.42-8.46z"/></svg>';

    function linkWhats(msg) { return 'https://wa.me/' + NUMERO + '?text=' + encodeURIComponent(msg); }
    function guardado(chave, valor) {
        try {
            if (valor === undefined) return sessionStorage.getItem(chave);
            sessionStorage.setItem(chave, valor);
        } catch (e) { return null; }
    }

    function montar() {
        var h1 = document.querySelector('h1.article-title');
        var artigo = h1 ? h1.textContent.replace(/\s+/g, ' ').trim() : '';
        var abertura = artigo
            ? 'Olá, estou lendo o artigo "' + artigo + '" no site.'
            : 'Olá, vim pelo site lgouvea.com.';

        /* chamada no meio dos artigos */
        var corpo = document.querySelector('.article-body');
        if (corpo && !corpo.querySelector('.article-cta-inline')) {
            var h2s = Array.prototype.filter.call(corpo.querySelectorAll('h2'), function (h) { return !h.closest('.article-cta'); });
            if (h2s.length >= 4) {
                var alvo = h2s[Math.ceil(h2s.length / 2)];
                var box = document.createElement('aside');
                box.className = 'article-cta-inline';
                box.innerHTML = '<p><strong>Está passando por essa situação?</strong> O escritório pode analisar os documentos do seu caso.</p>' +
                    '<a class="btn btn-outline" target="_blank" rel="noopener noreferrer" href="' + linkWhats(abertura + ' Gostaria de uma orientação.') + '">Falar pelo WhatsApp</a>';
                alvo.parentNode.insertBefore(box, alvo);
            }
        }

        if (document.querySelector('.wa-chat')) return;

        var raiz = document.createElement('div');
        raiz.className = 'wa-chat';
        var chips = '';
        ASSUNTOS.forEach(function (a) { chips += '<button type="button" class="wa-chat-chip" aria-pressed="false">' + a + '</button>'; });
        raiz.innerHTML =
            '<div class="wa-chat-panel" id="wa-chat-panel" role="dialog" aria-label="Falar com o escritório pelo WhatsApp" hidden>' +
                '<div class="wa-chat-header">' +
                    '<span class="wa-chat-avatar" aria-hidden="true">LG</span>' +
                    '<span class="wa-chat-id"><strong>Lucas Gouvea Advogado</strong><small>Atendimento pelo WhatsApp</small></span>' +
                    '<button type="button" class="wa-chat-close" aria-label="Fechar">&times;</button>' +
                '</div>' +
                '<div class="wa-chat-body">' +
                    '<p class="wa-chat-bubble">Olá! Sobre qual assunto você quer falar?</p>' +
                    '<div class="wa-chat-chips">' + chips + '</div>' +
                    '<label class="wa-chat-label" for="wa-chat-texto">Se quiser, conte em poucas palavras (opcional)</label>' +
                    '<textarea id="wa-chat-texto" class="wa-chat-texto" rows="2" maxlength="400"></textarea>' +
                '</div>' +
                '<div class="wa-chat-footer">' +
                    '<a class="wa-chat-enviar" target="_blank" rel="noopener noreferrer" href="#">' + ICONE + 'Continuar no WhatsApp</a>' +
                    '<small>A conversa continua no aplicativo do WhatsApp.</small>' +
                '</div>' +
            '</div>' +
            '<div class="wa-chat-teaser" hidden><span>Fale com o escritório</span><button type="button" aria-label="Dispensar">&times;</button></div>' +
            '<button type="button" class="whatsapp-float" aria-label="Falar pelo WhatsApp" aria-expanded="false" aria-controls="wa-chat-panel">' + ICONE + '</button>';
        document.body.appendChild(raiz);

        var painel = raiz.querySelector('.wa-chat-panel');
        var botao = raiz.querySelector('.whatsapp-float');
        var teaser = raiz.querySelector('.wa-chat-teaser');
        var texto = raiz.querySelector('.wa-chat-texto');
        var enviar = raiz.querySelector('.wa-chat-enviar');
        var assunto = '';

        function atualizar() {
            var msg = abertura;
            if (assunto) msg += ' Assunto: ' + assunto + '.';
            var extra = texto.value.replace(/\s+/g, ' ').trim();
            msg += extra ? ' ' + extra : ' Gostaria de uma orientação.';
            enviar.href = linkWhats(msg);
        }
        function abrir(sim) {
            painel.hidden = !sim;
            raiz.classList.toggle('aberto', sim);
            botao.setAttribute('aria-expanded', sim ? 'true' : 'false');
            teaser.hidden = true;
            if (sim) {
                guardado('waTeaser', '1');
                if (typeof gtag === 'function') gtag('event', 'whatsapp_chat_aberto', { page_path: location.pathname });
            }
        }

        botao.addEventListener('click', function () { abrir(painel.hidden); });
        raiz.querySelector('.wa-chat-close').addEventListener('click', function () { abrir(false); botao.focus(); });
        document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !painel.hidden) { abrir(false); botao.focus(); } });
        raiz.querySelectorAll('.wa-chat-chip').forEach(function (chip) {
            chip.addEventListener('click', function () {
                raiz.querySelectorAll('.wa-chat-chip').forEach(function (c) { c.classList.remove('ativo'); c.setAttribute('aria-pressed', 'false'); });
                chip.classList.add('ativo');
                chip.setAttribute('aria-pressed', 'true');
                assunto = chip.textContent;
                atualizar();
            });
        });
        texto.addEventListener('input', atualizar);
        enviar.addEventListener('click', function () {
            if (typeof gtag === 'function') gtag('event', 'whatsapp_chat_assunto', { assunto: assunto || 'não informado', page_path: location.pathname });
        });
        atualizar();

        /* aviso discreto, só em telas grandes e uma vez por visita */
        teaser.querySelector('span').addEventListener('click', function () { abrir(true); });
        teaser.querySelector('button').addEventListener('click', function () { teaser.hidden = true; guardado('waTeaser', '1'); });
        if (window.matchMedia && window.matchMedia('(min-width: 1024px)').matches && !guardado('waTeaser')) {
            setTimeout(function () { if (painel.hidden) teaser.hidden = false; }, 8000);
        }
    }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', montar);
    else montar();
})();
