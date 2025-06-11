from network_peer import NetworkServer


def main() -> None:
    na = NetworkServer.seed_chunks('A', [1,2])
    nb = NetworkServer.seed_chunks('B', [])
    nc = NetworkServer.seed_chunks('C', [3,4])
    nd = NetworkServer.seed_chunks('D', [])

    na.complete_chunk_transaction('B',1)
    na.complete_chunk_transaction('B',2)
    na.complete_chunk_transaction('C',1)

    nc.complete_chunk_transaction('D',4)
    nc.complete_chunk_transaction('B',3)

    nb.complete_chunk_transaction('D',3)
    nd.complete_chunk_transaction('A',3)

    res = NetworkServer.rank_peers()
    assert res == ['C','A','B','D'], "failue in providing peer rank list"

    print("overall success")


if __name__ == "__main__":
    main()