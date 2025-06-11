class NetworkPeer:

    def __init__(self, peer_id: str, chunk_ids: list) -> None:
        self.chunk_ids = chunk_ids
        self.peer_id = peer_id

    def complete_chunk_transaction(self, receiver_id, chunk_id) -> None:
        """
            calls whenever peer instance finishes transmission
            do not interfere
        
        """
        NetworkServer.record_chunk_transaction(self.peer_id, receiver_id, chunk_id)

    def __repr__(self) -> str:
        return "("+ self.peer_id + str(self.chunk_ids) + ")"
    

import collections


class NetworkServer:
    
    records = collections.defaultdict(lambda: collections.defaultdict(list)) # {receiver: {chunk: [sender, ...]}}
    peers = {}

    # seed_chunks populates the vehicles data store
    @classmethod
    def seed_chunks(cls, peer_id, chunk_ids):
        """
            calls when anoter round of transmission task begins
            do not intefere
        
        """
        peer = NetworkPeer(peer_id, chunk_ids)
        cls.peers[peer_id] = peer
        return peer

    @classmethod
    def record_chunk_transaction(cls, sender_id, receiver_id, chunk_id) -> None:
        """
            implement this function for transmission perisitence
        
        """    
        cls.records[receiver_id][chunk_id].append(sender_id)
        
    @classmethod
    def rank_peers(cls) -> list:
        """
            implement this function for rank generation
        
        """
        scores = collections.defaultdict(int)
        queue = collections.deque()
        for recv, sends in cls.records.items():
            for chunk in sends.keys():
                queue.append((recv, chunk))
        while queue:
            recv, chunk = queue.popleft()
            if chunk in cls.peers[recv].chunk_ids: 
                continue
            for send in cls.records[recv][chunk]:
                scores[send] += 1
                queue.append((send, chunk))
        
        return sorted(scores, key=scores.get, reverse=True)
