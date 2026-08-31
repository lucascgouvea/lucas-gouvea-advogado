document.addEventListener("DOMContentLoaded", () => {
    const metaTag = document.querySelector('meta[name="last-verified"]');
    if (metaTag) {
        const rawDate = metaTag.getAttribute("content");
        if (rawDate) {
            const dateObj = new Date(rawDate + "T00:00:00");
            const options = { day: 'numeric', month: 'long', year: 'numeric' };
            const formattedDate = dateObj.toLocaleDateString('pt-BR', options);
            
            const metaContainer = document.querySelector('.article-meta');
            if (metaContainer) {
                const checkIcon = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>';
                const verifiedDiv = document.createElement('div');
                verifiedDiv.className = 'article-meta-item';
                verifiedDiv.innerHTML = `${checkIcon} Fontes verificadas em: ${formattedDate}`;
                
                // Inserir antes da categoria (que geralmente tem margin-left:auto)
                const categoryItem = metaContainer.querySelector('.article-meta-item:last-child');
                metaContainer.insertBefore(verifiedDiv, categoryItem);
            }
        }
    }
});
