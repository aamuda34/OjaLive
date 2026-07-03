export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname === '/api/remove-background' && request.method === 'POST') {
      try {
        const incomingForm = await request.formData();
        const imageFile = incomingForm.get('image');

        if (!imageFile) {
          return new Response(JSON.stringify({ error: 'No image provided' }), {
            status: 400,
            headers: { 'Content-Type': 'application/json' }
          });
        }

        const photoroomForm = new FormData();
        photoroomForm.append('image_file', imageFile);

        const prResponse = await fetch('https://sdk.photoroom.com/v1/segment', {
          method: 'POST',
          headers: {
            'x-api-key': env.PHOTOROOM_API_KEY
          },
          body: photoroomForm
        });

        if (!prResponse.ok) {
          const errText = await prResponse.text();
          return new Response(JSON.stringify({ error: 'PhotoRoom API error', detail: errText }), {
            status: prResponse.status,
            headers: { 'Content-Type': 'application/json' }
          });
        }

        const imageBuffer = await prResponse.arrayBuffer();
        return new Response(imageBuffer, {
          headers: { 'Content-Type': 'image/png' }
        });

      } catch (err) {
        return new Response(JSON.stringify({ error: 'Server error', detail: err.message }), {
          status: 500,
          headers: { 'Content-Type': 'application/json' }
        });
      }
    }

    return env.ASSETS.fetch(request);
  }
};
