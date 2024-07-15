import unittest
import sys
sys.path.append("..")

from tx_engine import Tx, p2pkh_script, address_to_public_key_hash, TxOut, TxIn


class TxTest(unittest.TestCase):
    def test_parse_version(self):
        raw_tx = bytes.fromhex(
            "0100000001813f79011acb80925dfe69b3def355fe914bd1d96a3f5f71bf8303c6a989c7d1000000006b483045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031ccfcf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9c8e10615bed01210349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e213bf016b278afeffffff02a135ef01000000001976a914bc3b654dca7e56b04dca18f2566cdaf02e8d9ada88ac99c39800000000001976a9141c4bc762dd5423e332166702cb75f40df79fea1288ac19430600"
        )
        tx = Tx.parse(raw_tx)
        self.assertEqual(tx.version, 1)

    def test_parse_inputs(self):
        raw_tx = bytes.fromhex(
            "0100000001813f79011acb80925dfe69b3def355fe914bd1d96a3f5f71bf8303c6a989c7d1000000006b483045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031ccfcf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9c8e10615bed01210349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e213bf016b278afeffffff02a135ef01000000001976a914bc3b654dca7e56b04dca18f2566cdaf02e8d9ada88ac99c39800000000001976a9141c4bc762dd5423e332166702cb75f40df79fea1288ac19430600"
        )
        tx = Tx.parse(raw_tx)
        self.assertEqual(len(tx.tx_ins), 1)
        want = "d1c789a9c60383bf715f3f6ad9d14b91fe55f3deb369fe5d9280cb1a01793f81"

        prev_tx = tx.tx_ins[0].prev_tx
        self.assertEqual(prev_tx, want)

        self.assertEqual(tx.tx_ins[0].prev_index, 0)
        want_script = bytes.fromhex(
            "6b483045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031ccfcf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9c8e10615bed01210349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e213bf016b278a"
        )
        self.assertEqual(tx.tx_ins[0].script_sig.serialize(), want_script)
        self.assertEqual(tx.tx_ins[0].sequence, 0xFFFFFFFE)

    def test_parse_outputs(self):
        raw_tx = bytes.fromhex(
            "0100000001813f79011acb80925dfe69b3def355fe914bd1d96a3f5f71bf8303c6a989c7d1000000006b483045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031ccfcf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9c8e10615bed01210349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e213bf016b278afeffffff02a135ef01000000001976a914bc3b654dca7e56b04dca18f2566cdaf02e8d9ada88ac99c39800000000001976a9141c4bc762dd5423e332166702cb75f40df79fea1288ac19430600"
        )
        tx = Tx.parse(raw_tx)
        self.assertEqual(len(tx.tx_outs), 2)
        want: int = 32454049
        self.assertEqual(tx.tx_outs[0].amount, want)
        actual: bytes = bytes.fromhex("1976a914bc3b654dca7e56b04dca18f2566cdaf02e8d9ada88ac")
        self.assertEqual(tx.tx_outs[0].script_pubkey.serialize(), actual)
        want = 10011545
        self.assertEqual(tx.tx_outs[1].amount, want)
        actual_pubkey: bytes = bytes.fromhex("1976a9141c4bc762dd5423e332166702cb75f40df79fea1288ac")
        self.assertEqual(tx.tx_outs[1].script_pubkey.serialize(), actual_pubkey)

    def test_parse_locktime(self):
        raw_tx = bytes.fromhex(
            "0100000001813f79011acb80925dfe69b3def355fe914bd1d96a3f5f71bf8303c6a989c7d1000000006b483045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031ccfcf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9c8e10615bed01210349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e213bf016b278afeffffff02a135ef01000000001976a914bc3b654dca7e56b04dca18f2566cdaf02e8d9ada88ac99c39800000000001976a9141c4bc762dd5423e332166702cb75f40df79fea1288ac19430600"
        )
        tx = Tx.parse(raw_tx)
        self.assertEqual(tx.locktime, 410393)

    def test_vout(self):
        payment_addr = "mgzhRq55hEYFgyCrtNxEsP1MdusZZ31hH5"
        locking_script = p2pkh_script(address_to_public_key_hash(payment_addr))
        vouts = []
        amt = 100
        vouts.append(TxOut(amount=amt, script_pubkey=locking_script.get_commands()))

    def test_read_vin(self):
        funding_tx = "0100000001baa9ec5094816f5686371e701b3a4dcadc93df44d151496a58089018706b865c000000006b483045022100b53c9ab501032a626050651fb785967e1bdf03bca0cb17cb4f2c75a45a56d17d0220292a27ce9001efb9c41ab9a06ecaaefad91138e94d4407ee14952456274357a24121024f8d67f0a5ec11e72cc0f2fa5c272b69fd448b933f92a912210f5a35a8eb2d6affffffff0276198900000000001976a914661657ba0a6b276bb5cb313257af5cc416450c0888ac64000000000000001976a9147d981c463355c618e9666044315ef1ffc523e87088ac00000000"
        fund_tx = Tx.parse(bytes.fromhex(funding_tx))
        prev_tx = fund_tx.tx_ins[0].prev_tx

        self.assertEqual(prev_tx, "5c866b70189008586a4951d144df93dcca4d3a1b701e3786566f819450eca9ba")

    def test_vin_constructor(self):
        # __init__(prev_tx: bytes, prev_index: int, script_sig: bytes, sequence: int) -> TxIn
        txin = TxIn(prev_tx="5c866b70189008586a4951d144df93dcca4d3a1b701e3786566f819450eca9ba", prev_index=0)
        self.assertTrue(isinstance(txin, TxIn))

    def test_tx_constructor(self):
        # new(version: u32, tx_ins: Vec<PyTxIn>, tx_outs: Vec<PyTxOut>, locktime: u32) -> Self {
        tx = Tx(version=1, tx_ins=[], tx_outs=[])
        self.assertTrue(isinstance(tx, Tx))


if __name__ == "__main__":
    unittest.main()
