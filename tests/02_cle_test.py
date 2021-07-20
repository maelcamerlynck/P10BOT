from config import DefaultConfig

def test_cle_insight():
    
    assert DefaultConfig.APPINSIGHTS_INSTRUMENTATION_KEY == 'e40dca9d-734c-4acd-810e-93a94c9ffac3'
    
def test_cle_luis():
    
    assert DefaultConfig.LUIS_API_KEY == '7bccf58a81bf4e43bedb92e2272fe87f'
    
