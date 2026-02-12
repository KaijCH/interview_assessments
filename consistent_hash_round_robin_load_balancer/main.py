from consistent_hash_round_robin_balancer import TrafficBalancer, Backend, Pod, RequestInstance


def main() -> None:

    backend1, backend2 = Backend("localhost", 80, True), Backend("localhost", 140, False)
    
    backends = [backend1, backend2]
    
    traffic_balancer = TrafficBalancer(backends)

    request1 = RequestInstance("9f1bcb3c-2f74-42b3-bb12-5e26b7c3d821")

    assert traffic_balancer.serve_request(request1) == backend1, "failure in serve request with single available backend"

    backend2.flip_availability()

    backend1.flip_availability()

    assert traffic_balancer.serve_request(request1) == backend2, "failure in serve request with single available backend"

    print("overall success")

    




if __name__ == "__main__":
    main()