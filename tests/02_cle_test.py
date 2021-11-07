from config import DefaultConfig

def test_cle_insight():
    
    assert DefaultConfig.APPINSIGHTS_INSTRUMENTATION_KEY == 'c5b691e9-1311-4755-a74a-55c3eb7d2a18'
    
def test_cle_luis():
    
    assert DefaultConfig.LUIS_API_KEY == 'bc9f746c79564223889a7f7b5344ddcd'
