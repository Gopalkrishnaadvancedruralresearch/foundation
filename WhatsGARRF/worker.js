// Cloudflare Worker for WhataGARRF Signaling & Access Control
import directory from './directory.json';

const activeCalls = new Map(); // Tracks busy lines

addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
  const url = new URL(request.url);

  // Handle WebSocket Signaling Connection
  if (url.pathname === '/ws') {
    if (request.headers.get('Upgrade') !== 'websocket') {
      return new Response('Expected WebSocket', { status: 426 });
    }
    const pair = new WebSocketPair();
    [client, server] = Object.values(pair);
    handleWebSocketSession(server);
    return new Response(null, { status: 101, webSocket: client });
  }

  // Handle Number Verification & Routing Check
  if (url.pathname === '/api/verify') {
    const targetNumber = url.searchParams.get('number');
    const isInternalUser = request.headers.get('X-WhataGARRF-Auth') === 'authorized_113';

    if (!directory.registry[targetNumber]) {
      return Response.json({ status: 'error', message: 'Number not found' }, { status: 404 });
    }

    const entry = directory.registry[targetNumber];

    // Access Control Check
    if (entry.type === 'restricted_113' && !isInternalUser) {
      return Response.json({ 
        status: 'blocked', 
        message: 'Call failed: Private internal extension restricted to authorized staff.' 
      }, { status: 403 });
    }

    // Check if line is busy
    if (activeCalls.has(targetNumber)) {
      return Response.json({ status: 'busy', message: 'Try later, line is busy.' });
    }

    return Response.json({ status: 'allowed', routing: entry.type });
  }

  return new Response('WhataGARRF Secure Signaling Server Active', { status: 200 });
}

function handleWebSocketSession(ws) {
  ws.accept();
  ws.addEventListener('message', event => {
    try {
      const data = JSON.parse(event.data);
      // Relay WebRTC SDP offer/answer/ICE candidates peer-to-peer
      if (data.targetPeer && data.signal) {
        // Forward signal to target peer via registered socket
        broadcastToPeer(data.targetPeer, data.signal);
      }
    } catch (e) {
      ws.send(JSON.stringify({ error: 'Invalid signal packet' }));
    }
  });

  ws.addEventListener('close', () => {
    // Cleanup active call states on disconnect
  });
}

function broadcastToPeer(peerId, signal) {
  // Implementation for routing signaling payload between connected browsers
}
