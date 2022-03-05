import _thread
import time
import requests
import json
import blocksmith
import secrets
accounts = [
  "0xf977814e90da44bfa03b6295a0616a897441acec",
  "0x4b16c5de96eb2117bbe5fd171e4d203624b014aa",
  "0xa07c5b74c9b40447a954e1466938b865b6bbea36",
  "0x5a52e96bacdabb82fd05763e25335261b270efcb",
  "0x8894e0a0c962cb723c1976a4421c95949be2d4e3",
  "0x21d45650db732ce5df77685d6021d7d5d1da807f",
  "0x41772edd47d9ddf9ef848cdb34fe76143908c7ad",
  "0x1e34a77868e19a6647b1f2f47b51ed72dede95dd",
  "0xc78248d676debb4597e88071d3d889eca70e5469",
  "0x515b72ed8a97f42c568d6a143232775018f133c8",
  "0x3c783c21a0383057d128bae431894a5c19f9cf06",
  "0xbd612a3f30dca67bf60a39fd0d35e39b7ab80774",
  "0x73f5ebe90f27b46ea12e5795d16c4b408b19cc6f",
  "0xeb2d2f1b8c558a40207669291fda468e50c8a0bb",
  "0xdccf3b77da55107280bd850ea519df3705d1a75a",
  "0x29bdfbf7d27462a2d115748ace2bd71a2646946c",
  "0xfd6042df3d74ce9959922fec559d7995f3933c55",
  "0x01c952174c24e1210d26961d456a77a39e1f0bb0",
  "0xe2fc31f816a9b94326492132018c3aecc4a93ae1",
  "0x161ba15a5f335c9f06bb5bbb0a9ce14076fbb645",
  "0x1fbe2acee135d991592f167ac371f3dd893a508b",
  "0xd183f2bbf8b28d9fec8367cb06fe72b88778c86b"
]

ethaccounts = [
  "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
  "0xda9dfa130df4de4673b89022ee50ff26f6ea73cf",
  "0x73bceb1cd57c711feac4224d062b0f6ff338501e",
  "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
  "0x9bf4001d307dfd62b26a2f1307ee0c0307632d59",
  "0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5",
  "0x61edcdf5bb737adffe5043706e7c5bb1f1a56eea",
  "0xdc24316b9ae028f1497c275eb9192a3ea0f67022",
  "0x742d35cc6634c0532925a3b844bc454e4438f44e",
  "0x011b6e24ffb0b5f5fcc564cf4183c5bbbc96d515",
  "0x1b3cb81e51011b549d78bf720b0d924ac763a7c2",
  "0x07ee55aa48bb72dcc6e9d78256648910de513eca",
  "0xc61b9bb3a7a0767e3179713f3a5c7a9aedce193c",
  "0xe92d1a43df510f82c66382592a047d288f85226f",
  "0x8484ef722627bf18ca5ae6bcf031c23e6e922b30",
  "0xf977814e90da44bfa03b6295a0616a897441acec",
  "0xa7efae728d2936e78bda97dc267687568dd593f3",
  "0xdf9eb223bafbe5c5271415c75aecd68c21fe3d7f",
  "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae",
  "0x6262998ced04146fa42253a5c0af90ca02dfd2a3",
  "0xa929022c9107643515f5c777ce9a910f0d1e490c",
  "0x220866b1a2219f40e72f5c628b65d54268ca3a9d",
  "0xca8fa8f0b631ecdb18cda619c4fc9d197c8affca",
  "0x0548f59fee79f8832c299e01dca5c76f034f558e"
]

# Define a function for the thread
def shotAddress( threadName, threadNo):
  while True:
    print(threadNo)
    bits1 = secrets.randbits(256)
    bits_hex1 = hex(bits1)
    private_key1 = bits_hex1[2:]
    if(len(private_key1) == 64):
      address = blocksmith.EthereumWallet.generate_address(private_key1)
      if(address in ethaccounts or address in accounts):
        print("GOAL!")
        print(address, private_key1)
        input_dictionary = {"key" : private_key1, "address" : address}
        file = open("result.txt", "a")
        str = repr(input_dictionary)
        file.write("goal! = " + str + "\n")
        file.close()

# Create two threads as follows
try:
   _thread.start_new_thread( shotAddress, ("Thread-1", 1, ) )
   _thread.start_new_thread( shotAddress, ("Thread-2", 2, ) )
   _thread.start_new_thread( shotAddress, ("Thread-3", 3, ) )
   _thread.start_new_thread( shotAddress, ("Thread-4", 4, ) )
   _thread.start_new_thread( shotAddress, ("Thread-5", 5, ) )
   _thread.start_new_thread( shotAddress, ("Thread-6", 6, ) )

except:
   print ("Error: unable to start thread")

while 1:
   pass



