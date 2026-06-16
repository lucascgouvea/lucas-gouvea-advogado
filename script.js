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
        drawerOverlay.classList.add('active');
        document.body.style.overflow = 'hidden'; // Evita scroll de fundo
        mobileMenuToggle.setAttribute('aria-expanded', 'true');
    };

    const closeDrawer = () => {
        mobileMenuToggle.classList.remove('active');
        mobileDrawer.classList.remove('active');
        drawerOverlay.classList.add('active');
        // Remover classe de fade out
        setTimeout(() => {
            drawerOverlay.classList.remove('active');
        }, 100);
        document.body.style.overflow = '';
        mobileMenuToggle.setAttribute('aria-expanded', 'false');
    };

    mobileMenuToggle.addEventListener('click', () => {
        if (mobileDrawer.classList.contains('active')) {
            closeDrawer();
        } else {
            openDrawer();
        }
    });

    drawerCloseBtn.addEventListener('click', closeDrawer);
    drawerOverlay.addEventListener('click', closeDrawer);

    // Fechar drawer ao clicar em links
    drawerLinks.forEach(link => {
        link.addEventListener('click', closeDrawer);
    });

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

            // Se for válido, enviar formulário via API real (Web3Forms)
            if (isValid) {
                const submitBtn = contactForm.querySelector('.btn-submit');
                const submitText = submitBtn.querySelector('.submit-text');
                const successBanner = document.getElementById('form-success-banner');

                submitBtn.classList.add('loading');
                submitText.innerText = 'Enviando...';

                const formData = new FormData(contactForm);
                const object = Object.fromEntries(formData);
                const json = JSON.stringify(object);

                fetch('https://api.web3forms.com/submit', {
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
                })
                .catch(error => {
                    console.log(error);
                    alert("Ocorreu um erro de rede. Verifique sua conexão e tente novamente.");
                })
                .then(() => {
                    submitBtn.classList.remove('loading');
                    submitText.innerText = 'Solicitar atendimento';
                });
            }
        });
    }
});
