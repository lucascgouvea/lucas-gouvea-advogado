// Confere o e-mail do formulário de contato no ZeroBounce sem expor a chave no navegador.
// A chave fica na variável de ambiente ZEROBOUNCE_API_KEY
// (Vercel > projeto > Settings > Environment Variables).
//
// Em qualquer falha (chave ausente, serviço fora do ar, resposta inesperada) a função
// responde "unknown", e o formulário segue com o envio, como já acontecia antes.

const ALLOWED_HOSTS = /(^|\.)lgouvea\.com$|\.vercel\.app$/;

function sameSite(req) {
  const from = req.headers.origin || req.headers.referer || '';
  try {
    return ALLOWED_HOSTS.test(new URL(from).hostname);
  } catch (e) {
    return false;
  }
}

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');

  const key = process.env.ZEROBOUNCE_API_KEY;
  const email = String((req.query && req.query.email) || '').trim();
  const emailOk = email.length <= 254 && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

  if (req.method !== 'GET' || !key || !emailOk || !sameSite(req)) {
    return res.status(200).json({ status: 'unknown' });
  }

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 8000);

  try {
    const url = 'https://api.zerobounce.net/v2/validate?api_key=' + encodeURIComponent(key) +
      '&email=' + encodeURIComponent(email);
    const response = await fetch(url, { signal: controller.signal });
    const data = await response.json();
    return res.status(200).json({ status: typeof data.status === 'string' ? data.status : 'unknown' });
  } catch (e) {
    return res.status(200).json({ status: 'unknown' });
  } finally {
    clearTimeout(timer);
  }
};
