{
  "name": "Gaia-X",
    "engine": {
    "authorityRound": {
      "params": {
        "stepDuration": 5,
          "maximumUncleCountTransition": 0,
            "maximumUncleCount": 0,
              "validators": {
          "multi": {
            "0": {
              "list": [
                "0x00c1ac54db304c0f618010632b8e6ebc856e4ab0",
                "0x00d370a5c9771e3f894160aed4961b4e8d2e066e",
                "0x00286736829e2e6a125d83682cfdd5f0e0c57f1a"
              ]
            },
            "1287575": {
              "contract": "0xf0c7A31D7Ee26bEBfb4BAD8e37490bEadE3F846f"
            }
          }
        }
      }
    }
  },
  "params": {
    "gasLimitBoundDivisor": "0x400",
      "maximumExtraDataSize": "0x20",
        "minGasLimit": "0x1388",
          "networkID": "0x1ED688",
            "eip140Transition": "0x0",
              "eip211Transition": "0x0",
                "eip214Transition": "0x0",
                  "eip658Transition": "0x0",
                    "eip145Transition": 0,
                      "eip1014Transition": 0,
                        "eip1052Transition": 0,
                          "eip1283Transition": 0,
                            "eip1344Transition": 0,
                              "eip1706Transition": 0,
                                "eip1884Transition": 0,
                                  "eip2028Transition": 0
  },
  "genesis": {
    "seal": {
      "authorityRound": {
        "step": "0x0",
          "signature": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
      }
    },
    "difficulty": "0x20000",
      "gasLimit": "0x663BE0"
  },
  "nodes": [
    "enode://5f106600af9c958b47ab4ef56a1ad83dd852e24073b2e56cf11f4778add49bc0ebe4e35c94690e0164a26200f2f9c7901eab1cec772763424f501a85a5b66b4a@172.31.31.183:30303",
    "enode://9de09bae783e9c923bb4ef97ef78cf0179b0655db59563d4d6d6c8a271d1c180d7e0e346f962f6fa8db240e11e18dafd8f53e0703951befd6bab311ba0b724fd@172.31.29.42:30303",
    "enode://4307594e790104ed027f68d30d2d5beb91ef09b532ed29873a12b19f857099b348f190f96f351fbe0d23764bfde397230555c02c8efc52f019961a434e0a3b4c@172.31.26.105:30303"
  ],
    "accounts": {
    "0x0000000000000000000000000000000000000005": {
      "builtin": {
        "name": "modexp",
          "pricing": {
          "0": {
            "price": {
              "modexp": {
                "divisor": 20
              }
            }
          }
        }
      }
    },
    "0x0000000000000000000000000000000000000006": {
      "builtin": {
        "name": "alt_bn128_add",
          "pricing": {
          "0": {
            "price": {
              "alt_bn128_const_operations": {
                "price": 500
              }
            }
          },
          "12598600": {
            "info": "Istanbul HF",
              "price": {
              "alt_bn128_const_operations": {
                "price": 150
              }
            }
          }
        }
      }
    },
    "0x0000000000000000000000000000000000000007": {
      "builtin": {
        "name": "alt_bn128_mul",
          "pricing": {
          "0": {
            "price": {
              "alt_bn128_const_operations": {
                "price": 40000
              }
            }
          },
          "12598600": {
            "info": "Istanbul HF",
              "price": {
              "alt_bn128_const_operations": {
                "price": 6000
              }
            }
          }
        }
      }
    },
    "0x0000000000000000000000000000000000000008": {
      "builtin": {
        "name": "alt_bn128_pairing",
          "pricing": {
          "0": {
            "price": {
              "alt_bn128_pairing": {
                "base": 100000,
                  "pair": 80000
              }
            }
          },
          "12598600": {
            "info": "Istanbul HF",
              "price": {
              "alt_bn128_pairing": {
                "base": 45000,
                  "pair": 34000
              }
            }
          }
        }
      }
    },
    "0x0000000000000000000000000000000000000009": {
      "builtin": {
        "name": "blake2_f",
          "pricing": {
          "12598600": {
            "info": "Istanbul HF",
              "price": {
              "blake2_f": {
                "gas_per_round": 1
              }
            }
          }
        }
      }
    },
    "0x0000000000000000000000000000000000000001": {
      "balance": "1",
        "builtin": {
        "name": "ecrecover",
          "pricing": {
          "0": {
            "price": {
              "linear": {
                "base": 3000,
                  "word": 0
              }
            }
          }
        }
      }
    },
    "0x0000000000000000000000000000000000000002": {
      "balance": "1",
        "builtin": {
        "name": "sha256",
          "pricing": {
          "0": {
            "price": {
              "linear": {
                "base": 60,
                  "word": 12
              }
            }
          }
        }
      }
    },
    "0x0000000000000000000000000000000000000003": {
      "balance": "1",
        "builtin": {
        "name": "ripemd160",
          "pricing": {
          "0": {
            "price": {
              "linear": {
                "base": 600,
                  "word": 120
              }
            }
          }
        }
      }
    },
    "0x0000000000000000000000000000000000000004": {
      "balance": "1",
        "builtin": {
        "name": "identity",
          "pricing": {
          "0": {
            "price": {
              "linear": {
                "base": 15,
                  "word": 3
              }
            }
          }
        }
      }
    },
    "0xC7EC1970B09224B317c52d92f37F5e1E4fF6B687": {
      "balance": "1000000000000000000000000000"
    }
  }
}