class AuthorBlock extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
            <div class="author-block" style="background: var(--bg-light); padding: 30px; border-radius: 8px; margin-top: 40px; margin-bottom: 20px; border: 1px solid var(--border-color);">
                <h3 style="margin-top: 0; font-family: var(--font-serif); font-size: 1.4rem; color: var(--primary-color);">Sobre o autor</h3>
                <p style="margin-bottom: 0; font-size: 1rem; color: var(--text-color); line-height: 1.6;">Lucas Gouvea é advogado, graduado em Direito pela PUC Campinas e pós-graduado em Direito Público, Constitucional e Tributário pela PUC Rio Grande do Sul. Atua em Direito Bancário, Cível, Médico e Imobiliário, com escritório em São Carlos/SP e atendimento digital em todo o Brasil.</p>
            </div>
        `;
    }
}
customElements.define('author-block', AuthorBlock);
