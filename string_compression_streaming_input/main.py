from  streaming_string_compress import Compressor


def main():
    
    compressor = Compressor()
    
    assert  compressor.compress("bc") == "bc", "failure in compressing single symbols"
    
    compressor.reset()
    
    assert compressor.compress("aaa") == "a3", "failure in compressing consecutive symbols"

    assert  compressor.compress("bc") == "a3bc", "failure in streaming-compressing symbols"

    assert  compressor.compress("c") == "a3bc2", "failure in streaming-compressing symbols with merge design"
    
    assert  compressor.compress("2") == "a3bc2_2", "failure in compressing symbols with encode escaper"
    
    assert  compressor.compress("21") == "a3bc2_22_1", "failure in compressing symbols with encode escaper"

    assert compressor.compress("") == "a3bc2_22_1", "failure in streaming-compressing void symbol"

    print("overall success")


if __name__ == "__main__":
    main()
