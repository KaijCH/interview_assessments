from network_peer import NetworkServer


def main() -> None:
    npa = NetworkServer.seed_chunks('A', [1,2])
    npb = NetworkServer.seed_chunks('B', [])
    npc = NetworkServer.seed_chunks('C', [3,4])
    npd = NetworkServer.seed_chunks('D', [])

    npa.complete_chunk_transaction('B',1)
    npa.complete_chunk_transaction('B',2)
    npa.complete_chunk_transaction('C',1)

    npc.complete_chunk_transaction('D',4)
    npc.complete_chunk_transaction('B',3)

    npb.complete_chunk_transaction('D',3)
    npd.complete_chunk_transaction('A',3)

    res = NetworkServer.rank_peers()
    assert res == ['C','A','B','D'], "failue in providing peer rank list"

    print("overall success")


if __name__ == "__main__":
    main()