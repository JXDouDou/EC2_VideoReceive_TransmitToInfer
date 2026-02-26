# Distributed AI Control System

## Architecture

Edge → EC2 API Server → 5080 AI Server → EC2 → Edge

Control Plane: api-server (EC2)
Compute Plane: ai-server (RTX 5080)

---

## Responsibilities

### api-server
- Receive Edge data (WebSocket / WebRTC)
- Forward inference request to AI server
- Display frontend data
- Send control commands to Edge
- No GPU logic allowed

### ai-server
- Load model
- Perform GPU inference
- Return prediction results
- No frontend or business logic allowed

---

## Communication

- EC2 and 5080 connected via private network (Tailscale)
- API Server calls AI Server via WS (future: maybe gRPC)
- WebSocket used for streaming

---

## Design Constraints

- Strict separation of concerns
- Async implementation in api-server
- InferenceClient is the only gateway to AI server
- Must remain scalable for multi-GPU

---

## Folder Structure

video-system/
├── api-server/
├── ai-server/
└── docker-compose.yml