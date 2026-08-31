class BlogList extends HTMLElement {
    connectedCallback() {
        this.render();
    }

    render() {
        // Sort by date descending
        const sortedPosts = blogPosts.sort((a, b) => new Date(b.date) - new Date(a.date));

        let html = '';
        sortedPosts.forEach((post, index) => {
            const delay = (index + 1) * 50;
            html += `
                <article class="a-card" data-aos="fade-up" data-aos-delay="${delay}">
                    <div class="a-card-banner ${post.iconClass}">
                        <div class="a-card-banner-icon">
                            ${post.svgIcon}
                        </div>
                        <div class="a-card-banner-bottom">
                            <span class="a-card-category">
                                ${post.svgIcon.replace('stroke-width="1.2"', 'stroke-width="2"')}
                                ${post.category}
                            </span>
                        </div>
                    </div>
                    <div class="a-card-body">
                        <h2 class="a-card-title">
                            <a href="${post.url}">${post.title}</a>
                        </h2>
                        <p class="a-card-excerpt">${post.excerpt}</p>
                        <div class="a-card-footer">
                            <div class="a-card-meta">
                                <span>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                                    ${post.dateDisplay}
                                </span>
                                <span>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                                    ${post.readTime}
                                </span>
                            </div>
                            <a href="${post.url}" class="a-card-read">
                                Ler artigo
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
                            </a>
                        </div>
                    </div>
                </article>
            `;
        });

        this.innerHTML = html;
        this.className = "articles-grid";
    }
}

customElements.define('blog-list', BlogList);
