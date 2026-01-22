# ---------- Build stage ----------
FROM gcc:13-bookworm AS builder

WORKDIR /app

RUN apt-get update && \
    apt-get install -y cmake && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN cmake -S . -B build -DCMAKE_BUILD_TYPE=Release && \
    cmake --build build

# ---------- Runtime stage ----------
FROM debian:bookworm-slim

WORKDIR /app

# Install runtime libstdc++
RUN apt-get update && \
    apt-get install -y libstdc++6 && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/build/simple-cpp .

CMD ["./simple-cpp"]
